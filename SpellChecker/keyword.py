import re
keyword = {
    "colour" : "color", "arbour" : "arbor", "ardour" : "arbor", "armour" : "armor", "behaviour" : "behavior",
    "British" : "American","candour" : "candor" , "clamour" : "clamor", "colour" : "color",
    "demeanour" : "demeanor", "endeavour" :"endeavor","favour" : "favor","flavour": "flavor", "harbour" : "habor",
    "honour" : "honor", "humour" : "humor", "labour" : "labor", "neighbour" : "neighbor", "odour" : "odor", 
    "parlour" : "parlor", "rancour" : "rancor" , "rigour" : "rigor", "rumour" :	"rumor", "saviour" : "savior",
    "savour" : "savor", "splendour" : "splendor", "tumour" : "tumor", "valour" : "valor", "vigour" : "vigor", "dr" : "doctor",
    "mr" : "mister", "ms" : "miss", "mrs" : "misses"
}
lines="Mr. is colour blind who livs in the same neighbour"
lines=lines.lower()
for check,replace in keyword.items():
    print("check:",check,"replace:",replace,"\n")
    lines=re.sub(check,replace,lines)
print(lines)

# with open("dante_inf.txt") as ofile:
#     lines=ofile.read().replace('\n','')
# print(lines)
# for check,replace in keyword.items():
#     print("check:",check,"replace:",replace,"\n")
#     lines=re.sub(check,replace,lines)
# with open('checkregex.txt','w+') as pfile:
#     pfile.write(lines)