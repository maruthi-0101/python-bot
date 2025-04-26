import discord
import requests
import json

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        # Prevent bot from responding to itself
        if message.author == self.user:
            return

        # Check if message starts with $meme
        if message.content.startswith('$meme'):
            meme_url = get_meme()   # Call meme function
            await message.channel.send(meme_url)  # Send meme

# Set Intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot object
client = MyClient(intents=intents)

# Run bot
client.run('YOUR-TOKEN')   # (Don't expose real token)