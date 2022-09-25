#Importing regex and string package
import re
import string

def process_regex(fpath):
    #Word list to substitute
    keyword = {
        "colour" : "color", "arbour" : "arbor", "ardour" : "arbor", "armour" : "armor", "behaviour" : "behavior",
        "British" : "American","candour" : "candor" , "clamour" : "clamor", "colour" : "color",
        "demeanour" : "demeanor", "endeavour" :"endeavor","favour" : "favor","flavour": "flavor", "harbour" : "habor",
        "honour" : "honor", "humour" : "humor", "labour" : "labor", "neighbour" : "neighbor", "odour" : "odor", 
        "parlour" : "parlor", "rancour" : "rancor" , "rigour" : "rigor", "rumour" :	"rumor", "saviour" : "savior",
        "savour" : "savor", "splendour" : "splendor", "tumour" : "tumor", "valour" : "valor", "vigour" : "vigor", "dr" : "doctor",
        "mrs" : "misses","mr" : "mister", "ms" : "miss" 
    }
    # checkword=('colour','arbour','ardour','armour','behaviour','British','candour','clamour','demeanour','endeavour','favour','flavour','harbour','honour','humour','labour','neighbour','odour','parlour','rancour','rigour','rumour','saviour','savour','splendour','tumour','valour','vigour','dr','mr','ms','mrs')
    # replacement=('color', 'arbor', 'arbor', 'armor', 'behavior', 'American', 'candor', 'clamor', 'demeanor', 'endeavor', 'favor',
    # 'flavor', 'habor', 'honor', 'humor', 'labor', 'neighbor', 'odor', 'parlor', 'rancor', 'rigor', 'rumor', 'savior', 'savor', 
    # 'splendor', 'tumor', 'valor', 'vigor', 'doctor', 'mister', 'miss', 'misses')

    #Replacing all the words from british to american english
    #Replacing all the necessary words with relavent substitutions

    # with open(fpath, 'r') as file, open('regex.txt','w+') as newfile:
    #     for line in file:
    #         for check,replace in zip(checkword,replacement):
    #             temp=re.sub(check,replace,line)
    #         newfile.write(temp)
    with open(fpath,'r') as file:
        lines=file.read().replace('\n','')
        lines=lines.lower()
    for check,replace in keyword.items():
        lines=re.sub(check,replace,lines)
    with open('regex.txt','w+') as newfile:
        newfile.write(lines)

    


def normalize_text(dpath):
    text_file = open(dpath,'r')
    text = text_file.read()
    #Lowering the case of the words
    text = text.lower()
    words = text.split()
    #Stripping off all the special characters 
    words = [word.strip('.,!?;()[]') for word in words]

    #Removing Punctuations
    words = [word.translate(str.maketrans('','', string.punctuation)) for word in words]
    #Removing 's from all the words if any
    words = [word.replace("'s",'') for word in words]

    #removing Repeated words from the list
    unique = []
    for word in words:
        if word not in unique:
            unique.append(word)
    unique.sort()

    print("Done sorting unique\n")
    o = open("dictionary.txt","w")
    for items in unique:
        #Removing Non words from the list of unique tokens.
        if re.match("^[A-Za-z]*$", items):
            o.write(items)
            o.write("\n")
    print("Done writing dictionary.")



if __name__ == '__main__':
    process_regex("dante_inf.txt")
    normalize_text("regex.txt")
    # o = open("dictionary.txt","r")
    # p=[]
    # line = o.readlines()
    # for r in line:
    #     l=r.rstrip("\n")
    #     p.append(l)
    # print(p)