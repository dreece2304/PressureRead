from pymongo import MongoClient

def get_db(db_name, conn_string='mongodb://10.18.2.7:27017/'):
    """
    Connect to MongoDB and return the database object.

    :param db_name: Name of the database to connect to.
    :param conn_string: MongoDB connection string.
    :return: Database object for the specified database.
    """
    # Establish the connection to MongoDB
    client = MongoClient(conn_string)

    # Select and return the database
    db = client[db_name]
    return db
