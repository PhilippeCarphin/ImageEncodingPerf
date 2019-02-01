

import numpy as np
import regex as re

def byte_pair_encode_2(message):
    int
    

def byte_pair_encode(message):
    """
    Encode a message using byte-pair encoding

    message (str) : The message to encode

    returns a dictionary containing the encoded message and a list of the substitutions that were made

        {
            "coded_message": message,
            "dict_symb": dict_symb
        }
    """

    LUToctetsdispo = [True] * 256
    dict_symb =[message[0]]
    LUToctetsdispo[ord(message[0])] = False
    nbsymboles = 1
    for i in range(1,len(message)):
        if message[i] not in dict_symb:
            dict_symb += [message[i]]
            LUToctetsdispo[ord(message[i])] = False  #Octet utilisé
            nbsymboles += 1

    longueurOriginale = np.ceil(np.log2(nbsymboles))*len(message)


    dict_symb = []  #Dictionnaire des substitutions
    debut = ord(message[0])  # Origine trouver un code de substitution. Et pour avoir des caractères imprimables...

    remplacementpossible = True
    while remplacementpossible == True:
        #Recherche des paires
        paires = []
        for i in range(0,len(message)-1):
            temppaire = message[i]+message[i+1]
            if not list(filter(lambda x: x[0] == temppaire, paires)): #Si la liste retournée par filter est vide.
                try:
                    if '[' in temppaire:
                        continue
                    result = re.findall(temppaire, message, overlapped = True)
                except Exception as e:
                    print(message)
                    print("temppaire = {}".format(temppaire))
                    print("paires = {}".format(paires))
                    raise e

                paires += [[temppaire,len(result)]]

        #Trouve la paire avec le plus de répétitions.
        paires = sorted(paires, key=lambda x: x[1], reverse = True)

        if paires[0][1] > 1:
            #Remplace la paire
            # print(paires)
            # print("La paire ",paires[0][0], " est la plus fréquente avec ",paires[0][1], "répétitions")
            #Cherche un octet non utilisé
            while debut <256 and LUToctetsdispo[debut] == False:
                debut += 1
            if debut < 256:
                #On substitut
                message = message.replace(paires[0][0], chr(debut))
                LUToctetsdispo[debut] = False
                dict_symb += [[paires[0][0], chr(debut)]]
            else:
                print("Il n'y a plus d'octets disponible!") #Bien sûr, ce n'est pas exact car la recherche commence à message[0]

            # print(message)
            # print(dict_symb)
        else:
            remplacementpossible = False

    # print("Longueur = {0}".format(np.ceil(np.log2(nbsymboles))*len(message)))
    # print("Longueur originale = {0}".format(longueurOriginale))
    # print(dictsymb)
    return {"coded_message": message, "dict_symb": dict_symb}

def byte_pair_decode(coded_message, dict_symb):
    """ Decode a message encoded by byte-pair algorithm """
    for subst in reversed(dict_symb):
        coded_message = coded_message.replace(subst[1], subst[0])

    return coded_message

def test_byte_pair():
    Message = "ABAABAABACABBABCDAADACABABAAABAABBABABAABAAB"
    result = byte_pair_encode(Message)
    decoded_message = byte_pair_decode(result["coded_message"], result["dict_symb"])

    if decoded_message == Message:
        print("TEST PASSED : decoded message is the same as initial message")
    else:
        print("TEST FAILED : decoded message does not match initial message: \n    in : {}\n   out : {}"
              .format(Message, decoded_message))


if __name__ == "__main__":
    test_byte_pair()
