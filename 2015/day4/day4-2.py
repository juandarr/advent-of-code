from os.path import dirname, abspath
import sys
import hashlib

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def get_md5_hash(text):
    """
    Calculates the MD5 hash of a given string.

    Args:
        text (str): The input string to be hashed.

    Returns:
        str: The MD5 hash as a hexadecimal string.
    """
    # Encode the string to bytes (e.g., using UTF-8 encoding)
    encoded_text = text.encode('utf-8')

    # Create an MD5 hash object
    md5_hash_object = hashlib.md5()

    # Update the hash object with the encoded text
    md5_hash_object.update(encoded_text)

    # Get the hexadecimal representation of the hash
    md5_hex_digest = md5_hash_object.hexdigest()

    return md5_hex_digest

def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    secret = data.rstrip()
    return secret


def getCode(secret):
    for i in range(1,10*(10**6)):
        val = secret+str(i)
        hex = get_md5_hash(val)
        if hex[0:6]=='000000':
            return i
    return 0

def main(filename):
    secret = parseInformation(filename)
    code = getCode(secret)
    return code

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 4, [6742839,5714438], main)
    else:
        code = getAnswer(2015, 4, main)
        print("The code is is {0}".format(code))

