from os import listdir
from os.path import isfile, join
import json

path_custom = "CustomBattlers"
path_json = "json"
fusions = []

for element in listdir(path_custom):
    if isfile(join(path_custom, element)) and element.endswith(".png"):
        fusions.append(element[:-4])
        print(element[:-4])

jsonStr = json.dumps(fusions, separators=(',\n', ': '))
jsonFile = open(path_json + "/" +"aegide_sprites.json", "w")
jsonFile.write(jsonStr)
jsonFile.close()

print("DONE : ", len(fusions))

# ^(?!("[0-9]+\.[0-9]+"))
# "[0-9]+\.[0-9]+"