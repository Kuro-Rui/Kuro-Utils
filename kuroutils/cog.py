from typing import List, Optional

import discord
from redbot.cogs.downloader.installable import InstalledModule
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import humanize_list


class Cog(commands.Cog):
    __author__: List[str] = ["Kuro"]
    __commit__: Optional[str] = None
    __version__: str = "0.0.1"

    def __init__(self, bot: Red):
        self.bot = bot

    async def get_cog_as_installed_module(self) -> Optional[InstalledModule]:
        if not (downloader := self.bot.get_cog("Downloader")):
            return
        name = self.qualified_name.lower()
        name += "cog" if name == "calendar" else ""
        return discord.utils.get(await downloader.installed_cogs(), name=name)

    async def get_cog_commit(self) -> Optional[str]:
        if module := await self.get_cog_as_installed_module():
            return module.commit

    async def get_cog_repo_url(self) -> Optional[str]:
        if module := await self.get_cog_as_installed_module():
            if module.repo:
                return module.repo.clean_url

    async def cog_load(self) -> None:
        if commit := await self.get_cog_commit():
            self.__commit__ = commit
            if repo_url := await self.get_cog_repo_url():
                self.__version__ += f"+g[{commit[:7]}]({repo_url}/commit/{commit})"
            else:
                self.__version__ += f"+g[{commit[:7]}]"

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        cog_name = self.qualified_name.lower()
        docs = f"https://kuro-cogs.readthedocs.io/en/latest/cogs/{cog_name}.html"
        return (
            f"{pre_processed}\n\n"
            f"`Cog Authors   :` {humanize_list(self.__author__)}\n"
            f"`Cog Version   :` {self.__version__}\n"
            f"`Documentation :` [Click here to read!]({docs}"
        )
