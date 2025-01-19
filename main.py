# import requests
#
# class WebScrapingStudy:
#
#     def __init__(self, url, token, chat_id):
#         self.token = token
#         self.chat_id = chat_id
#         self.url = url
#     @staticmethod
#     def send_telegram_message(token, chat_id, message:str):
#         url = f"https://api.telegram.org/bot{token}/sendMessage"
#         data = {"chat_id": chat_id, "text": message}
#         requests.post(url=url, data=data)
#
#     @staticmethod
#     def get_json_data(url):
#         response = requests.get(url)
#         return response.json().get("data")
#
#     def run_script(self):
#         responses = self.get_json_data(self.url)
#         for response  in responses:
#             name = response.get("name")
#             self.send_telegram_message(token=self.token,chat_id=self.chat_id, message=name )
#         return responses
#
#
# token = "7887430713:AAFmBTOcwNeB6C6dNY2xuFmx_0iMnvKYmHM"
# chat_id = 5990731338
# url = "https://admin.soffstudy.uz/api/v1/gallery/?limit=9&offset=0"
# wss1 = WebScrapingStudy(url=url, token=token, chat_id=chat_id)
# wss1.run_script()




