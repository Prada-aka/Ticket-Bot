# Ticket Bot

A simple Discord bot that lets users create support ticket channels.

## Setup

1. Install dependencies:
   ```bash
   pip install discord.py
   ```
2. Set the bot token as an environment variable:
   ```bash
   export DISCORD_TOKEN="your-bot-token"
   ```
3. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

Use the `!ticket` command to create a new support channel. Provide an optional name to customize the channel:

```
!ticket            # creates a channel named 'support'
!ticket billing    # creates a channel named 'billing'
```

The bot will respond with a mention to the created channel and open it for the requesting user.
