from twitchio.ext import commands
import os
import serial
class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        serial_port = os.getenv('SERIAL_PORT')  # Get the serial port from environment variable
        self.SerialObj = serial.Serial(serial_port)
        self.SerialObj.baudrate = 9600  # set Baud rate to 9600
        self.SerialObj.bytesize = 8   # Number of data bits = 8
        self.SerialObj.parity  ='N'   # No parity
        self.SerialObj.stopbits = 1   # Number of Stop bits = 1
        super().__init__(token=os.environ['TMI_TOKEN'], prefix=os.environ['BOT_PREFIX'], initial_channels=os.environ['CHANNEL']) 

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def water(self, ctx: commands.Context):
        await ctx.send(f'WATERING THE PLANT, THANKS {ctx.author.name}!')
        self.SerialObj.write(b'A') 
        
        


bot = Bot()
bot.run()