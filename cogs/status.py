import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from cogs.Fn.function import fncheck,ID
from cogs.Fn.measure import Measure

class status(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    @slash_command(guild_ids=[ID],description='ส่วนเบี่ยงเบนเฉลี่ย ( Mean Deviation )')
    async def status(
        self,
        ctx,
        start: Option(int, "Enter Start",require=True),
        end: Option(int, "Enter End",require=True),
        wide: Option(int, "Enter wide",require=True),
        fi: Option(str, "Enter fi ความถี่ทั้งหมด เช่น 2 3 6 ... 8",require=True),
        chorice : Option(str, "T = Showdata",choices=['True','False'], require=False,default='F')
    ):
        embed = discord.Embed(color=0xFFBFFF, timestamp=discord.utils.utcnow())
        embed.title ='Bot สถิติ >w<'
        try:
            data = Measure(start,end,wide,fi)
            for key in data.keys():     
                if key == "data":
                    key2 = data[key]
                    for x in key2.keys():
                        embed.add_field(name=f'{x}', value=f'`{key2[x]}`', inline=True)
                else:
                    embed.add_field(name=f'{key}', value=f' 📝 `{data[key]}`', inline=False)
        
            embed.set_thumbnail(url=f'https://catalog.dnp.go.th/uploads/group/2023-01-06-024158.523961statistics2.png')
            embed.set_footer(text='🛠️ Dev By Wongsakron', icon_url=f'https://scontent.fbkk4-5.fna.fbcdn.net/v/t39.30808-1/310611601_1530814540749700_4131132864604920634_n.jpg?stp=dst-jpg_p320x320&_nc_cat=101&ccb=1-7&_nc_sid=7206a8&_nc_eui2=AeGr09ba1XwrBsSpwvYRCpKf8zTJrnAmdOLzNMmucCZ04q8eciMzJUTbu9U_2lmb3fDS5679x1yFctDC6wJC9Nwu&_nc_ohc=LEDfbWKhqdAAX-QfSZP&tn=1rTecYflq549wyUo&_nc_ht=scontent.fbkk4-5.fna&oh=00_AfDPjWizSn64SF2JqiZ75RvjIcbwehroOVfhGNort0Yl9Q&oe=63CFE73E')
        except:
            embed = discord.Embed(color=0xFF0000 ,timestamp=discord.utils.utcnow())
            embed.description = 'Player information not found.'       
    
        chorice = fncheck(chorice=chorice)
        await ctx.respond(embed=embed,ephemeral=chorice)
        



def setup(bot):
    bot.add_cog(status(bot))
    