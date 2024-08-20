from os import listdir, path

from discord import Intents
from discord.ext.commands import Bot
from squarecloud import Client


class SquareBot(Bot):
    """
    (Português) Isto é a subclasse do Bot\n
    (English) This is the Bot subclass
    """

    def __init__(self, locale: dict[str, str]) -> None:
        from os import getenv
        
        super().__init__(command_prefix='.', intents=Intents.default())
        self.synced = False
        self.locale = locale
        self.square = Client(getenv('API_TOKEN'))

    async def _load_modules(self, pathing: str):
        """Load modules from path automatically looking every file in a dir"""
        for files in listdir(pathing):
            try:
                await self.load_extension(
                    '.'.join(path.split(pathing)) + '.' + files[-3]
                )
            except Exception as e:
                print(
                    self.locale['initialization']
                    .get('load_error')
                    .format(cog_name=files)
                )
                print(e)

    async def setup_hook(self) -> None:
        """
        (Português) Tudo que acontece antes do bot ligar\n
        (English) Everything that happens before the bot turns on
        """
        from asyncio import gather

        path_to_cogs = 'bot/cogs'
        path_to_groups = 'bot/groups'
        await gather(
            self._load_modules(path_to_cogs),
            self._load_modules(path_to_groups),
        )
        print(
            self.locale['inicialization']
            .get('load_cogs')
            .format(', '.join(cogs=self.cogs.keys()))
        )

    async def on_ready(self) -> None:
        """
        (Português) Quando o bot vai ligar e está pronto pra uso\n
        (English) When the bot is ready
        """
        if not self.synced:
            await self.tree.sync()
            self.synced = True
        print(
            self.locale.get('on_ready', str()).format(bot_name=self.user.name)
        )
