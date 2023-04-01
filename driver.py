from dataset.AlexaTopOneMillionUrls import AlexaTopOneMillionUrls
from environment.SingleTabBrowserEnvironment import SingleTabBrowserEnvironment
from experiments.ForeGroundExperiment import ForeGroundExperiment
from webdriver.WebDriverSingleton import WebDriverSingleton

if __name__ == '__main__':
    alexa_top = AlexaTopOneMillionUrls('dataset/alexa-top-1-million/top-1m.csv')
    driver = WebDriverSingleton()
    single_tab_browser = SingleTabBrowserEnvironment(alexa_top, driver)
    fore_ground_experiment = ForeGroundExperiment(single_tab_browser, alexa_top, driver)
    fore_ground_experiment.run_experiment()

