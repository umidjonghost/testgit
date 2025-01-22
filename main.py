import requests

class WebScrapingStudy:

    def __init__(self, url, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.url = url

    @staticmethod
    def send_telegram_message(token, chat_id, message: str):
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": message}
        requests.post(url=url, data=data)

    @staticmethod
    def get_json_data(url: str):
        response = requests.get(url)
        return response.json().get("data")










