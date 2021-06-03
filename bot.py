import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
jokes = [
        "Deine Mutter bekommt beim Elternabend einen Klassenbucheintrag.",
        "Deine Mudder kauft Ihre Binden im Matratzen-Geschäft.",
        "Google Earth hat angerufen, deine Mutter steht im Bild.",
        "Deine Mutter ist so fett, sie guckt die Speisekarte an und sagt zum Kellner: 'ok'.",
        "Deine Mutter schüttet Actimel über den Computer, damit er gegen Viren geschützt ist.",
        "Deine Mutter arbeitet bei IKEA als unterste Schublade.",
        "Deine Mutter bringt sogar das Happy-Meal zum Weinen.",
        "Deine Mutter geht zu “Wer wird Millionär?” und macht Schulden.",
        "Deine Mutter ist so fett, die bricht vom Stammbaum ab.",
        "Wenn deine Mutter Zwiebeln schneidet, weinen die Zwiebeln.",
        "Deine Mutter zieht Flip Flops mit einem Schuhlöffel an.",
        "Deine Mutter bestellt sich gleich zweimal All you can Eat.",
        "Deine Mutter macht 5 Diäten, weil sie von einer nicht satt wird.",
        "Deine Mutter steckt sich eine Münze ins Ohr und denkt sie hört 50 Cent.",
        "Deine Mutter steht gerade hinter dir und fragt sich, woher wir das alles über sie wissen.",
        "Deine Mutter zieht Katapulte nach Gondor.",
        "Deine Mutter ist die Kugel in Indiana Jones",
        "Deine Mutter kann ihr Profilbild bei Facebook nicht speichern – die Datei ist zu groß.",
        "Deine Mutter kann ihr Profilbild bei Facebook nicht speichern – die Datei ist zu groß.",
        "Deine Mutter ist wie die Weimarer Republik. Ihre Verfassung könnte besser sein.",
        "Deine Mutter ist sogar in Minecraft rund.",
        "Wenn deine Mutter sich auf die Waage stellt, sieht sie ihre Telefonnummer.",
        "Deine Mutter kippt beim Joghurt mit der Ecke die große in die kleine.",
        "Deine Mutter ist in Chewbacca verliebt. Sie dachte nie, dass sie jemanden findet, der genauso haarig ist.",
        "Deine Mutter stürzt öfter ab als Windows.",
        "Deine Mutter schreibt die Texte für Scooter.",
        "Deine Mutter arbeitet am Strand als Schatten.",
        "Deine Mutter kocht Wasser nach Rezept.",
        "Deine Mutter wird von 30 Großwildjägern gesucht",
        "Deine Mutter ist das Nebelhorn auf nem Kreuzfahrtschiff.",
        "Wenn deine Mutter tanzen geht, bekommt der Begriff Walzer ‘ne ganz neue Bedeutung.",
        "Deine Mutter heißt Dieter und ist der Haarigste im Zoo.",
        "Wenn deine Mutter an meinem Haus vorbeigeht, ist es drei Tage dunkel.",
        "Deine Mutter ist so hässlich, dein Vater nimmt sie mit auf die Arbeit, damit er ihr keinen Abschiedskuss geben muss.",
        "Deine Mutter wurde von Aliens entführt. Sie haben sie nach fünf Minuten wieder zurückgebracht.",
        "Deine Mutter arbeitet auf einem Fischkutter – als Geruch.",
        "Deine Mutter ist so fett, als ich ihr gegenüberstand und mich umdrehte, war sie immer noch da.",
        "Deine Mutter schaut sich bei YouTube Tutorials fürs Brotschneiden an.",
        "Wenn deine Mutter strippt, bekommt sie viel Geld – dafür, dass sie sich schnell wieder anzieht."
    ]

def get_joke():
        return random.choice(jokes)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='type !witz'))

    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!witz':
        response = get_joke()
        await message.channel.send(response)

client.run(TOKEN)