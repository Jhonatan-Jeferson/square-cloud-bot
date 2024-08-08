from discord.ext.commands import Cog, Bot
from discord import app_commands, Interaction, Embed, Colour


class SquareCommands(Cog):

    """
    (Português)Este é o Cog dos comandos da square
    (English) This is the square commands Cog
    """

    def __init__(self, client: Bot) -> None:

        # Definindo o bot dentro do cog
        self.bot = client
        
    @app_commands.command(name="set_token")
    async def set_token(self, interaction: Interaction) -> None:
    	
    	"""Defines the acess token of a user"""
    	pass

    @app_commands.command(name="apps")
    async def get_ui(self, interaction: Interaction) -> None:

        """Sends the UI"""
        pass


async def setup(client: Bot) -> None:

    """Setup necessário pro bot carregar o cog"""

    await client.add_cog(SquareCommands(client))
