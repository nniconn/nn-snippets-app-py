import logging
import argparse
import psycopg2

# Set the log output file, and the log level
# logging.basicConfig(filename="snippets.log", level1=logging.DEBUG, level2=logging.INFO)
# logging.basicConfig(filename="snippets.log", dict.level{1: logging.DEBUG, 2:logging.INFO, 3:logging.WARNING, 4:logging.ERROR, 5:logging.CRITICAL})
logging.basicConfig(format='%(asctime)s %(message)s', filename="snippets.log", level=logging.DEBUG)
logging.debug('Debug message for the log file')
logging.info('Info message for the log file')
logging.warning('Warning message for the log file')


logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("Database connection established.")



# from bicycle class lesson - reference on how to use .format
# class Bicycle(object):
#     def __init__(self, brand, weight, prodCost):
#         self.brand = brand
#         self.weight = weight
#         self.prodCost = prodCost
        
#     change 
#     def __repr__(self):
#         return "{} {}lbs ${}".format(self.brand, self.weight, self.prodCost)

# connect to database ( psycopg2 )

def put(name, snippet):
    """Store a snippet with an associated name."""
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet

def get(name):
    """Retrieve the snippet with a given name.
    If there is no such snippet, return '404: Snippet Not Found'.
    Returns the snippet.
    """

    #retrieve the snippet from the db
    
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    print("this function is running",get.__name__)
    return ""
    

def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # put | get | anycommand | some take more arguments | --flags
    put_parser = subparsers.add_parser('put', help="name message")
    put_parser.add_argument('name', help="Name of snippet")
    put_parser.add_argument('snippet', help="Snippet text")

    get_parser = subparsers.add_parser('get', help="name to retrieve")
    get_parser.add_argument('name', help="Name to be retreived from the database")
    
    # Subparser for the put command
    logging.debug("Constructing put subparser")
    #put(name, snippet)    put_parser = subparsers.add_parser("put", help="Store a snippet")
    #put_parser.add_argument("name", help="Name of the snippet")
    #put_parser.add_argument("snippet", help="Snippet text")
    
    
    arguments = parser.parse_args()
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))
        
if __name__ == "__main__":
    main()
    