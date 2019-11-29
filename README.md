# Git Slack Bot

[![Pull-Requests](https://img.shields.io/github/issues-pr/parithiban/git-slack-bot.svg?color=blue&style=plastic)](https://github.com/parithiban/git-slack-bot/pulls/)
[![Issues](https://img.shields.io/github/issues-raw/parithiban/git-slack-bot.svg?style=plastic)](https://github.com/parithiban/git-slack-bot/issues)

[![GitHub contributors](https://img.shields.io/github/contributors/parithiban/git-slack-bot.svg?style=plastic&color=blue)](https://GitHub.com/parithiban/git-slack-bot/graphs/contributors/)
![Last Commit](https://img.shields.io/github/last-commit/parithiban/git-slack-bot.svg?style=plastic)

[![GitHub forks](https://img.shields.io/github/forks/parithiban/git-slack-bot.svg?style=social)](https://github.com/parithiban/git-slack-bot/network/)
[![GitHub stars](https://img.shields.io/github/stars/parithiban/git-slack-bot.svg?style=social)](https://github.com/parithiban/git-slack-bot/stargazers)
[![GitHub watchers](https://img.shields.io/github/watchers/parithiban/git-slack-bot.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/parithiban/git-slack-bot/watchers/)
[![GitHub followers](https://img.shields.io/github/followers/parithiban.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/parithiban?tab=followers)

This is a slack bot that is integrated with git to post some awesome notifications in slack

## Requirements

If you are wanting to build and develop this, you will need the following items installed.

- Python version 3.7+
- Pip
- Redis

## Installation Steps

#### Clone the Repo

```bash
git clone https://github.com/parithiban/git-slack-bot.git
cd git-slack-bot
```

#### Install dependency

```bash
make all
```

#### Activate your virtual environment

```bash
source venv/bin/activate
```

#### Setup Environment Variable

create a file .env similar to .env.example with updated tokens

#### Run the Application

Inside the virtual environment execute

```bash
make run
```

#### Run the Redis Queue

Inside the virtual environment execute

```bash
export FLASK_APP=manage.py
make run-queue
```

#### Monitor Queue

To monitor the queue

`http://{YOUR_URL}/queue/`

#### Documentation for slack comand

https://api.slack.com/slash-commands#creating_commands

#### List of Permission for bot to access

Once you have installed it in your slack workspace you need to give below scope access

```
channels:read
chat:write:bot
chat:write:user
im:read
users:read
users.profile:read
```

#### Check it live

Run the command

`ngrok http 5000`

You will get the http url replace that in Request URL in slash command

Ex: ![Alt text](assests/ngrok.png?raw=true "Ngrok")

#### Available commands

Run `/git help` to list the commands

Ex: ![Alt text](assests/help_command.png?raw=true "help_command")

#### Example command

Run `/git pr your_repo`

Ex: ![Alt text](assests/output.png?raw=true "output")

Test PR
