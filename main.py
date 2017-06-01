import discord
from discord.ext import commands
import sys
import traceback
import os

"""
Note : S'assurer de ne pas envoyer de message au bot qui pourrait dépasser les 2000 caractères
"""

description = """ Le bot de la plateforme Trapstorm """

initial_extensions = [
    'cogs.song',
    'cogs.user',
]

bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"), description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def joined(member: discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))


@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
    bot.run(os.environ.get('DISCORD_PRIVATE_KEY'))
