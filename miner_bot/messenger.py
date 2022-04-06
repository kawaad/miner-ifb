import telebot
import requests

from time import sleep
from bot_auth_token import token

from utils.files_utils import FilesUtils
from utils.campuses import campuses_info


class Messenger:

    def __init__(self, news, campus_key, link_key, file_path):
        self.news = news
        self.campus_key = campus_key
        self.link_key = link_key
        self.file_path = file_path

    bot = telebot.TeleBot(token['auth_token'])

    def update(self):

        self.send_message()
        self.update_last_date()
        sleep(1)

    def update_last_date(self):
        last_news_updates = FilesUtils(file_path=self.file_path).read()
        last_update_date = last_news_updates[self.campus_key][self.link_key]
        news_datetime = self.news.get('datetime')
        object_dict = last_news_updates.get(self.campus_key)
        if news_datetime > last_update_date:
            object_dict.update({self.link_key: news_datetime})
        else:
            object_dict.update({self.link_key: last_update_date})
        last_news_updates.update(object_dict)
        FilesUtils(file_path=self.file_path).write(last_news_dict=last_news_updates)

    def send_message(self):
        channel_id = campuses_info[self.campus_key]['channel']
        image = self.news.get('image')
        title = self.news.get('title')
        url = self.news.get('url')
        if not image:
            self.bot.send_message(chat_id=channel_id, text=f"\n*{title}* \n\n{url}\n", parse_mode="markdown", disable_web_page_preview=True)
        elif 'jpg' in image:
            FilesUtils(file_path='utils/temp.jpg').save_image(image)
            import pdb;pdb.set_trace()
            self.bot.send_photo(chat_id=channel_id, photo=image, caption=f"\n*{title}*\n{url}", parse_mode="markdown")
        else:
            self.bot.send_photo(chat_id=channel_id, photo=image, caption=f"\n*{title}*\n{url}", parse_mode="markdown")
