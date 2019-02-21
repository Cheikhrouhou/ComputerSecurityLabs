# caesarShift is the additive cipher view in lectures
#
import string

def caesarShift(message, key, encrypt = True):
    """Perform a Caesar Shift on a given message to either encrypt or decrypt the message.

    Args:
        message: The message to be encoded.
        key: The integer amount to shift the message by.  Assumed to be the encryption key.
        encrypt: Whether to encrypt the message or decrypt it. (default: True)

    Returns:
        The resulting message.
    """
    #message = message.lower().replace(' ', '')
    alphabet = string.printable
    newMessage = ""

    #Change shift direction depending on encrypting or decrypting
    if not encrypt:
        key = -key

    #Loop through the message
    for char in message:
        index = alphabet.find(char)
        newMessage += alphabet[(index + key) % len(alphabet)]

    return newMessage

def test():
    """A small function to test the outputs of the methods in this file.
    """

    plain = input ("Enter the message to be encrypted: ")
    key = input ("Enter the Key: ")
    key = int (key)
    ciphertxt = caesarShift (plain, key)
    print (ciphertxt)
    print ("########    The decryption Process  ############")
    print (caesarShift (ciphertxt, key, False))

    # print ("########    Other Methods  ############")
    # print ("Cipher Text :", caesarShiftStringOps (plain, key))
    # print ("Plain  Text :", caesarShiftStringOps (ciphertxt, key, False))

############################################

# Run the test method
while True:
    test()

