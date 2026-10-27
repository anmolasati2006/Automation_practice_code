import os
import subprocess
import sys
import pytest
from playwright.sync_api import Page, expect, sync_playwright

# Ensure project root is present in Python path regardless of execution directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from config.config import TIMEOUT
from Pages.contact_us_page import Contact_us
from Pages.signup_login_page import SignupLogin
from Pages.testcase_page import Testcase
from Pages.products_page import Search_Products
from Pages.home_page import *

# Automatically register step definitions so pytest-bdd finds them globally
pytest_plugins = [
    "step_defs.step_common",
    "step_defs.step_registrations_workflows",
    "step_defs.step_contact_us_workflow",
    "step_defs.step_login_workflows",
    "step_defs.step_testcase_workflow",
    "step_defs.step_products_search_workflows",
    "step_defs.step_home_page_workflow",
]


# ==========================================
# PLAYWRIGHT & PAGE FIXTURES
# ==========================================


@pytest.fixture(scope="function")
def setup_page():
    """Launches browser maximized, configures default timeouts, and navigates to the login page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        page.set_default_timeout(TIMEOUT)
        page.set_default_navigation_timeout(TIMEOUT)

        page.goto(
            "https://automationexercise.com/login", wait_until="domcontentloaded"
        )
        expect(page.get_by_role("link", name="Home")).to_be_visible()

        yield page

        context.close()
        browser.close()


@pytest.fixture
def signup_page(setup_page):
    """Instantiates the SignupLogin Page Object."""
    return SignupLogin(setup_page)


@pytest.fixture
def contact_us(setup_page):
    """Instantiates the Contact_us Page Object."""
    return Contact_us(setup_page)


@pytest.fixture
def testcase_page(setup_page):
    """Instantiates the Testcase Page Object."""
    return Testcase(setup_page)

@pytest.fixture
def products_page(setup_page):
    """Instantiates the Search Products Page Object."""
    return Search_Products(setup_page)

@pytest.fixture
def homepage(setup_page):
    """Instantiates the Search Products Page Object."""
    return Homepage(setup_page)


# ==========================================
# AUTOMATIC ALLURE REPORT HOOK
# ==========================================


def pytest_sessionfinish(session, exitstatus):
    """Executes after test run completion to compile and launch the interactive Allure Dashboard."""
    results_dir = os.path.join(PROJECT_ROOT, "reports", "allure-results")
    report_dir = os.path.join(PROJECT_ROOT, "reports", "allure-report")

    # Paths to project-local Allure CLI and JDK
    allure_bat = os.path.join(
        PROJECT_ROOT, "allure-2.46.1", "bin", "allure.bat"
    )
    jdk_dir = os.path.join(PROJECT_ROOT, "jdk-27")
    java_bin = os.path.join(jdk_dir, "bin")

    # Inject project-local JAVA_HOME and bin path dynamically
    env = os.environ.copy()
    env["JAVA_HOME"] = jdk_dir
    env["PATH"] = java_bin + os.pathsep + env.get("PATH", "")

    if os.path.exists(results_dir) and os.listdir(results_dir):
        print("\n[ALLURE HOOK] Compiling raw JSON into Allure Dashboard...")

        # Step 1: Generate interactive HTML report
        gen_result = subprocess.run(
            f'"{allure_bat}" generate "{results_dir}" -o "{report_dir}" --clean',
            shell=True,
            capture_output=True,
            text=True,
            env=env,
        )

        if gen_result.returncode == 0:
            print(
                f"[ALLURE HOOK SUCCESS] Report compiled at: {os.path.abspath(report_dir)}"
            )
            print("[ALLURE HOOK] Opening dashboard in your default browser...")

            # Step 2: Serve and launch interactive dashboard
            subprocess.Popen(
                f'"{allure_bat}" open "{report_dir}"',
                shell=True,
                env=env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        else:
            print(
                f"[ALLURE HOOK ERROR] Allure CLI Failed:\n{gen_result.stderr}"
            )
    else:
        print(
            "\n[ALLURE HOOK WARNING] No JSON files found in reports/allure-results."
        )