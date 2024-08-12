from os import path, getenv
from dotenv import load_dotenv
from bot import config
from bot.bot import SquareBot
from uuid import UUID

dotenv_path: str = './bot/.env'
language: dict[str, str] = config.RESPONSES.get(config.LANGUAGE)

if not path.exists(dotenv_path):
    print(language.get('dotenv_missing'))
    bot_token = input(language.get('bot_token')).strip()
    api_token = input(language.get('api_token')).strip()
    with open(dotenv_path, 'w') as dotenv_file:
        try:
            UUID(api_token)
        except ValueError as e:
            print(language.get('invalid_token'))
        dotenv_file.write(
            f'BOT_TOKEN={bot_token}\n'+
            f'API_TOKEN={api_token}'
        ) 
    del bot_token, api_token
    
load_dotenv()
client = SquareBot(language)
client.run(getenv('BOT_TOKEN'))
