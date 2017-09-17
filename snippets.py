import logging
import argparse

# Set the log output file, and the log level
# logging.basicConfig(filename="snippets.log", level1=logging.DEBUG, level2=logging.INFO)
# logging.basicConfig(filename="snippets.log", dict.level{1: logging.DEBUG, 2:logging.INFO, 3:logging.WARNING, 4:logging.ERROR, 5:logging.CRITICAL})
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)
#logging.basicConfig(filename="snippets.log", level=logging.INFO)

# from bicycle class lesson - reference on how to use .format
# class Bicycle(object):
#     def __init__(self, brand, weight, prodCost):
#         self.brand = brand
#         self.weight = weight
#         self.prodCost = prodCost
        
#     change 
#     def __repr__(self):
#         return "{} {}lbs ${}".format(self.brand, self.weight, self.prodCost)
        
        
#class logging.LoggerAdapter(logger, extra)
        
        
def put(name, snippet):
    """
    Store a snippet with an associated name.

    Returns the name and the snippet
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet
    
    
    
def get(name):
    """Retrieve the snippet with a given name.

    If there is no such snippet, return '404: Snippet Not Found'.

    Returns the snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""


def main():
    """Main fucntion"""
    logging.info("Constructing parser")
    parser = argparse.ArguementParser(description="Store and retrieve snippets of text")
    arguments = parser.parse_args()
    
    if __name__ == "__main__":
        main()
