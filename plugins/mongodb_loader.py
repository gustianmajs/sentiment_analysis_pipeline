import pymongo


def get_mongo_client(mongo_uri):
    """Establish connection to the MongoDB."""
    try:
        client = pymongo.MongoClient(mongo_uri)
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return client
        except Exception as e:
            print(e)
            return None
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None


def get(database, collection):
    mongo_uri = "<connection>"
    mongo_client = get_mongo_client(mongo_uri)
    if not mongo_client:
        print("Failed to create MongoDB client")
        return None

    # Ingest data into MongoDB
    db = mongo_client[database]
    col = db[collection]

    return db
