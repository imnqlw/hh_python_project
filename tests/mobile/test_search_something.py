# from appium.webdriver.common.appiumby import AppiumBy
# from selene import browser, have
#
#
#
#
#
#
#
#
# def test_search_something():
#     browser.element((AppiumBy.ID, 'ru.hh.android:id/fragment_intentions_onboarding_choose_direction_button_have_account')).click()
#     browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(3)')).click()
#     browser.element((AppiumBy.ID, 'ru.hh.android:id/view_hh_button_title_text_view')).click()
#     browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Почта")')).type('qaqurupython@gmail.com')
#     browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Пароль")')).type('12344321')
#     browser.element((AppiumBy.ID, 'ru.hh.android:id/view_title_button_button')).click()
#     browser.element((AppiumBy.ID, 'ru.hh.android:id/view_main_search_text_view_position')).click()
#     browser.element((AppiumBy.ID, 'ru.hh.android:id/view_main_search_container')).type('Python').press_enter()
#     browser.element((AppiumBy.ID, 'ru.hh.android:id/cell_vacancy_card_text_view_job_position')).should(have.text('Python Backend developer'))