
from messenger import Messenger
from scraper import Scraper

from utils.campuses import campuses_info
from utils.updates import Updates


class Updater:

    file_path = 'utils/last_news_updates.json'

    def first_step(self):

        for campus_key, campus_value in campuses_info.items():
            campus_links = campus_value['links']

            for link_key, link_value in campus_links.items():
                news_list = Scraper().start_requests(url=link_value)
                for news_key, news_values in news_list.items():
                    messenger = Messenger(news_key, news_values, campus_key, link_key, self.file_path)
                    messenger.update()


if __name__ == "__main__":
    updater = Updater()
    updater.first_step()
