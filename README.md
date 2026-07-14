# DreamxBotz Auto Filter Bot

<p align="center">
  <img src="https://raw.githubusercontent.com/DreamXBotz/Pics/main/dreamxbotz.jpg" alt="DreamxBotz Logo" width="220">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12+">
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Ready">
  <img src="https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot">
</p>

<p align="center">
  <a href="https://t.me/Princess_V4_bot">
    <img src="https://img.shields.io/badge/Demo%20Bot-Click%20Here-blue?style=for-the-badge&logo=telegram" alt="Demo Bot">
  </a>
  <a href="https://t.me/Deendayal_Support_Group">
    <img src="https://img.shields.io/badge/Support%20Group-Join-blue?style=for-the-badge&logo=telegram" alt="Support Group">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  </a>
</p>

A Telegram auto-filter bot for indexing files from channels/groups, searching them quickly, and sharing files through Telegram bot commands. The project supports MongoDB storage, group settings, force subscription, verification, premium users, streaming links, and admin tools.

> This project is intended for educational use. Use it responsibly and follow Telegram rules, hosting provider rules, and copyright laws.

<!-- > ## ⚠ <u>Under Maintenance</u> ⚠
> This repository is currently under maintenance. Please **DO NOT deploy** until further notice. -->

## Table Of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Environment Variables](#required-environment-variables)
- [Deploy On Render](#deploy-on-render)
- [Deploy On Heroku](#deploy-on-heroku)
- [Deploy With Docker](#deploy-with-docker)
- [Local Setup](#local-setup)
- [Commands](#commands)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)

## Features

- Auto file indexing from Telegram channels/groups
- Fast auto-filter search in groups and private chat
- MongoDB database support
- Optional multiple database support
- Force subscription support
- Request-to-join force subscription support
- Three-step verification support
- Premium user management
- Movie update notification tools
- Stream and download link support
- Group settings menu
- Broadcast and group broadcast tools
- User ban/unban and chat disable tools
- Auto delete, file protection, and forward restriction options
- Maintenance mode for admin-controlled downtime

## Requirements

- Python 3.12+
- MongoDB database URI
- Telegram bot token from [@BotFather](https://t.me/BotFather)
- Telegram `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org)
- A log channel where the bot is added as admin

## Quick Links

| Link | URL |
| --- | --- |
| Demo Bot | [Open on Telegram](https://t.me/Princess_V4_bot) |
| Support Group | [Join Support](https://t.me/Deendayal_Support_Group) |
| Telegram API | [my.telegram.org](https://my.telegram.org) |
| BotFather | [Create Bot](https://t.me/BotFather) |
| MongoDB Atlas | [Create Database](https://www.mongodb.com) |

## Required Environment Variables

| Variable | Required | Description |
| --- | --- | --- |
| `BOT_TOKEN` | Yes | Telegram bot token from BotFather |
| `API_ID` | Yes | Telegram API ID from my.telegram.org |
| `API_HASH` | Yes | Telegram API hash from my.telegram.org |
| `DATABASE_URI` | Yes | MongoDB connection URI |
| `LOG_CHANNEL` | Yes | Telegram log channel ID, usually starts with `-100` |
| `ADMINS` | Yes | Space-separated Telegram user IDs or usernames |
| `CHANNELS` | Recommended | Space-separated channel/group IDs for indexing |

## Common Optional Variables

| Variable | Default | Description |
| --- | --- | --- |
| `DATABASE_NAME` | `Cluster0` | MongoDB database name |
| `COLLECTION_NAME` | `dreamcinezone_files` | MongoDB collection name |
| `BIN_CHANNEL` | `-100` | Channel used for file/bin logs |
| `PREMIUM_LOGS` | `-100` | Premium activity log channel |
| `AUTH_CHANNELS` | `-100` | Force subscription channel IDs |
| `AUTH_REQ_CHANNELS` | `-100` | Request-to-join force subscription channel IDs |
| `REQST_CHANNEL_ID` | `-100` | Request channel ID |
| `SUPPORT_CHAT_ID` | `-100` | Support group ID |
| `SUPPORT_CHAT` | `https://t.me/` | Support group link |
| `FQDN` | Web bind address | Public domain for stream links |
| `PORT` | `8080` | Web server port |
| `HAS_SSL` | `True` | Use HTTPS in generated stream URLs |
| `NO_PORT` | `False` | Hide port in generated HTTP stream URLs |
| `STREAM_MODE` | `True` | Enable stream mode |
| `PREMIUM_STREAM_MODE` | `False` | Restrict stream mode to premium users |
| `MAINTENANCE` | `False` | Enable maintenance mode |
| `IS_VERIFY` | `False` | Enable verification system |
| `SHORTENER_API` | Built-in fallback | Shortener API key for verification links |
| `SHORTENER_WEBSITE` | `omegalinks.in` | Shortener domain |
| `TMDB_API_KEY` | Empty | TMDB API key for movie metadata |

## Example `.env`

```env
BOT_TOKEN=123456:your_bot_token
API_ID=123456
API_HASH=your_api_hash
DATABASE_URI=mongodb+srv://user:password@cluster.mongodb.net/
DATABASE_NAME=Cluster0
COLLECTION_NAME=dreamcinezone_files
ADMINS=123456789
CHANNELS=-1001234567890
LOG_CHANNEL=-1001234567890
BIN_CHANNEL=-1001234567890
FQDN=your-app-name.onrender.com
HAS_SSL=True
NO_PORT=True
```

## Deploy On Render

1. Fork or upload this repository to GitHub.
2. Create a new Render Web Service.
3. Select Docker as the runtime.
4. Add the required environment variables from the table above.
5. Deploy the service.

Render must receive a valid `PORT` environment variable or use the default `8080`. If stream links use your Render domain, set:

```env
FQDN=your-app-name.onrender.com
HAS_SSL=True
NO_PORT=True
```

## Deploy On Heroku

This repository includes `app.json`, `Procfile`, and `heroku.yml`, so it can also run on Heroku-style deployments.

1. Create a Heroku app.
2. Add the required environment variables.
3. Deploy this repository.
4. Ensure the worker or web process is enabled according to your hosting setup.

## Deploy With Docker

Build the image:

```bash
docker build -t dreamxbotz .
```

Run the container:

```bash
docker run --env-file .env -p 8080:8080 dreamxbotz
```

## Local Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file with your configuration, then run:

```bash
python bot.py
```

## Commands

### User Commands

| Command | Description |
| --- | --- |
| `/start` | Start the bot |
| `/settings` | Open group settings |
| `/stats` | Show database stats |
| `/id` | Get Telegram ID |
| `/info` | Get user information |
| `/top` | Show top searched items |
| `/link` | Create a single file link |
| `/batch` | Create batch file links |

### Admin Commands

| Command | Description |
| --- | --- |
| `/movie_update` | Toggle movie update notifications |
| `/pm_search` | Toggle private message search |
| `/verification` | Show verified user count |
| `/delete` | Delete a specific file from database |
| `/deleteall` | Delete all files from database |
| `/deletefiles` | Delete PreDVD/CamRip files |
| `/broadcast` | Broadcast to users |
| `/grp_broadcast` | Broadcast to groups |
| `/ban` | Ban a user |
| `/unban` | Unban a user |
| `/add_premium` | Add premium access |
| `/remove_premium` | Remove premium access |
| `/premium_users` | List premium users |
| `/restart` | Restart the bot |
| `/maintenance` | Toggle maintenance mode |
| `/reset_group` | Reset group settings |
| `/trial_reset` | Reset user trial |
| `/remove_fsub` | Remove force subscription from a group |

## Public Repo Safety

- Do not commit `.env`, session files, logs, or virtual environments.
- Rotate any token or API key that was previously committed publicly.
- Keep real values only in your hosting provider environment variables.
- For public forks, avoid hardcoding shortener, TMDB, Telegraph, MongoDB, or Telegram credentials.

## Troubleshooting

### `AttributeError: 'NoneType' object has no attribute 'lower'`

This happens when a boolean environment variable is missing and the parser tries to call `.lower()` on `None`. The helper in `info.py` should return the default value when an env var is not set.

### `ValueError` near `API_ID`

Set a valid numeric `API_ID` in your environment variables.

### MongoDB connection error

Check that `DATABASE_URI` is valid, the database user has access, and your hosting provider IP is allowed in MongoDB Atlas.

### Stream links are wrong

Set `FQDN`, `HAS_SSL`, and `NO_PORT` according to your hosting provider domain.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

Special thanks to:

- [⌯ Ꭺɴᴏɴʏᴍᴏᴜs | ×͜× |](https://t.me/BeingXAnonymous)
- [⌯ ᴢɪsʜᴀɴ | ×͜× |](https://t.me/IM_JISSHU)
- [⌯ ʙʜᴀʀᴀᴛʜ | ×͜× |](https://t.me/Bharath_boy)
- [Harshal Purohit Edits](https://github.com/HarshalPurohitEdits)
- [Support Group](https://t.me/Deendayal_Support_Group)

Thanks to the DreamXBotz community and all contributors who worked on the original project and related modules.
