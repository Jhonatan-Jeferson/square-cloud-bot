from discord import Colour, Embed, Interaction, app_commands
from discord.ext.commands import Bot, Cog
from discord.ext.tasks import loop


class SquareCommands(Cog):
    """
    (Português)Este é o Cog dos comandos da square\n
    (English) This is the square commands Cog
    """

    def __init__(self, client: Bot) -> None:
        from ..config import RESTART_APLICATIONS

        self.bot = client
        if RESTART_APLICATIONS is True:
            self.start_applications.start()

    @loop(name='start_offline_apps', minutes=5)
    async def start_applications(self):
        """This task will check all your applications and gonna start the offline ones"""


async def setup(client: Bot) -> None:
    """Setup necessário pro bot carregar o cog"""
    await client.add_cog(SquareCommands(client))
