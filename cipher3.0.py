import sys
import collections
from random import randint
import string
print("----------------------------------------------------------------------------------------------------------------------------------------------\nThe parameters must be entered in the following format: \n --encrypt/--decrypt "
      "[rotation]e.g. 10 --file(if inputing a file) [filename] e.g. plaintext1.txt  \n if you would like to enter your own message to encrypt enter --encrypt/--decrypt as the first argument then your rotation number as the sencond argument\nif you want to auto decrypt the second parameter must be --auto \n-----------------------------------------------------------------------------------------------------------------------------------------------")

Alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']


def get_message():
    msg = []
    print("Enter a message:")
    # user can input multiple lines and so output can treat each line as a separate message
    # A while loop which ends when the user double taps enter
    while True:
        Line = input()
        if Line:
            msg.append(Line + "\n")
        elif Line == "":
            break
    #print(msg)
    return msg

def encrypt_ceasar(msg):

    ShiftNum = rot
    Text = " "
    msg = [x.upper() for x in msg]
#converts every item in list to uppercase

#  Finds which index the letter from message is in relation to the alphabet
# It then shifts by the given rotation and uses mod 26 so the the character can loop back round in the alphabet
# Uses the index found previously and rotates it about alpha by the rotation provided
# Converts the index back into a letter from alpha to give encrypted word
# from message
    for word in msg:
        for ch in word:
            if ch in Alpha:
                index = Alpha.index(ch)
                eIndex = (index + ShiftNum) % 26
                ShiftedMsg = Alpha[eIndex]
                Text += ShiftedMsg
                #print(Text)

            else:
                Text = Text + ch

    return Text
    
def decrypt_caesar(msg): #does the exact same as the encrypt_ceasar function but decrypts instead
    ShiftNum = rot
    msg = [x.upper() for x in msg]
    DecryptedText =  " "
    for item in msg:
        for ch in item:
            if ch in Alpha:
                index = Alpha.index(ch)
                dIndex = (index - ShiftNum) % 26 #decryption done by minusing shift num to index of letter in Alphabet
                                                 # instead of adding
                ShifteddMsg = Alpha[dIndex]
                DecryptedText += ShifteddMsg
            else:
                DecryptedText = DecryptedText + ch
                
    return DecryptedText

def get_file():
    MyFile = open(str(sys.argv[4]), "r").read()  #reads the file entered as one of the parameters
    print("The message from the file you want to encrypt/decrypt is: \n \n" + MyFile) #prints the contents of file
    with open(str(sys.argv[4]), "a") as MyFile:
        MyFile.write("\n")
    AdditionalText = input("Would you like to add any more lines of text to your file? (yes/no): ")

    #!# here i give the user the option to add additional lines of text to their file before encryption/decryption

    if AdditionalText == "yes":
        print("Please enter the text you would like to add: ")
        while True:
            AddText = input()
            if AddText:
                with open(str(sys.argv[4]), "a") as MyFile:
                    MyFile.write(AddText + "\n")


            elif AddText == "":
                break
    else:
        print("The will be no additional text added to your file")
    MyFile = open(str(sys.argv[4]), "r").read()
    print("Your file now contains:\n" + MyFile)

    msg = MyFile

    return msg

def analysis(AnaText):
    print("--------------------------------------------------------------------------------------------------------------\nAnalysis")
    EmptyList = []
    if sys.argv[1] == "--encrypt" and len(sys.argv) == 3:
        AnaText = " ".join(AnaText) #joins list into one string with spaces between
    AnaText = AnaText.replace("\n", " ") #replaces new line with a space
    AnaText = AnaText.split(" ")
    for word in AnaText:
        word = word.upper()
        EmptyList.append(word)
    EmptyList = [''.join(c for c in s if c not in string.punctuation) for s in EmptyList] #removes punctuation from items in list
    EmptyList = [s for s in EmptyList if s] #removes any empty string in list
    print("\nThe Total number of words in the message/file is: " + str(len(EmptyList)))
    UniqueSet = set(EmptyList) #convets list into a set to remove any duplicates in lists
    print("There are " + str(len(UniqueSet)) + " Unique words")
    LongestWord = len(max(EmptyList, key=len)) #finds the longest word in a list
    print("The longest word has " + str(LongestWord) + " letters" + " this word is: " + max(EmptyList, key=len))
    Shortestword = len(min(EmptyList, key=len)) #finds the shortest word in the list
    print("The shortest word has " + str(Shortestword) + " letter(s) this word is: " + min(EmptyList, key=len))
    JoinedWrds = ''.join(EmptyList) #joins all the words into one sting without spaces
    #JoinedWrdsWithSpaces = ' '.join(EmptyList)
    MostCommonCh = collections.Counter(JoinedWrds).most_common(1) #counts and finds the most common letter and how many times it is used
    print("The Most common letter is " + str(MostCommonCh))
    MostCommonWord = collections.Counter(EmptyList).most_common(10) #finds the most common 10 words in order and the amount of apperances they make in the text
    print("The most common words are: " + str(MostCommonWord))
    AverageWordLen = sum(len(word) for word in EmptyList) / len(EmptyList) #sum of the length of every character in the list divided by the number of words
    print("The Average word length is : " + str(AverageWordLen))


if sys.argv[1] == "--encrypt" and len(sys.argv) == 3:
    rot = sys.argv[2]
    #!# added feature which allows the user to select a random rotation value on the encryption
    Random = input("Would you like a random rotation on your encrypted message? (yes/no): ")
    if Random == "yes":
        rot = randint(0,100)
    elif Random == "no":
        try: #Basically runs the code to get the rotation and ensures it is an interger
            rot = int(rot)

        except ValueError: #Makes an exception if there is an error in the parameter provided
            print("the index shift parameter must be an interger, please restart programme")
            quit()
    else:
        print("restart programme and enter yes or no correctly")
        quit()

    def main():
        msg = get_message()
        #print(msg)
        Text = encrypt_ceasar(msg)
        print("Your encrypted message is: \n" + Text)
        AnaText = msg
        analysis(AnaText)

    main()


elif sys.argv[1] == "--decrypt" and len(sys.argv) == 3 and sys.argv[2] != "--auto":

    rot = sys.argv[2]
    try:
        rot = int(rot)

    except ValueError:
        print("the index shift must be an interger, please restart programme")

    def main():
        msg = get_message()
        DecryptedText = decrypt_caesar(msg)
        print("Your Decrypted message is: \n" + DecryptedText)
        AnaText = DecryptedText
        analysis(AnaText)
        
    main()
if sys.argv[1] == "--encrypt" and len(sys.argv) == 5 and sys.argv[3] == "--file":

    rot = sys.argv[2]
    try:
        rot = int(rot)

    except ValueError:
        print("the index shift must be an interger, please restart programme")

    def main():
        msg = get_file()
        Text = encrypt_ceasar(msg)
        print("Your encrypted message is: \n \n" + Text)
        AnaText = msg
        analysis(AnaText)
    main()

if sys.argv[1] == "--decrypt" and len(sys.argv) == 5 and sys.argv[3] == "--file":

    rot = sys.argv[2]
    try:
        rot = int(rot)

    except ValueError:
        print("the index shift parameter must be an interger, please restart programme")
        quit()


    def main():
        msg = get_file()
        DecryptedText = decrypt_caesar(msg)
        print("\nYour decrypted file is: \n\n" + DecryptedText)
        AnaText = DecryptedText
        analysis(AnaText)
    main()

if sys.argv[1] == "--decrypt" and sys.argv[2] == "--auto":

    EngDict = open("english-dictionary-500.txt", "r").read()

    def rotation(rot):
        msg = open("ciphertext1-13.txt", "r").read()
        msg = [x.upper() for x in msg]
        dText = " "
        for item in msg:
            for ch in item:
                if ch in Alpha:
                    index = Alpha.index(ch)
                    dIndex = (index - rot) % 26
                    ShifteddMsg = Alpha[dIndex]
                    dText += ShifteddMsg
                else:
                    dText = dText + ch #dText contains the same message with 26 different rotations
        #print(dText)
        SplitText = dText.split(" ")
        NoLineText = dText.replace("\n", " ")
        ListDText = NoLineText.split(" ")
        for Item in ListDText:
            for Ch in Item:
                if Ch in Alpha:
                    continue
                else:
                    pass
        ListDText = set(ListDText)
        #print(ListDText)
        BigEngDict = EngDict.upper()
        EngDictList = BigEngDict.replace("\n"," ")
        EngDictList = EngDictList.split()
        #print(EngDictList)
        for Item in ListDText:
            Elem = Item
            if Elem in ListDText and Elem in EngDictList:
                if len(Elem) > 5: #!# this searches for possible decryptions that have more than two matches in the english dictionary
                    print(dText)
                    Correct_Message = input("Is this your encrypted message? (input 'yes' or 'no') ")
                    if Correct_Message == "yes":
                        print("\n----------------------------------------\nYipeeee! have fun reading your decrypted message :) ")
                        AnaText = dText
                        analysis(AnaText)
                        quit()
        return dText

    for rot in range(26): #this is the line that trys 1-26 rotations on the encrypted message
        rotation(rot)

elif sys.argv[1] != "--encrypt" and sys.argv[1] != "--decrypt":
    print("Please enter the correct parameters in the following format: \n --encrypt/--decrypt [rotation]e.g. 10 --file(if inputing a file) [filename] e.g. plaintext1.txt\n if you want to auto decrypt the second parameter must be --auto")