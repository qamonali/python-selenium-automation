from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when("Click on Cart icon")
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()
    sleep(2)

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")
