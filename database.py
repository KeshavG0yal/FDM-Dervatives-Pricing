from pymongo import MongoClient

def connect_db():
    connection_string = "mongodb+srv://keshavg1:k5IzbEwTBEMGzMtO@derivativecluster.rvksi.mongodb.net/derivatives?retryWrites=true&w=majority"
    client = MongoClient(connection_string)
    db = client['derivatives']
    collection = db['option_pricing']
    return collection

def save_option_price(collection, method, option_price, details):
    collection.insert_one({
        'method': method,
        'option_price': option_price,
        'details': details
    })
    
def get_option_prices(collection):
    return list(collection.find({}))
