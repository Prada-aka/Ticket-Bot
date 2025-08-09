import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(name="ticket")
async def create_ticket(ctx, *, channel_name: str = "support"):
    guild = ctx.guild
    channel_name = channel_name.replace(" ", "-")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
    }

    existing = discord.utils.get(guild.channels, name=channel_name)
    if existing:
        await ctx.send(f"A channel named `{channel_name}` already exists.")
        return

    channel = await guild.create_text_channel(channel_name, overwrites=overwrites)
    await channel.send(f"{ctx.author.mention} this is your support channel.")
    await ctx.send(f"Created channel {channel.mention} for you.")

bot.run(TOKEN)
