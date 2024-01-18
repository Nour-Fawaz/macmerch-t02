import sys #lets us know what first argument is


def parseArguments():
    arguments = {
        "price": sys.argv[1],
        "quantity": sys.argv[1],
        "province": "ON"
    }
    
    return arguments