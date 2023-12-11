import requests
from azure.iotcentral.models import Template
from azure.iotcentral.devices import Device, DeviceManager

id_scope = "IdScope"
app_id = "AppId"
app_name = "AppName"

token = "SharedAccessSignature Token"

credentials = {"token": token}

central_client = DeviceManager(app_id, credentials)

devices = central_client.get_devices()

text = "Registered Devices:\n"
for device in devices:
    text += f"- {device.id}\n"

token = "BotToken"
chat_id = "ChatId"

url = f"https://api.telegram.org/bot{token}/sendMessage"
data = {"chat_id": chat_id, "text": text}

response = requests.post(url, data=data)