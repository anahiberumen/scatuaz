# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture
from selenium.webdriver import Chrome

@fixture
def browser_chorome(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.driver = Chrome()
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.quit()

def before_all(context):
    use_fixture(browser_chorome, context)
    # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook.