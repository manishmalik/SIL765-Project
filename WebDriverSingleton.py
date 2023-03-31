from selenium import webdriver


class WebDriverSingleton:
    """
    Singleton class to handle a single instance of the WebDriver.
    """
    _instance = None

    def __new__(cls):
        if not cls._instance:
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-infobars')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            cls._instance = webdriver.Chrome(options=options)
        return cls._instance