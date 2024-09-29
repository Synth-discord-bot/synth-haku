# -*- coding: utf-8 -*-

"""
synthhaku subclassing test 2
~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a valid extension file for discord.py intended to
discover weird behaviors related to subclassing.

This variant overrides behavior directly.

:copyright: (c) 2021 Devon (Gorialis) R
:license: MIT, see LICENSE for more details.

"""

from disnake.ext import commands

import synthhaku
from synthhaku.types import ContextT


class Magnet2(
    *synthhaku.OPTIONAL_FEATURES, *synthhaku.STANDARD_FEATURES
):  # pylint: disable=too-few-public-methods
    """
    The extended synthhaku cog
    """

    @synthhaku.Feature.Command(
        name="synthhaku", aliases=["jsk"], invoke_without_command=True, ignore_extra=False
    )
    async def jsk(self, ctx: ContextT):
        """
        override test
        """
        return await ctx.send(
            "The behavior of this command has been overridden directly."
        )


async def setup(bot: commands.Bot):
    """
    The setup function for the extended cog
    """

    bot.add_cog(Magnet2(bot=bot))  # type: ignore[reportGeneralTypeIssues]
