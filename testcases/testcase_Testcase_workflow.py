import os
import sys
import pytest

# 1. Append project root to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# 2. Main execution entrypoint
if __name__ == "__main__":
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
from step_defs.step_common import *
from step_defs.step_testcase_workflow import *

scenarios("../features/testcase_workflow.feature")