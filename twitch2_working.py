from twitchio.ext import commands
import os
import serial
import time
class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...

        super().__init__(token=os.environ['TMI_TOKEN'], prefix=os.environ['BOT_PREFIX'], initial_channels=[os.environ['CHANNEL']]) 

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def water(self, ctx: commands.Context):
        await ctx.send(f'WATERING THE PLANT, THANKS {ctx.author.name}!')
        self.SerialObj.write(b'A') 
        
        


bot = Bot()
bot.run()