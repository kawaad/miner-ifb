import telebot

from time import sleep
from bot_auth_token import token

from utils.updates import Updates
from utils.campuses import campuses_info


class Messenger:

    def __init__(self, news_key, news_values, campus_key, link_key, file_path):
        self.news_key = news_key
        self.news_values = news_values
        self.campus_key = campus_key
        self.link_key = link_key
        self.file_path = file_path

    bot = telebot.TeleBot(token['auth_token'])

    def update(self):
        last_news_updates = Updates(file_path=self.file_path).read()
        self.send_message()
        self.update_last(last_news_updates)
        sleep(1)

    def update_last(self, last_news_updates):
        last_update_date = last_news_updates[self.campus_key][self.link_key]
        import pdb;pdb.set_trace()
        object_dict = last_news_updates.get(self.campus_key)
        object_dict.update({self.link_key: self.news_values.get('datetime')})
        last_news_updates.update(object_dict)
        Updates(file_path=self.file_path).write(last_news_dict=last_news_updates)

    def send_message(self):
        channel_id = campuses_info[self.campus_key]['channel']
        image = self.news_values.get('image')
        title = self.news_key
        url = self.news_values.get('url')
        if not image:
            self.bot.send_message(chat_id=channel_id, text=f"\n*{title}* \n\n{url}\n", parse_mode="markdown", disable_web_page_preview=True)
        else:
            self.bot.send_photo(chat_id=channel_id, photo=image, caption=f"\n*{title}*\n{url}", parse_mode="markdown")
