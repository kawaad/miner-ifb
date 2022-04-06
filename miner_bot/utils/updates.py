import json


class Updates:

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path) as json_file:
            return json.load(json_file)

    def write(self, last_news_dict):
        with open(self.file_path, 'w') as json_file:
            json_string = json.dumps(last_news_dict)
            json_file.write(json_string)
