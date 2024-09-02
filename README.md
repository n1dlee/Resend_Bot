# Telegram Bot for Group Message Forwarding

This Telegram bot forwards messages from a group chat to specific users in a round-robin fashion.

## Features

- Forwards messages from a group chat to predefined users
- Uses SQLite database to keep track of the current message recipient
- Rotates recipients after each message

## Requirements

- Python 3.7+
- python-telegram-bot library
- SQLite3

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install python-telegram-bot
   ```
3. Set up your Telegram bot token and user IDs in `config.py`

## Usage

1. Run the bot:
   ```
   python app.py
   ```
2. Add the bot to your group chat
3. Start sending messages in the group

## Configuration

Edit `config.py` to set your bot token and user IDs:

```python
TOKEN = 'your_bot_token_here'
USERS = ['user_id_1', 'user_id_2', ...]
```

## License

This project is open-source and available under the MIT License.
