from typing import Optional

import discord


async def delete_message(
    message: Optional[discord.Message], delay: Optional[float] = None
) -> bool:
    """
    Delete a message, ignoring any exceptions.
    Easier than putting these 3 lines at each message deletion for each cog.

    Thanks AAA3A! (https://github.com/AAA3A-AAA3A/AAA3A_utils/blob/main/AAA3A_utils/cogsutils.py#L487-L504)
    """
    if not message:
        return True
    try:
        await message.delete(delay=delay)
    except discord.NotFound:
        return True
    except discord.HTTPException:
        return False
    return True
