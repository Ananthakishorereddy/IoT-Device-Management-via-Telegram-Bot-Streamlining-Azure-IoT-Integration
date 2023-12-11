from azure.cosmos import CosmosClient, PartitionKey, exceptions

# replace with your Cosmos DB connection string
CONNECTION_STRING = "<your_cosmos_db_connection_string>"

# initialize the Cosmos DB client
client = CosmosClient.from_connection_string(CONNECTION_STRING)

# replace with your database and container names
DATABASE_NAME = "<your_database_name>"
CONTAINER_NAME = "<your_container_name>"

# get a reference to the container
container = client.get_database_client(DATABASE_NAME).get_container_client(CONTAINER_NAME)

# define the telemetry data payload
def get_telemetry_data():
    return {"device_id": "<your_device_id>", "timestamp": "<your_timestamp>", "temperature": "<your_temperature>"}

# add the telemetry data to Cosmos DB
data = get_telemetry_data()
container.upsert_item(data)