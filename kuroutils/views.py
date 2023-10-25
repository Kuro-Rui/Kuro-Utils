from typing import Dict
import discord


class LinksView(discord.ui.View):
    """
    A view that creates link buttons.

    Parameters
    ----------
    labels_and_urls: Dict[:class:`str`, :class:`str`]
        A dict of labels and URLs for the buttons. Max length is 25.
    """
    def __init__(self, labels_and_urls: Dict[str, str]) -> None:
        super().__init__(timeout=None)
        for label, url in labels_and_urls.items():
            self.add_item(discord.ui.Button(style=discord.ButtonStyle.link, label=label, url=url))
