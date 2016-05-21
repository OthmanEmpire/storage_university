### This program uses ROT13 encryption used in the first century ###

import string


def substituteCharacter(uncryp):

    encryp_const = 13

## One possible method to code this function is shown below but requires more lines    
    
##    alphabet = list(string.ascii_lowercase)
##
##    str1 = alphabet[:encryp_const]
##    str2 = alphabet[encryp_const:]
##
##    zipped = zip(str1,str2)
##    encryp = dict(zipped)
##

    char = ord('a')     # Starting character
    d = {chr(char):chr(char+encryp_const) for char in range(char, char + encryp_const)}

    if(uncryp in d):
        cryp = d[uncryp]
        return cryp
    elif(ord(uncryp) < char or ord(uncryp) > (char + 2*len(d))):
        return 'Invalid Input'
    else:
        uncryp = ord(uncryp) - encryp_const
        cryp = chr(uncryp)
        return cryp



def encryptROT13(string):

    cryp = []
    uncryp = list(string)

    for i in range(len(uncryp)):
        cryp.append(substituteCharacter(uncryp[i]))

    cryp_string = ''.join(cryp)
    
    return cryp_string

uncryp = input("WeLcOmE tO cRyPtIc VeRsIoN x.Y.z! PlEaSe InPuT sTrInG: ")
cryp = encryptROT13(uncryp)
print("An uncryptic \'{}\' generates a cryptic \'{}\'".format(uncryp, cryp))

decryp = encryptROT13(cryp)
print("A cryptic \'{}\'  a cryptic \'{}\'".format(cryp, decryp))

