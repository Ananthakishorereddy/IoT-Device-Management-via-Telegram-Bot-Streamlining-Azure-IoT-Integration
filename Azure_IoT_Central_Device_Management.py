from azure.iotcentral.models import Template
from azure.iotcentral.devices import Device, DeviceManager

id_scope = "IdScope"
app_id = "AppId"
app_name = "AppName"

token = "SharedAccessSignature Token"

credentials = {"token": token}

central_client = DeviceManager(app_id, credentials)

devices = central_client.get_devices()

for device in devices:
    print(device.id)