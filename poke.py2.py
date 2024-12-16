""" import json

# Open and load the JSON file
with open('./PokeTCG.json', 'r',  encoding='utf-8-sig') as file:
    data = json.load(file)
returninglist = []
# Print the loaded data (optional)
#print the name of all fighting type pokemon
for fightingpk in data['data']:
 #   while ['types']:
if ["Fighting"]["types"] in ["types"]:  #  if ["types"] == ["Fighting"]:
        returninglist.append(fightingpk["id"]["name"]["supertype"]["subtypes"]["level"]["hp"])
        print ["id"],["name"],["supertype"],["subtypes"],["level"],["hp"]
        print(returninglist)
#print all cards from the set "HeartGold & SoulSilver"

#print all cards where the averageSellPrice is greater than 1.5
#                                  data['data'] """
print("g")