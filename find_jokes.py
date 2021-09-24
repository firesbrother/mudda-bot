jokes_new = """ Deine Mutter ist so dumm. Sie sitzt hinterm Fernseher und sucht Kabel 1.

215      Fernseher Witze


Deine Mutter kratzt an Bäumen nach Hartz 4.

229      Baum Witze


Deine Mutter war schon als kleiner Junge hässlich.

188      hässlich Witze


Deine Mutter liebt Kalorien. Sie gibt ihnen ein Zuhause.     ~ Kevin

144      Kalorien Witze


Deine Mutter sitzt im Getränkeautomaten und säuft die Reste.

Deine Mutter lässt sich für 1 € auf dem Jahrmarkt in die Eier treten.

182      Jahrmarkt Witze


Wenn deine Mutter Zwiebeln schneidet, dann weinen die Zwiebeln.     ~ Roberto

154      Zwiebel Witze


Deine Mutter arbeitet auf einem Fischkutter - als Geruch.     ~ David B. S.

140      Mütterwitze


Deine Mutter dreht die Würfel bei Tetris.

158      Tetris Witze


Deine Mutter ist so hässlich. Bei Ihr wird eingebrochen um die Vorhänge zuzumachen.     ~ rofl

279      Mütterwitze

Deine Mutter mag dich nur wegen des Kindergeldes.

174      Kindergeld Witze


Deine Mutter wird öfter geknallt als die Tür vom Arbeitsamt.

161      Türwitze


Deine Mutter ist so haarig. Die einzige Sprache, die sie spricht, ist Wookie.

129      Mütterwitze


Deine Mutter ist so hässlich. Wenn sie strippt bekommt sie Geld dafür, dass sie sich wieder anzieht!     ~ jolo

167      hässlich Witze


Deine Mutter zieht Katapulte nach Gondor.

Deine Mutter nimmt kein Gramm ab und wird trotzdem THE BIGGEST LOSER.

151      Mütterwitze


Deine Mutter isst Erdnüsse, kackt auf den Boden und freut sich über ein Snickers.     ~ *MrGenius*

278      Snickers Witze


Respekt. Deine Mutter kann Geschlechtskrankheiten von Hunden und Katzen am Geschmack erkennen.

142      Mütterwitze


Deine Mutter steht vor KiK und schreit: "Ich bin billiger."

231      Mütterwitze


Deine Mutter klaut Gratissocken bei Deichmann!     ~ vivi03

Deine Mutter arbeitet bei der Marine - als Flugzeugträger.

146      Mütterwitze


Deine Mutter bindet sich eine Lkw-Felge auf den Rücken und denkt sie wäre Optimus Prime.     ~ mutter

197      Mütterwitze


Was ist der Unterschied zwischen einem Eichhörnchen und deiner Mutter?

Deine Mutter hatte schon mehr Eicheln im Mund!     ~ Nutty

118      Eichel Witze


Deine Mutter spielt die Kugel in Indiana Jones!     ~ Broken Byte

135      Mütterwitze


Deine Mutter ist so fett. Wenn sie einen gelben Regenmantel anzieht und einen Berg hinaufgeht, denken alle die Sonne geht auf!

Seit deine Mutter eine Burka trägt, ist sie sehr viel schöner.     ~ Burkhardt

99      Burka Witze


Deine Mutter hat in einem Porno mitgespielt: Bums den Wal zurück ins Meer!

97      Wal Witze


Deine Mutter ist so fett. Sie wird nicht von der Erde angezogen, sondern die Erde wird von ihr angezogen.     ~ connidaspony

106      fett Witze


Deine Mutter ist so fett. Ihr Gürtel heißt Äquator.

166      Äquator Witze


Deine Mutter kippt beim Joghurt mit der Ecke die große in die kleine.

Deine Mutter ist so dumm. Sie verläuft sich in einer Telefonzelle.

160      dumm Witze


Deine Mutter ist so fett. Ihr Schatten wiegt 100 Kilo.

153      fett Witze


Deine Mutter ist so fett. Wenn sie zu McDonald's geht, wird sie gefragt, was sie nicht bestellen will.

124      McDonald’s Witze


Deine Mutter ist so fett. Als sie sich an den Strand gelegt hat, wollten Umweltschützer sie ins Meer zurückschieben.

178      Mütterwitze


Deine Mutter macht piep beim Rückwärtslaufen!   

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
