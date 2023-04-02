import time

from dataset import AlexaTopOneMillionUrls
from dataset.FileAppender import FileAppender
from experiments.IExperiment import IExperiment


class ForeGroundExperiment(IExperiment):
    """
    Interface for an environment that can open new tabs and switch tabs by URL.
    """
    current_url = None
    TOP_URL_COUNT = 1000
    START_IDX = 64
    def __init__(self, browser_env, alexa_top_1_mil: AlexaTopOneMillionUrls, driver):
        self.driver = driver
        self.file = FileAppender('dataset/alexa-top-1-million/foreground_experiment.csv')
        super().__init__(browser_env, alexa_top_1_mil)

    def prepare_experiment(self):
        self.browser_env.open_new_tab('http://' + self.current_url)
        self.browser_env.open_new_tab(self.ATTACK_URL)

    def find_median(self, double_list):
        double_list = [float(x) for x in double_list]  # Convert string values to float
        double_list.sort()  # Sort the list

        # Find median
        n = len(double_list)
        if n % 2 == 0:
            median = (double_list[n // 2 - 1] + double_list[n // 2]) / 2
        else:
            median = double_list[n // 2]

        return median

    def run_experiment(self):
        print("Running Foreground Experiment:")
        count = self.START_IDX + 1
        for url in self.alexa_dataset.get_top_urls(self.START_IDX, self.TOP_URL_COUNT):
            try:
                self.current_url = url

                # prepare environment for experiment
                self.prepare_experiment()

                # switch to attack site tab
                self.browser_env.switch_tab(self.ATTACK_URL)

                ref_site_url = "http://google.com:1"
                victim_site_url = 'http://' + url + ':1'

                ref_site = self.driver.find_element("id", "reference_site")
                vic_site = self.driver.find_element("id", "victim_site")

                # enter values for reference site and victim site
                ref_site.send_keys(ref_site_url)
                vic_site.send_keys(victim_site_url)

                # find the compute button and click it
                compute_btn = self.driver.find_element("id", "compute_btn")
                compute_btn.click()

                # switch to foreground tab
                self.browser_env.switch_tab('http://' + self.current_url)
                time.sleep(22)

                # switch back to attack page
                self.browser_env.switch_tab(self.ATTACK_URL)

                result_el = self.driver.find_element("id", "results")
                results = result_el.text.split('\n')
                res_str = '{}\t{}'.format(url, self.find_median(results))
                print('{}/{}: {}'.format(count, self.TOP_URL_COUNT, res_str))
                self.file.append(res_str)

                # clean up environment post experiment
                self.clean_up()
            except Exception as e:
                print("An error occurred while processing the URL {}: {}".format(url, e))
            count = count + 1

        self.file.complete()

        print("Foreground Experiment completed.")

    def clean_up(self):
        self.browser_env.close_tab('http://' + self.current_url)
        self.browser_env.close_tab(self.ATTACK_URL)
