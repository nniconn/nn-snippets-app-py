import logging
import argparse
import psycopg2

logging.basicConfig(format='%(asctime)s %(message)s', filename="snippets.log", level=logging.DEBUG)
logging.debug('Debug message for the log file')
logging.info('Info message for the log file')
logging.warning('Warning message for the log file')


logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("Database connection established.")




# connect to database ( psycopg2 )

def put(name, snippet):
    """Store a snippet with an associated name."""
    # commenting the 3 lines below in order to try and refactor the put method to use context managers
    # logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    # cursor = connection.cursor()
    # command = "insert into snippets values (%s, %s)"
    with connection, connection.cursor() as cursor:
        cursor.execute("store snippets where values=%s", (snippet,))

    
    try:
        command = "insert into snippets values (%s, %s)"
        cursor.execute(command, (name, snippet))
    except psycopg2.IntegrityError as e:
        connection.rollback()
        command = "update snippets set message=% where keyword=%s"
        cursor.execute(command, (snippet, name))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet


def catalog(name):
    ''' To query keywords from snippets table'''
    #cursor.fetchall() use this 
    #select * from table order by age (find rows with value stored in age column)
    with connection, connection.cursor() as cursor:
        cursor.execute("select all keyword=%s", (name,))
        row = cursor.fetchall()
    if not row:
        #No snippet was found with that name.
        return "404: Snippet not Found"
    return row[0]

def search():
    ''' To list snippets which contain a given string snywhere in their messages'''
    #using like operator - select * from table where prescription like '%cobwell%'
    

def get(name):
    """Retrieve the snippet with a given name.
    If there is no such snippet, return '404: Snippet Not Found'.
    Returns the snippet.
    """
    #retrieve the snippet from the db - commnet from session of nicole darcy
    #i added the 'cursor= ' line because it said it was unused code, copied it from def put()
# commenting lines below to replace with new code as per class lesson
    # cursor=connection.cursor()
    # row = cursor.fetchone()
    # connection.commit()
    with connection, connection.cursor() as cursor:
        cursor.execute("select message from snippets where keyword=%s", (name,))
        row = cursor.fetchone()
    if not row:
        #No snippet was found with that name.
        return "404: Snippet not Found"
    return row[0]
    
    # warning for 'unreachable code' so i commented it out...
    # logging.error("FIXME: Unimplemented - get({!r})".format(name))
    # print("this function is running",get.__name__)
    # return ""
    

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
    #test this
    put_parser.add_argument('Nicole', help="Lives in Brooklyn")
    put_parser.add_argument('Esther', help="Lives in Queens")
    put_parser.add_argument('Chandi', help="Lives in NJ")
 
    
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
    