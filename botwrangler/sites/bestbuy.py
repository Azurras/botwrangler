from twill import browser
from twill.commands import *

class BestBuy:
    domain = "https://www.bestbuy.com/"
    login_step1 = "https://www.bestbuy.com/identity/signin?token=tid%3A2f1772cc-2ff6-11ee-b3ff-0a3a0094f93f"
    username_input_id = "fld-e"
    password_input_id = "fld-p1"

    def login(self):
        pass


browser.go("https://www.python.org/")
assert 'Python' in browser.html
find("Documentation")
browser.showforms()

