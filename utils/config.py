import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOGIN_URL = "file:///" + BASE_DIR + "/sample_web_pages/login.html"
REGISTER_URL = "file:///" + BASE_DIR + "/sample_web_pages/register.html"
