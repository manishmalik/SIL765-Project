from dataset.AlexaTopOneMillionUrls import AlexaTopOneMillionUrls
from environment.BrowserEnvironment import BrowserEnvironment
from experiments.BackGroundExperiment import BackGroundExperiment
from experiments.DNSNotVisitedExperiment import DNSNotVisitedExperiment
from experiments.DNSVisitedExperiment import DNSVisitedExperiment
from experiments.ForeGroundExperiment import ForeGroundExperiment
from experiments.NotPresentExperiment import NotPresentExperiment
from webdriver.WebDriverSingleton import WebDriverSingleton

if __name__ == '__main__':
    alexa_top = AlexaTopOneMillionUrls('dataset/alexa-top-1-million/top-1m.csv')
    driver = WebDriverSingleton()
    browser_env = BrowserEnvironment(driver)
    dns_visited_experiment = DNSVisitedExperiment(browser_env, alexa_top, driver)
    dns_visited_experiment.run_experiment()

    dns_not_visited_experiment = DNSNotVisitedExperiment(browser_env, alexa_top, driver)
    dns_not_visited_experiment.run_experiment()