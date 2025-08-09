import os
import asyncio
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

_ticket_counter = 0

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(help="Open a new support ticket")
async def ticket(ctx):
    """Create a private ticket channel for the requesting user."""
    global _ticket_counter
    _ticket_counter += 1
    guild = ctx.guild
    category = discord.utils.get(guild.categories, name="Tickets")
    if category is None:
        category = await guild.create_category("Tickets")

    channel = await guild.create_text_channel(f"ticket-{_ticket_counter}", category=category)
    await channel.set_permissions(guild.default_role, read_messages=False)
    await channel.set_permissions(ctx.author, read_messages=True, send_messages=True)
    await channel.send(
        f"{ctx.author.mention} thanks for opening a ticket. Use `!close` when you're done."
    )
    await ctx.send(f"Ticket created: {channel.mention}")

@bot.command(help="Close the current ticket")
async def close(ctx):
    """Close and delete the ticket channel after a short delay."""
    if ctx.channel.category and ctx.channel.category.name == "Tickets":
        await ctx.send("Closing ticket in 5 seconds...")
        await asyncio.sleep(5)
        await ctx.channel.delete()
    else:
        await ctx.send("This command can only be used in ticket channels.")

@bot.command(help="Check bot latency")
async def ping(ctx):
    """Respond with the bot's latency."""
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command(help="Show information about the server")
async def serverinfo(ctx):
    """Display basic information about the guild."""
    guild = ctx.guild
    embed = discord.Embed(title=guild.name, color=discord.Color.blue())
    embed.add_field(name="Member Count", value=str(guild.member_count))
    embed.set_thumbnail(url=guild.icon.url if guild.icon else discord.Embed.Empty)
    await ctx.send(embed=embed)

if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("DISCORD_TOKEN environment variable not set")
    bot.run(TOKEN)
