# -*- coding: utf-8 -*-

"""
synthhaku subclassing test 1
~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a valid extension file for discord.py intended to
discover weird behaviors related to subclassing.

This variant overrides behavior using a Feature.

:copyright: (c) 2021 Devon (Gorialis) R
:license: MIT, see LICENSE for more details.

"""

from disnake.ext import commands

import synthhaku
from synthhaku.types import ContextT


class ThirdPartyFeature(synthhaku.Feature):
    """
    overriding feature for test
    """

    @synthhaku.Feature.Command(
        name="synthhaku", aliases=["jsk"], invoke_without_command=True, ignore_extra=False
    )
    async def jsk(self, ctx: ContextT):
        """
        override test
        """
        return await ctx.send(
            "The behavior of this command has been overridden with a third party feature."
        )


class Magnet1(
    ThirdPartyFeature, *synthhaku.OPTIONAL_FEATURES, *synthhaku.STANDARD_FEATURES
):  # pylint: disable=too-few-public-methods
    """
    The extended synthhaku cog
    """


async def setup(bot: commands.Bot):
    """
    The setup function for the extended cog
    """

    bot.add_cog(Magnet1(bot=bot))
