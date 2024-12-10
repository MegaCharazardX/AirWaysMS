import string
import random
#import Loading

#print(string.ascii_letters)

chars = " "  + string.digits + string.ascii_letters
chars = list(chars)
key = ['d', 'H', 'v', 'b', 'r', '7', 'T', 'S', 'M', 'E', 'W', 'A', 'K', 'e', 'i', 'C', 'G', 'w', ' ', 'P', 'y', 'x', 'R', 'q', 'U', 'B', 'g', 'O', 'k', 'N', '0', 't', 'u', 'X', 'L', '4', '8', 'n', 'Q', 'J', 'h', 'o', 'V', '5', 'I', 'l', 's', '9', 'z', 'f', 'Z', 'F', 'c', '1', 'p', 'j', 'Y', 'D', 'm', '3', '6', '2', 'a']
# for i in string.punctuation :
#     if i in key :
#         key.remove(i)
#     #if
# print(key)
# random.shuffle(key)
# print(key)
class crypt :
    #ENCRYPT
    def __init__(self, _text):
        self.text = _text

    def encrypt(self):
        #plain_text = input("Enter a message to encrypt: ")
        cipher_text = ""

        for letter in self.text:
            if letter in string.punctuation :
                cipher_text += letter
            else :
                index = chars.index(letter)
                cipher_text += key[index]

        return cipher_text

    #DECRYPT
    def decrypt(self):
        #cipher_text = input("Enter a message to decrypt: ")
        plain_text = ""

        if type(self.text) == list or type(self.text) == tuple :
           
            for word in self.text:                
                for letter in word:
                    if letter in string.punctuation :
                        plain_text += letter
                    else :
                        index = key.index(letter)
                        plain_text += chars[index]
                plain_text+=" "
            return plain_text

        else :
        
            for letter in self.text:
                if letter in string.punctuation :
                    plain_text += letter
                else :
                    index = key.index(letter)
                    plain_text += chars[index]

            return plain_text

# Loading.loading(text = "Encrypting.. ")
#print(crypt("Charazard101").encrypt())