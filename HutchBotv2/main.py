# imports
import discord
from discord.ext import commands, tasks
import datetime


intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.reactions = True
intents.members = True

# creates an instance of the bot with a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

custom_dates = []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await send_ping_at_custom_date.start()

@bot.event
async def on_command_error(ctx, error):
    print(f"Error in command '{ctx.command}': {error}")

@tasks.loop(hours=24)  # adjust the interval based on your needs
async def send_ping_at_custom_date():
    now = datetime.datetime.now()
    
    for date in custom_dates:
        if now.day == date['day'] and now.hour == date['hour'] and now.minute == date['minute']:
            guild = bot.guilds[0]  # assuming the bot is in only one guild
            channel = guild.get_channel(YOUR_CHANNEL_ID)  # replace YOUR_CHANNEL_ID with your channel ID

            await channel.send("@everyone Custom ping at a custom date!")

@bot.command(name='holidaymessage', help='Sends a specific message during holidays.')
async def holiday_message(ctx):
    now = datetime.datetime.now()
    
    for date in custom_dates:
        if now.day == date['day']:
            await ctx.send("Happy Holidays! 🎄🎉")  # customize the holiday message as needed
            return
    
    await ctx.send("No special holiday message today.")

@bot.command(name='addcustomdate', help='Adds a custom date for special messages.')
async def add_custom_date(ctx, day: int = 1, hour: int = 0, minute: int = 0):
    try:
        # create a new datetime object based on the provided parameters
        custom_date = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, day, hour, minute)
    except ValueError:
        await ctx.send("Invalid date. Please provide a valid date.")
        return

    # add the custom date to the list
    custom_dates.append({'day': day, 'hour': hour, 'minute': minute})
    await ctx.send(f"Custom date {day}/{datetime.datetime.now().month}/{datetime.datetime.now().year} {hour}:{minute} added.")

# function to remove the "Part of the herd role" if "Calf" is added
@bot.event
async def on_member_update(before, after):
    role1 = discord.utils.get(after.guild.roles, name="Part of the herd")
    role2 = discord.utils.get(after.guild.roles, name="Calf")

    if role2 in after.roles and role1 in before.roles:
        await after.remove_roles(role1)

# function to test the bot's functionality
@bot.command(name='beep', help='Responds with "boop".')
async def beep(ctx):
    print('Command executed: beep')
    await ctx.send('boop')

# token
bot.run('MTE3NzI2NDIyMjQ1MTgwNjMxOQ.GZUXlX.hHq3dazKmX0wTcTyW158PfkkMSM5oo4qizHuB8')