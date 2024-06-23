import os

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from dotenv import load_dotenv

name = os.getenv('name')
passw = os.getenv('passw')
text = os.getenv('text')
load_dotenv()


@allure.epic('Resume')
@allure.story('Resume')
@allure.feature('Resume')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity('normal')
def test_hh_resume():
    with allure.step('Click button  have account'):
        browser.element((AppiumBy.ID,
                         'ru.hh.android:id/fragment_intentions_onboarding_choose_direction_button_have_account')).click()

    with allure.step('Click button use mail/pass'):
        browser.element(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(3)')).click()

    with allure.step('Login'):
        browser.element((AppiumBy.ID, 'ru.hh.android:id/view_hh_button_title_text_view')).click()

    with allure.step('Type login'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Почта")')).type(name)

    with allure.step('Type pass'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Пароль")')).type(passw)

    with allure.step('Login with login/pass'):
        browser.element((AppiumBy.ID, 'ru.hh.android:id/view_title_button_button')).click()

    with allure.step('Select profile'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Профиль")')).click()

    with allure.step('Find resume'):
        browser.element((AppiumBy.ID, 'ru.hh.android:id/view_resume_header_text_view_title')).should(have.text(text))
