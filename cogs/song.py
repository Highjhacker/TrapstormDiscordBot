import requests
from discord.ext import commands


class Song:
    BASE_URL_API = "http://www.trapstorm.com/api/v1.0/songs"

    def __init__(self, bot):
        self.bot = bot

    def __repr__(self):
        return '<%r>' % self.name

    @commands.command(name="song")  # maybe pass_context
    async def get_song(self, id):
        r = requests.get(Song.BASE_URL_API + "/%s" % id)
        r_url = r.json()['address']
        if "soundcloud" in r_url:
            await self.bot.say(r_url)
        else:
            await self.bot.say("https://www.youtube.com/watch?v=" + r_url)

    @commands.command(name="randomsong")
    async def get_random_song(self):
        r = requests.get(Song.BASE_URL_API + "/random")
        r_url = r.json()['address']
        if "soundcloud" in r_url:
            await self.bot.say(r_url)
        else:
            await self.bot.say("https://www.youtube.com/watch?v=" + r_url)

    @commands.command(name="randomwithtag")
    async def random_song_with_tag(self, tag_name):
        r = requests.get(Song.BASE_URL_API + "/random/%s" % tag_name)
        r_url = r.json()['address']
        if "soundcloud" in r_url:
            await self.bot.say(r_url)
        else:
            await self.bot.say("https://www.youtube.com/watch?v=" + r_url)


def setup(bot):
    bot.add_cog(Song(bot))