import logging
import azure.functions as func
import json

def main(event: func.EventHubEvent) -> None:
    result = json.dumps({
        'event': event.get_body().decode('utf-8'),
        'message': 'This message was processed by the Azure Function'
    })

    logging.info('Python EventHub trigger processed an event: %s', result)