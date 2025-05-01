from catalog import getFullCatalog
import json

data = getFullCatalog()
print(data)

with open("fullcatalog.json", "w") as file:
    json.dump(data, file, indent=2)
