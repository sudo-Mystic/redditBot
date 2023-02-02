# redditBot

redditBot is a Reddit bot that provides real-time market updates for Adani Group and Indian market indices. 

## Requirements

- Python 3.7 or higher
- PRAW (Python Reddit API Wrapper)
- Nsetools

## Installation

1. Clone the repository 
```git clone https://github.com/sudo-Mystic/redditBot.git```
2. Create a virtual environment and activate it
```python3 -m venv env```
```source env/bin/activate ```
3. Install the required packages
```pip install -r requirements.txt```

4. Create a Reddit app and obtain the following values:
  - client_id
  - client_secret
  - user_agent
  - username
  - password
5. Store the values in environment variables as follows:

```export clientid='your_client_id'```
```export clientsecret='your_client_secret'```
```export useragent='your_user_agent'```
```export username='your_username'```
```export password='your_password'```

## Usage

1. Navigate to the cloned repository
```cd redditBot
```
2. Run the bot
```python bot.py```

## Commands
- `!adani help` - Display the list of available commands
- `!adani marketaction` - Display the current market action of NIFTY 50, NIFTY BANK, NIFTY IT
- `!adani sob` - Display the current market action of Adani Group companies: ADANIENT, ADANIGREEN, ADANIPORTS, ADANIPOWER, ADANITRANS, ATGL, AWL.

## Contributing

Contributions are welcome. Feel free to submit a pull request.
