jokes_new = """Was ist 200 km/h schnell und rollt über die Autobahn? – Deine Mutter mit McDonalds-Gutscheinen.
Was antwortet deine Mutter, wenn sie gefragt wird, was die Hälfte von sechs ist? – Halb sechs.
Warum freut sich deine Mutter über ein Puzzle, das sie in 4 Monaten fertig bekommen hat? – Weil auf der Packung steht 3-4 Jahre.
Was ist der Unterschied zwischen Milch und deiner Mutter? – Die Milch gibt es auch in fettarm.
Warum behauptet deine Mutter, sie wäre Veganerin? – Damit sie wenigstens irgendwo dazugehört.
Wie schreckt deine Mutter ihre Eier ab? – Mit ihrem Gesicht.
Warum fällt der Baum um, wenn deine Mutter daran lehnt? – Der Klügere gibt nach.
Wie bringt man Gott zum Weinen? – Zeig ihm deine Mutter.
Warum wirft deine Mutter Brot ins Klo? – Sie will die WC-Ente füttern.
Womit verdient deine Mutter heimlich ihr Geld? – Sie arbeitet als Hüpfburg auf Kindergeburtstagen.

"""

import re
import json

with open("jokes.json", encoding="utf8") as jsonFile:
    jokes = json.load(jsonFile)
    jokes = jokes
    jsonFile.close()

x = re.findall(r"(?=Deine)(.*)(?=)", jokes_new)

for i in x:
    if i not in jokes:
        #i = i + "."
        jokes.append(i)

jsonFile = open("jokes.json", "w+", encoding="utf-8")
jsonFile.write(json.dumps(jokes))
jsonFile.close()
