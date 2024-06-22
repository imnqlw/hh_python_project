import os

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from dotenv import load_dotenv

name = os.getenv('name')
wrong_pass = os.getenv('wrong_pass')
text = os.getenv('text')
load_dotenv()



@allure.epic('unsuccess login')
@allure.story('unsuccess login')
@allure.feature('unsuccess login')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity('normal')
def test_unsuccess_login():
    with allure.step('Click button  have account'):
        browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_intentions_onboarding_choose_direction_button_have_account')).click()

    with allure.step('Click button use mail/pass'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(3)')).click()
    with allure.step('Login'):
        browser.element((AppiumBy.ID, 'ru.hh.android:id/view_hh_button_title_text_view')).click()

    with allure.step('Type login'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Почта")')).type(name)

    with allure.step('Type wrong_pass'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Пароль")')).type(wrong_pass)

    with allure.step('Login with login/wrong_pass'):
        browser.element((AppiumBy.ID, 'ru.hh.android:id/view_title_button_button')).click()

    with allure.step('unsuccess login'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ru.hh.android:id/snackbar_text")')).should(have.text('Неправильные данные для входа. Пожалуйста, попробуйте снова.'))





