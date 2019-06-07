# Git Slack Bot

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
source env/bin/activate
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
