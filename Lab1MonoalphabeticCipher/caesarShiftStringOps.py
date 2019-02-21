import string
def caesarShiftStringOps(message, key, encrypt = True):
    """Same as other caesarShift function, but uses string operations since those are implemented
        in C and therefore somewhat faster.  Found on Stack Overflow.
    """
    #message = message.lower().replace(' ', '')
    #alphabet = string.ascii_lowercase
    alphabet = string.printable #'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\\'()*+,-./:;<=>?@[\\]^_`{|}~

    if not encrypt:
        key = -key

    shiftedAlphabet = alphabet[key:] + alphabet[:key]
    return message.translate(str.maketrans(alphabet, shiftedAlphabet))

def test():
    """A small function to test the outputs of the methods in this file.
    """

    plain = input ("Enter the message to be encrypted: ")
    key = input ("Enter the Key: ")
    key = int (key)
    ciphertxt = caesarShiftStringOps (plain, key)
    print (ciphertxt)
    print ("########    The decryption Process  ############")
    print (caesarShiftStringOps (ciphertxt, key, False))



############################################

# Run the test method
while True:
    test()