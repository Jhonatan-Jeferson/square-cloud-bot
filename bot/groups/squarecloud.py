from os import getenv

from discord import Interaction, app_commands
from discord.ext.commands import Bot


class Square(app_commands.Group):
    """This group brings all square slash commands"""

    @app_commands.command(name='account_info')
    async def get_account_info(self, interaction: Interaction):
        """This command gets the account info of the token owner"""

    @app_commands.command(name='apps')
    async def get_apps(self, interaction: Interaction):
        """This command gets all applications bounded of the token owner"""

    @app_commands.command(name='app')
    async def get_app(self, interaction: Interaction, app: str):
        """This command gets the app by its id"""

    @app_commands.command(name='upload_app')
    async def upload_app(self, interaction: Interaction):
        """This command upload a new app to Square Cloud"""

    @app_commands.command(name='bind_webhook')
    async def bind_webhook(
        self, interaction: Interaction, app: str, webhook: str
    ):
        """This command binds an github webhook to an application"""


async def setup(client: Bot) -> None:
    """Load the group on bot"""
    client.tree.add_command(Square())
