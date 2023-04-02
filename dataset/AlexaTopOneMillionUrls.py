import csv
import random


class AlexaTopOneMillionUrls:
    """
    Class to read a CSV file with a list of URLs and provide methods to
    return the top 3000 URLs and k random URLs from the rest of the list.
    """
    k = 0

    def __init__(self, csv_filename):
        self.urls = []
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                self.urls.append(row[1])

    def get_top_urls(self, top_k_urls):
        self.k = top_k_urls
        return self.urls[:top_k_urls]

    def get_top_urls(self, start, top_k_urls):
        self.k = top_k_urls
        return self.urls[start:top_k_urls]

    def get_random_urls(self, n_random_urls):
        return random.sample(self.urls[self.k:], n_random_urls)