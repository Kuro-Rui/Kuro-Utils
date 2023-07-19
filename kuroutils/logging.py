# Thanks Laggron!
# https://github.com/laggron42/Laggron-utils/blob/master/laggron_utils/logging.py#L41-L78

import logging

from red_commons.logging import RedTraceLogger, getLogger
from redbot.core import commands
from redbot.core.data_manager import cog_data_path
from redbot.logging import RotatingFileHandler

__all__ = ("get_logger", "init_logger", "close_logger")


def get_logger(cog: commands.Cog) -> RedTraceLogger:
    return getLogger(f"red.kuro-cogs.{cog.qualified_name.lower()}")


def init_logger(cog: commands.Cog, logger: RedTraceLogger) -> None:
    formatter = logging.Formatter(
        "[{asctime}] {levelname} [{name}] {message}", datefmt="%Y-%m-%d %H:%M:%S", style="{"   
    )
    # logging to a log file
    # file is automatically created by the module, if the parent folder exists
    cog_path = cog_data_path(cog)
    if cog_path.exists():
        file_handler = RotatingFileHandler(
            stem=cog.qualified_name.lower(),
            directory=cog_path,
            maxBytes=1000000,
            backupCount=8,
            encoding="utf-8",
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


def close_logger(logger: RedTraceLogger) -> None:
    for handler in logger.handlers:
        handler.close()
    logger.handlers = []
