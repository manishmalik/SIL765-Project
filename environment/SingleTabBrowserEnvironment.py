from dataset.AlexaTopOneMillionUrls import AlexaTopOneMillionUrls
from environment.BrowserEnvironment import BrowserEnvironment
from webdriver import WebDriverSingleton


class SingleTabBrowserEnvironment(BrowserEnvironment):
    """
    Implementation of BrowserEnvironment that opens only one additional tab.
    """
    urls_opened = []

    def __init__(self, data_source: AlexaTopOneMillionUrls, driver: WebDriverSingleton):
        super().__init__(driver)
        for url in data_source.get_random_urls(1):
            self.open_new_tab('http://' + url)
            self.urls_opened.append(url)

    def get_opened_urls(self):
        return self.urls_opened
