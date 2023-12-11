import requests

token = "BotToken"
chat_id = "ChatId"
text = "Hello, World!"

url = f"https://api.telegram.org/bot{token}/sendMessage"
data = {"chat_id": chat_id, "text": text}

response = requests.post(url, data=data)