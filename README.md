# DiscordBot Template
This repository provides a template to quickly set up a Discord bot with various functionalities. The template is designed to streamline the process of integrating essential features such as command handling, message responses, scheduled tasks, and environment management. By using this template, you can focus on customizing the bot's behavior and adding unique features without worrying about the underlying setup complexities.

## Features of This Template

- **Command Handling**: Easily create and manage bot commands.
- **Scheduled Tasks**: Implement tasks that run at specific times or intervals.
- **Message Handling**: Respond to user messages and interact with Discord channels.
- **Environment Variable Management**: Securely manage sensitive information like bot tokens.


## Discord Bot Setup Guide

This guide will walk you through setting up your Discord bot. The bot is written in Python and uses the `discord.py` library. Follow the steps below to get your bot up and running.

## Prerequisites

Before you start, make sure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine. You can do this using the following command:

```bash
git clone git@github.com:JuliusBooth/DiscordBotTemplate.git
cd DiscordBotTemplate
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Your .env File

You need to create a .env file that contains your Discord bot token.

- Copy the .env.template file to a new file named .env:
```bash
cp .env.template .env
```
- Open the .env file and add your Discord bot token:
```bash
DISCORD_TOKEN=your_discord_bot_token_here
```
Replace your_discord_bot_token_here with your actual Discord bot token.

### 5. Set Up Your .env File
With everything set up, you can now start the bot:

```bash
python DiscordBot.py
```

Your bot should now be running. You can interact with it in your Discord server.

### 6. (Optional) Add Channel IDs
When responding to messages, you can easily obtain the Channel ID directly from the message context. However, for scheduling messages, it's necessary to know the Channel ID in advance. To find the Channel ID in Discord, follow these steps: 

Navigate to User Settings, then select the 'Advanced' option. Here, enable 'Developer Mode'. Once Developer Mode is activated, simply right-click on the desired channel in your server and select 'Copy ID' to copy the Channel ID.

## Additional Information
- To get a Discord bot token, you'll need to create a bot on the [Discord Developer Portal](https://discord.com/developers/applications).
- Ensure you've invited the bot to your Discord server with the appropriate permissions.


For more help, refer to the official discord.py documentation.

Good luck with your Discord bot!