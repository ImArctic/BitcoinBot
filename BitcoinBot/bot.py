
from discord.ext import commands
import discord
from discord import app_commands
import main

bot = commands.Bot(command_prefix="!", intents = discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Bot singed in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Integration):
    await interaction.response.send_message(f"Hey {interaction.user.mention}", ephemeral=True)

@bot.tree.command(name="buy")
@app_commands.describe(listing_id = "Listing ID")
@app_commands.describe(amount = "Amount")
async def buy(interaction: discord.Integration, listing_id: int, amount: int):
    data = ""
    for i in range(0, amount+1):
        data += f"{main.InitiateTransaction(interaction.user.id, listing_id)}\n"

    channel = await interaction.user.create_dm()
    await channel.send(f"Your Order:\n```{data}```")

bot.run("MTAyMDAxNDE3NDcyNzg0Mzk0MA.GY7rGX.4dbOh8PsxBbVlD-ru27YGThqMIhbi_W7BrzOKI")