from os import getenv, path
from uuid import UUID

from dotenv import load_dotenv

from bot import config
from bot.bot import SquareBot

dotenv_path: str = './bot/.env'
language: dict[str, str] = config.RESPONSES.get(config.LANGUAGE)

if not path.exists(dotenv_path):
    print(language.get('dotenv_missing'))
    bot_token = input(
        language['initialization'].get('bot_token', str())
    ).strip()
    api_token = input(
        language['initialization'].get('api_token', str())
    ).strip()
    with open(dotenv_path, 'w') as dotenv_file:
        try:
            UUID(api_token)
        except ValueError:
            print(language['initialization'].get('invalid_token'))
        dotenv_file.write(
            f'BOT_TOKEN={bot_token}\n' + f'API_TOKEN={api_token}'
        )
    del bot_token, api_token

load_dotenv()
client = SquareBot(language)
client.run(getenv('BOT_TOKEN'))
