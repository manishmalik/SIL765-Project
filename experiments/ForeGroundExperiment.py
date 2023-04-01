from dataset import AlexaTopOneMillionUrls
from experiments.IExperiment import IExperiment


class ForeGroundExperiment(IExperiment):
    """
    Interface for an environment that can open new tabs and switch tabs by URL.
    """
    current_url = None

    def __init__(self, browser_env, alexa_top_1_mil: AlexaTopOneMillionUrls, driver):
        self.driver = driver
        super().__init__(browser_env, alexa_top_1_mil)

    def prepare_experiment(self):
        self.browser_env.open_new_tab(self.current_url)

    def run_experiment(self):
        for url in self.alexa_dataset.get_top_urls(10):
            self.current_url = url
            self.prepare_experiment()
            self.clean_up()

    def clean_up(self):
        self.browser_env.close_tab(self.current_url)
