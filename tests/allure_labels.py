import pytest
import allure
from allure_commons.types import Severity


@pytest.fixture(autouse=True)
def general_labels():
    allure.dynamic.tag("web")
    allure.dynamic.label("owner", "solveyga")
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.link("https://github.com", name="Testing")
    yield
