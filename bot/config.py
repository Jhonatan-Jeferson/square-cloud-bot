DB_TYPE: str | None = None  # change this to add a database to your bot
LANGUAGE: str = 'PT-BR'             # if you want, you can change to 'EN-US'
RESTART_APLICATIONS: bool = (
    True  # set it False if you don't wanna the bot turning all your apps
)
LOGS_CHANNEL: int | None = None       # set it with the id of a discord channel you wanna it to send logs

DB_types: list[str] = ['mongodb', 'sql']
RESPONSES: dict[str, str] = {
    'PT-BR': {
        'initialization': {
            'dotenv_missing': '\033[1m\033[31mWARNING: Você não tem um dotenv\033[0m',
            'bot_token': 'Insira seu token do bot discord: ',
            'api_token': 'Insira seu token de api da square: ',
            'invalid_token': 'Token inválido',
            'on_ready': 'Sou {bot_name}, estou online e pronto pra uso!',
            'load_cogs': 'Cogs carregados com sucesso -> {cogs}',
            'load_error': 'Erro ao carregar o arquivo: {cog_name}'
        }
    },
    'EN-US': {
        'initialization': {
            'dotenv_missing': "\033[31mWARNING: You don't have an dotenv\033[0m",
            'bot_token': 'Insert discord bot token: ',
            'api_token': 'Insert square api token: ',
            'invalid_token': 'Invalid Token',
            'on_ready': "i'm {bot_name}, i'm online and ready",
            'load_cogs': 'loaded successfully -> {cogs}',
            'load_error': 'Error while loading the file: {cog_name}',
        },
    },
}
