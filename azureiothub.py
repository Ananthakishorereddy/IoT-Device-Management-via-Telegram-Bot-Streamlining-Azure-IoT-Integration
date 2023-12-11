from azure.iot.device import IoTHubDeviceClient, Message
import random

# replace with your device connection string
CONNECTION_STRING = "<your_device_connection_string>"

# initialize the client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

# define the message payload
def get_message_payload():
    return {"temperature": random.randint(20, 30)}

# send a message to IoT Hub every second
while True:
    payload = get_message_payload()
    message = Message(json.dumps(payload))
    client.send_message(message)
    print("Sent message: {}".format(message))
    time.sleep(1)