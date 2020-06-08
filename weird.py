from discord.ext import commands, tasks
from random import choices

bot = commands.Bot(command_prefix='weird ')
token = ""
messages = []
string = "!\"#$%&'()********************+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^____________________abcdefghijklmnopqrstuvwxyz{}~~~~~~~~~~"
is_spoiler = []


@bot.event
async def on_ready():
    print("time to go crazy")
    edit.start()


@bot.command()
async def send(ctx):
    messages.append(await ctx.send('great things will happen to this message'))


@tasks.loop(seconds=1)
async def edit():
    if is_spoiler:
        for message in messages:
            await message.edit(content=f"||{message.content}||")
        is_spoiler.clear()
    else:
        for message in messages:
            await message.edit(content=f'\n{"".join(choices(string, k=200))}')
        is_spoiler.append('')


bot.run(token)
