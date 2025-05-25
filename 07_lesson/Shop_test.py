from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from OpenShop import OpenShop
from BasketShop import Basket
from CheckProductShop import CheckProduct
from YourInformation import YourInformation
from CheckResultShop import Result


def test_shop():
    browser= webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    open = OpenShop(browser)
    open.avtorisation_login("standard_user")
    open.avtorisation_password("secret_sauce")
    open.click()

    add_prod = Basket(browser)
    add_prod.add_product()
    add_prod.click_basket()

    check_prod = CheckProduct(browser)
    check_prod.check_product()
    check_prod.click_checkout()

    inform = YourInformation(browser)
    inform.add_information()
    
    result = Result(browser)
    total = result.check_result()

    browser.quit()

    assert total == "$58.29"
  