from dataset.AlexaTopOneMillionUrls import AlexaTopOneMillionUrls
from environment.SingleTabBrowserEnvironment import SingleTabBrowserEnvironment
from experiments.BackGroundExperiment import BackGroundExperiment
from experiments.ForeGroundExperiment import ForeGroundExperiment
from experiments.NotPresentExperiment import NotPresentExperiment
from webdriver.WebDriverSingleton import WebDriverSingleton

if __name__ == '__main__':
    alexa_top = AlexaTopOneMillionUrls('dataset/alexa-top-1-million/top-1m.csv')
    driver = WebDriverSingleton()
    single_tab_browser = SingleTabBrowserEnvironment(alexa_top, driver)
    # fore_ground_experiment = ForeGroundExperiment(single_tab_browser, alexa_top, driver)
    # fore_ground_experiment.run_experiment()

    # back_ground_experiment = BackGroundExperiment(single_tab_browser, alexa_top, driver)
    # back_ground_experiment.run_experiment()

    np_experiment = NotPresentExperiment(single_tab_browser, alexa_top, driver)
    np_experiment.run_experiment()

