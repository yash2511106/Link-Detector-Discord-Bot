import discord

TOKEN = 'YOUR_BOT_TOKEN_HERE'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  
    if "http://" in message.content or "https://" in message.content:
        try:
            await message.delete()
            print(f"Deleted a link from {message.author.name} in #{message.channel.name}")
        except discord.Forbidden:
            print(f"Error: Bot does not have permission to delete messages in #{message.channel.name}")
        except discord.NotFound:
            print(f"Error: Message to delete not found in #{message.channel.name}")
        except Exception as e:
            print(f"An error occurred while deleting a link: {e}")

client.run(TOKEN)
