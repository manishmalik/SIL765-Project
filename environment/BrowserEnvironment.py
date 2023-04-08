from urllib.parse import urlparse

from webdriver.WebDriverSingleton import WebDriverSingleton


class BrowserEnvironment:
    """
    Interface for an environment that can open new tabs and switch tabs by URL.
    """
    def __init__(self, driver: WebDriverSingleton):
        self.driver = driver
        self.url_map = {}

    def open_new_tab(self, url):
        self.driver.execute_script('window.open("");')
        new_tab_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab_handle)
        try:
            self.driver.get(url)
            self.url_map[url] = self.driver.current_url
            return True
        except Exception as e:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            print("An error occurred while opening the URL {}: {}".format(url, e))
            return False


    def urls_equal(self, url1, url2):
        """
        Compares two URLs and returns True if they are considered equivalent.
        """
        parsed_url1 = urlparse(url1)
        parsed_url2 = urlparse(url2)
        domain1 = parsed_url1.netloc.replace("www.", "")
        domain2 = parsed_url2.netloc.replace("www.", "")

        return domain1 == domain2 or domain1.split('.')[0] == domain2.split('.')[0]

    def switch_tab(self, url):
        for tab_index in range(len(self.driver.window_handles)):
            self.driver.switch_to.window(self.driver.window_handles[tab_index])
            current_url = self.driver.current_url
            if 'data:,' == current_url:
                continue
            if current_url.startswith('file:') and current_url == url:
                self.driver.switch_to.window(self.driver.window_handles[tab_index])
                return

            if self.urls_equal(current_url, url) or self.urls_equal(current_url, self.url_map[url]):
                self.driver.switch_to.window(self.driver.window_handles[tab_index])
                return
        raise ValueError("URL '{}' not found in open tabs.".format(url))

    def close_tab(self, url):
        try:
            self.switch_tab(url)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            del self.url_map[url]
        except Exception as e:
            print("An error occurred while closing processing the URL {}: {}".format(url, e))
