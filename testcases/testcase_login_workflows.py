import os
import sys
import pytest

# 1. Append project root to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from step_defs.step_common import *
from step_defs.step_login_workflows import *

# 2. Main block at the top
if __name__ == "__main__":
    # Runs pytest targeting this exact file and outputs allure results
    sys.exit(
        pytest.main(
            [
                os.path.abspath(__file__),
                "-v",
                "-s",
                "--alluredir=reports/allure-results",
            ]
        )
    )

from pytest_bdd import scenarios

# 3. Scenarios call below main
scenarios("../features/login_workflows.feature")