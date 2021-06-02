import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

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
        "Deine Mutter ist die Kugel in Indiana Jones"
    ]

    def get_joke():
        return random.choice(jokes)

    if message.content == '!witz':
        response = get_joke()
        await message.channel.send(response)

client.run(TOKEN)