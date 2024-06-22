import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have



@allure.epic('Support')
@allure.story('Send text in support chat')
@allure.feature('Support')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity('high')
def test_hh_support():
    with allure.step('Tape support button'):
        browser.element((AppiumBy.ID, 'ru.hh.android:id/view_hh_button_small_thin_title_text_view')).click()

    with allure.step('Type text in support chat'):
        browser.element((AppiumBy.ID, 'ru.hh.android:id/view_chat_message_input_edit_text')).type('Test')

    with allure.step('Send text in support chat'):
        browser.element((AppiumBy.ID, 'ru.hh.android:id/view_chat_message_input_image_send')).click()

    with allure.step('Check text'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Test")')).should(have.text('Test'))
