import time

from selenium.webdriver.common.by import By

from dataset import AlexaTopOneMillionUrls
from dataset.FileAppender import FileAppender
from experiments.IExperiment import IExperiment


class DNSVisitedExperiment(IExperiment):
    """
    Interface for an environment that can open new tabs and switch tabs by URL.
    """
    current_url = None
    TOP_URL_COUNT = 1000
    START_IDX = 0
    def __init__(self, browser_env, alexa_top_1_mil: AlexaTopOneMillionUrls, driver):
        self.driver = driver
        self.file = FileAppender('dataset/experiment_results/dns_visited_experiment.csv')
        self.ATTACK_URL = 'file:///C:/Users/manis/Documents/GitHub/SIL765-Project/dns.html'
        super().__init__(browser_env, alexa_top_1_mil)

    def prepare_experiment(self):
        # execute JavaScript to clear the DNS cache
        self.driver.get("chrome://net-internals/#dns")
        self.driver.find_element(By.ID, 'dns-view-clear-cache').click()

        #open victim
        self.browser_env.open_new_tab('http://' + self.current_url)

        # open attack page
        self.browser_env.open_new_tab(self.ATTACK_URL)

    def run_experiment(self):
        print("Running DNS Visited Experiment:")
        count = self.START_IDX + 1
        for url in self.alexa_dataset.get_top_urls(self.START_IDX, self.TOP_URL_COUNT):
            try:
                self.current_url = url

                # prepare environment for experiment
                self.prepare_experiment()

                # switch to attack site tab
                self.browser_env.switch_tab(self.ATTACK_URL)

                url_to_resolve = self.driver.find_element(By.ID, "url")

                # enter values for reference site and victim site
                url_to_resolve.send_keys(url)

                # find the compute button and click it
                compute_btn = self.driver.find_element(By.ID, "compute_btn")
                compute_btn.click()
                time.sleep(3)

                result_el = self.driver.find_element(By.ID, "result")
                result = result_el.text

                res_str = '{}\t{}'.format(url, result)
                print('{}/{}: {}'.format(count, self.TOP_URL_COUNT, res_str))
                self.file.append(res_str)

                # clean up environment post experiment
                self.clean_up()
            except Exception as e:
                print("An error occurred while processing the URL {}: {}".format(url, e))
            count = count + 1

        self.file.complete()

        print("DNS Visited Experiment completed.")

    def clean_up(self):
        self.browser_env.close_tab('http://' + self.current_url)
        self.browser_env.close_tab(self.ATTACK_URL)
