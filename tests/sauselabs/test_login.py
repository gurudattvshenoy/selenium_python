import pytest
from lib.Logger import log_to_file

credentials = [
    ("standard_user","secret_sauce"),
    #("locked_out_user","secret_sauce"),
    #("problem_user","secret_sauce"),
    #("performance_glitch_user","secret_sauce")
]
@pytest.mark.parametrize('username,password',credentials)
def test_case1(saucelabs_helper,username,password):
    log_to_file.info("Testing Login using username -{} and password-{}".format(username,password))
    saucelabs_helper.click_login(username,password)
    assert saucelabs_helper.get_app_logo_text() =="Swag Labs"
