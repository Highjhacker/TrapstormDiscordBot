import requests
from discord.ext import commands


class User:
    BASE_URL_API = "http://www.trapstorm.com/api/v1.0/users"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userid")
    async def user_page_id(self, id):
        r = requests.get(User.BASE_URL_API + "/%s" % id)
        print(r.url)
        await self.bot.say(r.json())

    @commands.command(name="username")
    async def user_page_name(self, nickname):
        r = requests.get(User.BASE_URL_API + "/%s" % nickname)
        await self.bot.say(r.json())

    @commands.command(name="randomuser")
    async def random_user(self):
        r = requests.get(User.BASE_URL_API + "/random")
        await self.bot.say(r.json())


def setup(bot):
    bot.add_cog(User(bot))