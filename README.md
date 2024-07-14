# Telegram Resend Bot

This Telegram bot listens to messages in a specified group and forwards them to two users in a round-robin fashion.

## Features

- Listens for messages in a specified group.
- Forwards messages to two users alternately.
- Uses SQLite for tracking the current receiver.
- Logs activities for monitoring and debugging.

## Requirements

- Python 3.8+
- `python-telegram-bot` library
- `sqlite3` library

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/telegram-resend-bot.git
   cd telegram-resend-bot
  ``
2. **Create and activate a virtual environment:**

  ```sh
  python3 -m venv venv
  source venv/bin/activate
  ``` 
3. **Install the dependencies:**

  ```sh
  pip install -r requirements.txt
  ```
4. **Initialize the database:**
  ```sh
  python init_db.py
  ```
5. **Configuration**
Update the TOKEN variable in app.py with your Telegram bot token.
Update the USERS list in app.py with the numeric user IDs of the two users who should receive the messages.

6. **Running the Bot**
To start the bot, run the following command:
  ```sh
  python app.py
  ```

**Running the Bot as a Service**
If you are running this bot on a server, you can set it up as a systemd service to ensure it runs continuously and restarts on failure.

1. **Create a systemd service file:**

 ```ini
[Unit]
Description=Telegram Resend Bot
After=network.target

[Service]
User=your_username
WorkingDirectory=/path/to/your/project
ExecStart=/path/to/your/project/venv/bin/python /path/to/your/project/app.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
2. **Move the service file to the systemd directory:**

  ```sh
  sudo mv telegram_bot.service /etc/systemd/system/telegram_bot.service
  ```
3. **Reload systemd and start the bot service:**

  ```sh

  sudo systemctl daemon-reload
  sudo systemctl start telegram_bot.service
  sudo systemctl enable telegram_bot.service
  ```
4. **Logging**
Logs are written to bot.log in the project directory. You can view the logs with the following command:

  ```sh
  tail -f bot.log
  ```
**License*
This project is licensed under the MIT License. See the LICENSE file for details.

**Contributing**
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

**Support**
If you encounter any issues or have questions, feel free to open an issue on GitHub or contact the maintainer.
