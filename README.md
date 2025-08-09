# Ticket-Bot
## Features

- `!ticket` - create a private ticket channel
- `!close` - close and delete the current ticket
- `!ping` - check bot latency
- `!serverinfo` - show basic information about the server

- ## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your bot token in the `DISCORD_TOKEN` environment variable.
3. Run the bot:
   ```bash
   python bot.py
   ```

   ## Notes

This example uses text commands with the `!` prefix. For production use, consider adding
role checks, persistent ticket IDs, and database support.
