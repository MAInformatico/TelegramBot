
# TelegramBot

A lightweight Telegram bot built with Python to monitor your server and keep track of the devices connected to your local network.

The bot provides real-time access to server temperature and LAN device information directly through Telegram.

It is designed to work alongside [Raspberry-Pi-Monitoring-Network](https://github.com/MAInformatico/Raspberry-Pi-Monitoring-Network), providing a convenient way to access monitoring information remotely.

## Features

- 🌡️ **Server temperature:** Check your server's current temperature.
- 🖥️ **Network monitoring:** Get a list of devices currently connected to your local network.
- 🤖 **Telegram integration:** Access monitoring information through simple Telegram commands.
- 🐳 **Docker support:** Build and run the bot inside a Docker container.
- 🐍 **Python-based:** Lightweight implementation using Python 3 and the Telegram Bot API.

## Telegram Commands

| Command | Description |
|---|---|
| `/start` | Not implemented yet. |
| `/help` | Display the available commands. |
| `/temperature` | Show the current server temperature. |
| `/hosts` | List the devices connected to your LAN. |

## Requirements

Before getting started, make sure you have:

- Python 3.11 or later.
- A Telegram account.
- A Telegram bot token from [@BotFather](https://t.me/BotFather).
- The monitoring data files required by the application.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/MAInformatico/TelegramBot.git
cd TelegramBot
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Alternatively, you can use the provided installation script:

```bash
chmod +x installer.sh
./installer.sh
```

### 4. Configure your Telegram bot

Create a Telegram bot using [@BotFather](https://t.me/BotFather) and obtain its API token.

Open `bot.py` and replace the placeholder token:

```python
application = Application.builder().token("your_token_here").build()
```

With your actual Telegram bot token.

**Security notice:** Never commit your Telegram bot token to a public repository. Consider moving it to an environment variable for a more secure configuration.

### 5. Prepare monitoring files

The application expects the following files in its working directory:

| File | Description |
|---|---|
| `temperature.txt` | Contains the current server temperature. |
| `hosts.txt` | Contains IP addresses detected on the local network. |
| `dictionary.txt` | Maps IP addresses to device hostnames. |

The expected format for `dictionary.txt` is:

```text
192.168.1.10 Router
192.168.1.20 RaspberryPi
192.168.1.30 Desktop
```

These files are part of the monitoring workflow and must be generated or supplied before using the corresponding commands.

## Usage

Once everything is configured, start the bot:

```bash
python bot.py
```

Open your Telegram conversation with your bot and send:

```text
/help
```

You can then use:

```text
/temperature
```

To retrieve the server temperature, or:

```text
/hosts
```

To see the devices connected to your local network.

## Docker

The repository includes a `Dockerfile` for containerized deployment.

### Build the image

```bash
docker build -t telegrambot .
```

### Run the container

```bash
docker run -d \
  --name telegrambot \
  --restart unless-stopped \
  telegrambot
```

Make sure the monitoring files and Telegram token are properly configured before starting the container.

## Project Structure

```text
TelegramBot/
│
├── bot.py             # Main Telegram bot application
├── checker.py         # Monitoring data processing
├── temperature.py     # Temperature-related functionality
├── suntime.py         # Sun-related calculations
├── avg.py             # Average calculations
│
├── installer.sh       # Python environment installation script
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker configuration
├── LICENSE            # GPL-3.0 license
└── README.md          # Project documentation
```

## Related Project

This project is part of a Raspberry Pi monitoring ecosystem.

Check out the companion repository:

- [Raspberry-Pi-Monitoring-Network](https://github.com/MAInformatico/Raspberry-Pi-Monitoring-Network)

It provides the monitoring infrastructure and network information consumed by this Telegram bot.

## Technologies

- [Python](https://www.python.org/)
- [python-telegram-bot](https://python-telegram-bot.org/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Docker](https://www.docker.com/)

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

This project was inspired by tutorials and resources from the Python and Telegram bot development community, including [freeCodeCamp](https://www.freecodecamp.org/).

---

**Developed by [MAInformatico](https://github.com/MAInformatico)**
