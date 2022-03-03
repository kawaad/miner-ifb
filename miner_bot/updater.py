import json

from utils.campuses import campuses_info
from scraper import Scraper


class Updater:

    with open('utils/last_news_updates.json') as json_file:
        last_news_updates = json.load(json_file)

    def first_step(self):
        for campus_key, campus_value in campuses_info.items():
            campus_links = campus_value['links']
            for link_key, link_value in campus_links.items():

                # last_update = last_news_updates[campus_key][link_key]

                scraper = Scraper()

                news_list = scraper.start_requests(url=link_value)
                # step 2 - prepare message to send

    # implement write json file after message send


if __name__ == "__main__":
    updater = Updater()
    updater.first_step()
