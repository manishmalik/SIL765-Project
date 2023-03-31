from WebDriverSingleton import WebDriverSingleton
import time

class BrowserEnvironment:
    """
    Interface for an environment that can open new tabs and switch tabs by URL.
    """
    def __init__(self):
        self.driver = WebDriverSingleton()
        self.url_to_tab_map = {}

    def open_new_tab(self, url):
        self.driver.execute_script('window.open("");')
        tab_index = len(self.driver.window_handles) - 1
        self.driver.switch_to.window(self.driver.window_handles[tab_index])
        self.driver.get('http://' + url)
        self.url_to_tab_map[url] = tab_index

    def switch_tab(self, url):
        if url in self.url_to_tab_map:
            tab_index = self.url_to_tab_map[url]
            self.driver.switch_to.window(self.driver.window_handles[tab_index])
        else:
            raise ValueError("URL '{}' not found in open tabs.".format(url))

    def close_tab(self, url):
        if url in self.url_to_tab_map:
            tab_index = self.url_to_tab_map[url]
            self.driver.switch_to.window(self.driver.window_handles[tab_index])
            self.driver.close()
            del self.url_to_tab_map[url]
        else:
            raise ValueError("URL '{}' not found in open tabs.".format(url))