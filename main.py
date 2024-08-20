from os import getenv

from dotenv import load_dotenv

from bot import config
from bot.bot import SquareBot


def check_for_environment(language: dict[str,str]) -> None:
    """This function checks if you created the environment"""
    from uuid import UUID
    from os import path
    
    dotenv_path: str = './bot/.env'
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
                f'BOT_TOKEN={bot_token}\nAPI_TOKEN={api_token}'
            )

def main() -> None:    
    language: dict[str, str] = config.RESPONSES.get(config.LANGUAGE)
    check_for_environment(language)
    load_dotenv()
    client = SquareBot(language)
    client.run(getenv('BOT_TOKEN'))

main()