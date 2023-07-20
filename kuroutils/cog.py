import contextlib
from typing import List, Optional

import discord
from redbot.cogs.downloader.installable import InstalledModule
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import humanize_list

from .logging import close_logger, get_logger, init_logger


class Cog(commands.Cog):
    __author__: List[str] = ["Kuro"]
    __commit__: Optional[str] = None
    __version__: str = "0.0.1"

    def __init__(self, bot: Red):
        self.bot = bot
        self._log = get_logger(self)
        init_logger(self, self._log)

    async def get_cog_as_installed_module(self) -> Optional[InstalledModule]:
        if not (downloader := self.bot.get_cog("Downloader")):
            return
        name = self.qualified_name.lower()
        name += "cog" if name == "calendar" else ""
        return discord.utils.get(await downloader.installed_cogs(), name=name)

    async def cog_load(self) -> None:
        await self.bot.wait_until_red_ready()
        if module := await self.get_cog_as_installed_module():
            self.__commit__ = module.commit
            if repo_url := getattr(module.repo, "clean_url", None):
                self.__version__ += f"+g[{module.commit[:7]}]({repo_url}/commit/{module.commit})"
            else:
                self.__version__ += f"+g[{module.commit[:7]}]"
        if 732425670856147075 in self.bot.owner_ids:
            with contextlib.suppress(RuntimeError, ValueError):
                self.bot.add_dev_env_value(self.qualified_name, lambda ctx: self)

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        cog_name = self.qualified_name.lower()
        docs = f"https://kuro-cogs.readthedocs.io/en/latest/cogs/{cog_name}.html"
        return (
            f"{pre_processed}\n\n"
            f"`Cog Authors   :` {humanize_list(self.__author__)}\n"
            f"`Cog Version   :` {self.__version__}\n"
            f"`Documentation :` [Click here to read!]({docs})"
        )

    def cog_unload(self):
        close_logger(self._log)
