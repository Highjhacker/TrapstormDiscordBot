import requests
from discord.ext import commands
import json


class Song:
    BASE_URL_API = "http://www.trapstorm.com/api/v1.0/songs"

    def __init__(self, bot):
        self.bot = bot

    def __repr__(self):
        return '<%r>' % self.name

    @commands.command(name="song")  # maybe pass_context
    async def get_song(self, id):
        try:
            r = requests.get(Song.BASE_URL_API + "/%s" % id)
            r_url = r.json()['address']
            if "soundcloud" in r_url:
                await self.bot.say(r_url)
            else:
                await self.bot.say("https://www.youtube.com/watch?v=" + r_url)
        except json.JSONDecodeError as e:
            print(e)
            await self.bot.say("Impossible de trouver la chanson demandée.")
        except commands.CommandError as e:
            print(e)
            await self.bot.say("Commande erronée, la syntaxe est: song [id].")

    @commands.command(name="randomsong")
    async def get_random_song(self):
        r = requests.get(Song.BASE_URL_API + "/random")
        r_url = r.json()['address']
        if "soundcloud" in r_url:
            await self.bot.say(r_url)
        else:
            await self.bot.say("https://www.youtube.com/watch?v=" + r_url)

    @commands.command(name="tag")
    async def random_song_with_tag(self, tag_name):
        r = requests.get(Song.BASE_URL_API + "/random/%s" % tag_name)
        r_url = r.json()['address']
        if "soundcloud" in r_url:
            await self.bot.say(r_url)
        else:
            await self.bot.say("https://www.youtube.com/watch?v=" + r_url)

    # Implémenter une météhode qui permet d'aller chopper la liste des tags existants sur trapstorm


def setup(bot):
    bot.add_cog(Song(bot))