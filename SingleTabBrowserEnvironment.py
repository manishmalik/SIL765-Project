from AlexaTopOneMillionUrls import AlexaTopOneMillionUrls
from environment.BrowserEnvironment import BrowserEnvironment


class SingleTabBrowserEnvironment(BrowserEnvironment):
    """
    Implementation of BrowserEnvironment that opens only one additional tab.
    """

    def __init__(self, data_source: AlexaTopOneMillionUrls):
        super().__init__()
        for url in data_source.get_random_urls(1):
            self.open_new_tab(url)
