#NOTE:Update Input text file location in line 103. This file will be used to create the dictionary.[No change necessary:If present in the same directory & if file named as dante_inf.txt]
#NOTE:The program takes longer if the word that it is searching for is further towards the end of the alphabet list. To get results quicker, 
# suggest using words starting with the alphabet in the first half of the alaphabet. 
#Importing regex and string package
import re
import string

def process_regex(fpath):
    
    #Word list to perform substitution. Found this list which has all the words that are different in american english and british english.
    keyword = {
        "colour" : "color", "arbour" : "arbor", "ardour" : "arbor", "armour" : "armor", "behaviour" : "behavior",
        "British" : "American","candour" : "candor" , "clamour" : "clamor", "colour" : "color",
        "demeanour" : "demeanor", "endeavour" :"endeavor","favour" : "favor","flavour": "flavor", "harbour" : "habor",
        "honour" : "honor", "humour" : "humor", "labour" : "labor", "neighbour" : "neighbor", "odour" : "odor", 
        "parlour" : "parlor", "rancour" : "rancor" , "rigour" : "rigor", "rumour" :	"rumor", "saviour" : "savior",
        "savour" : "savor", "splendour" : "splendor", "tumour" : "tumor", "valour" : "valor", "vigour" : "vigor", "dr." : "doctor",
        "mrs." : "misses","mr." : "mister", "ms." : "miss"
    }
    #Replacing all the words from british to american english.
    #Replacing all the necessary words with relavent substitutions.
    #Each word is checked if its present in the keyword dictionary, if yes, the word is replaced with its mentioned replacement.
    with open(fpath,'r') as file:
        lines=file.read().replace('\n','')
        lines=lines.lower()
    for check,replace in keyword.items():
        #if word is present in the keyword list, the word is replaced with the associated word with it in the keyword list.
        lines=re.sub(check,replace,lines)
    #Rewriting output in a new file after we have substituted the desired words.
    with open('regex.txt','w+') as newfile:
        newfile.write(lines)

    print("done with regex")
           

def normalize_text(dpath):
    print("Starting Dictionary")
    text_file = open(dpath,'r')
    text = text_file.read()
    
    #Lowering the case of the words.
    text = text.lower()

    #spliting each word in a string.
    words = text.split()

    #Stripping off all the special characters.
    words = [word.strip('.,!?;()[]') for word in words]

    #Removing Punctuations
    words = [word.translate(str.maketrans('','', string.punctuation)) for word in words]

    #Removing " 's " from all the words if any
    ords = [word.replace("'s",'') for word in words]

    #removing Repeated words from the list and saving them in a dictionary file. 
    #initialize empty list.
    unique = []

    #if word in not already present in the list append it to the list.
    for word in words:
        if word not in unique:
            unique.append(word)
    unique.sort()
    #The list is sorted in ascending order.

    # print("Done sorting unique\n")
    o = open("dictionary.txt","w")
    for items in unique:
        #Removing Non words from the list of unique tokens such as red[221] etc. Using regular expression to screen through the words and accepting only right word.
        if re.match("^[A-Za-z]*$", items):
            o.write(items)
            o.write("\n")
        #All the words are saved in single lines of the dictionary file.
    print("Done writing dictionary.")



def levenshteinDist(s, t):
    #implementing levenshteindistance ALgorithm. 
    #if the string 's' is empty, the minimum distance is gonna be returned as length(t).
    if s == "":
        return len(t)
        
    #Similaryly, if the string 't' is empty, the minimum distance is gonna be returned as length(s).
    if t == "":
        return len(s)
    # Defining cost variable. If the characters are same then its 0 else 2.
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 2
    
    #This is the recurrsive function to return the minimum distance. It returns the minimum value of the three recurrsive function defined below.
    res = min([levenshteinDist(s[:-1], t)+1,
               levenshteinDist(s, t[:-1])+1, 
               levenshteinDist(s[:-1], t[:-1]) + cost])
    #Returns the minimum distance for the two words passed to this function.
    return res


if __name__ == '__main__':
    
    #NOTE:CHANGE THE LOCATION OF FILE "HERE" IF NEEDED. 
    #Calling process_regex function to do text Regex. Passing location of the input text file to convert to Dicitionary. 
    process_regex("dante_inf.txt")

    #Calling normalize_text function to do the rest of normalizing steps. 
    normalize_text("regex.txt")

    #Starting application for the user to check the string for spellchecking
    print("----------------------------------------\n Welcome to the spell checker!\n Please enter a text to check spelling or enter quit to exit the program.\n----------------------------------------")
    while True:
        #Menu driven, if quit is typed the application quits.
        ch=(input("Enter string to be checked:\n"))
        ch=ch.lower()
        if (ch=="quit"):
            print("exiting application")
            exit()
        else:
            #This part gets excecuted if the user enters a sentence expect for the word "quit".
            #Dictionary file is opened and read into lines.
            o = open("dictionary.txt","r")
            lines = o.readlines()
            #initializing list variable 'line', which will hold all the words from the list for checking.
            line=[]
            for r in lines:
                l=r.rstrip("\n")
                #removing "\n" from each word. the dictionary has \n as the dictionary file needed to 
                # have words in separate line.
                line.append(l)
            ch=ch.lower()
            s=[]
            #The sentence is split into words and saved in the list 's'.
            s=ch.split()
            #start checking for mistakes
            #suggested_word is the dictionary which will hold wrong_word:suggested_word pair to show the 
            # user the mistaken word and the suggested correct word.
            suggested_word={}
            for word in s:
                #checking each word in the stentence one after another.
                td=0
                if word in line:
                    #if the word is present in the dictionary(this is saved in 'line' variable)
                    #if found nothing is to be done.
                    continue
                else:   
                    #if the word is not found. This else part will run. 
                    print("checking....")
                    for row in line:
                        #Levenshtein Algorithm is called passing the word that's being checked with 
                        # each word that is present in the dictionary. 
                        td=levenshteinDist(word,row)
                        #We are setting the distance tolerance as 2 to ensure the word suggested is not 
                        #very far off from the correct word. This tolerance can be changed to get different 
                        #accuracy in results.
                        if(td<=2):
                            #the suggested word is then added to the dictionary to be shown once the whole 
                            #sentence is checked for spelling.
                            suggested_word[word]=row
                            # print("Suggested word in loop:",row)
                            break
            #If no changes are necessary, i.e., all the words are right then the else part will get triggered.
            if(len(suggested_word)!=0):
                #We are checking if changes are needed by checking the dictionary length is not 0.
                print("Suggested word correction[wrong_word:suggested_correction]:",suggested_word)
            else:
                print("No changes necessary")
                