from appium.webdriver.common.touch_action import TouchAction


class BaseDriver():

    def __init__(self, driver):
        self.driver = driver

    def cap_screenshot(self, folder_num, ss_num):
        ss_name = f'C:\\python-appium\\simple-demo\\Screenshot\\TC_{folder_num}\\{ss_num}.png'
        self.driver.save_screenshot(ss_name)

    def get_scroll(self, x1, y1, x2, y2, dur):
        self.driver.swipe(x1, y1, x2, y2, dur)

    def get_keys_keycode(self, keycode):
        self.driver.press_keycode(keycode)

    def get_tap_screen(self, xcor, ycor):

        user_action = TouchAction(self.driver)
        user_action.tap(x=xcor, y=ycor).perform()
