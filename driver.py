from AlexaTopOneMillionUrls import AlexaTopOneMillionUrls
from environment.SingleTabBrowserEnvironment import SingleTabBrowserEnvironment
from experiments.ForeGroundExperiment import ForeGroundExperiment

if __name__ == '__main__':
    alexa_top = AlexaTopOneMillionUrls('top-1m.csv')
    single_tab_browser = SingleTabBrowserEnvironment(alexa_top)
    fore_ground_experiment = ForeGroundExperiment(single_tab_browser, alexa_top)
    fore_ground_experiment.run_experiment()

