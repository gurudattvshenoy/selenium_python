import os
import json
import pathlib

test_constant = {}

def read_config(key):
    global test_constant
    if len(test_constant) == 0:
        path = pathlib.Path(__file__).parent.absolute()
        with open( os.path.join(path,"test_config.json")) as f:
            test_constant = json.load(f)
    return test_constant.get(key)

class TestConstants:
    BROWSER = read_config('browser')
    URL = read_config('url')
    MODE = read_config('debug_mode')
    IMPLICIT_TIMEOUT = read_config("implicit_timeout")
    EXPLICIT_TIMEOUT = read_config("explicit_timeout")
    LOG_FILENAME= read_config('log_filename')


