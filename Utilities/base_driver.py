


class BaseDriver():

    def __init__(self, driver):
        self.driver = driver

    def cap_screenshot(self, folder_num, ss_num):

        ss_name = f'C:\\python-appium\\simple-demo\\Screenshot\\TC_{folder_num}\\{ss_num}.png'
        self.driver.save_screenshot(ss_name)


