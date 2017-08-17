import logging

# Set the log output file, and the log level
loging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name, snippet):
    """
    Store a snippet with an associated name. 
    Returns the name and the snippet
    """
    
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet
    
def get(name):
    """Retreive the snippet with a given name. 
    If there is no such snippet, return '404: Snippet Not Found'.
    Returns the snippet
    """
    
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""