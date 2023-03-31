import AlexaTopOneMillionUrls
from environment import BrowserEnvironment


class IExperiment:
    """
    Interface for an environment that can open new tabs and switch tabs by URL.
    """

    def __init__(self, browser_env: BrowserEnvironment, alexa_top_1_mil: AlexaTopOneMillionUrls):
        self.browser_env = browser_env
        self.alexa_dataset = alexa_top_1_mil

    def prepare_experiment(self):
        pass

    def run_experiment(self):
        pass

    def clean_up(self):
        pass
