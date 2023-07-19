try:
    from emoji import UNICODE_EMOJI_ENGLISH as EMOJI_DATA  # emoji<2.0.0
except ImportError:
    from emoji import EMOJI_DATA  # emoji>=2.0.0
from redbot.core import commands


class Emoji(commands.EmojiConverter):
    async def convert(self, ctx: commands.Context, argument: str) -> str:
        if argument in EMOJI_DATA:
            return argument
        return str(await super().convert(ctx, argument))
