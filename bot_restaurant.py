import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, I am a bot from the Universe restaurant {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def menu(ctx):
    await ctx.send(f"""
-Starters

Galactic Greens: Fresh salad with interstellar veggies and stardust vinaigrette.
Cosmic Soup: Creamy tomato soup with planet-shaped croutons.

-Main Courses

Asteroid Burger: Juicy beef patty with cosmic cheddar, served with meteorite fries.
Lunar Pasta: Fettuccine in a creamy mushroom sauce with rocket parmesan.
Nebula Veggie Bowl: Quinoa, roasted vegetables, and galaxy-glazed tofu.

-Desserts

Milky Way Cake: Chocolate cake with a starry vanilla swirl.
Planetary Sorbet: Assorted fruit sorbets resembling mini planets.

-Drinks

Supernova Smoothie: Mixed berries with a sparkling twist.
Rocket Fuel Latte: Espresso with a hint of cinnamon and caramel.
Starlight Soda: Refreshing lemon-lime soda with shimmering edible glitter.""")

@bot.command()
async def goodbye(ctx):
    await ctx.send(f"Goodbye dear client. Hope to see you again at the Universe!")

@bot.command()
async def instructions(ctx):
    await ctx.send("""
Welcome to the Universe Bot! Here's how you can interact with me:

1. **#hello** - Say hello to the bot.
2. **#menu** - View our restaurant's menu.
3. **#dessert_choice** - Let me suggest a dessert for you.
4. **#goodbye** - Say goodbye and get a farewell message.

Use these commands to explore and enjoy our services!
""")

@bot.command()
async def dessert_choice(ctx):
    desserts = ["Milky Way Cake", "Planetary Sorbet"]
    choice = random.choice(desserts)
    await ctx.send(f"My suggestion for dessert is: {choice}!")


@bot.command()
async def fortune(ctx):
    fortunes = [
        "You will have a stellar day today!",
        "Beware of meteorites in your path.",
        "An intergalactic adventure is on your horizon.",
        "Your cosmic energy is radiating good vibes!",
        "Today is a great day to try something new from the menu!"
    ]
    chosen_fortune = random.choice(fortunes)
    await ctx.send(f"🔮 Your fortune: {chosen_fortune}")


bot.run("MTMxMDI2MDA4NDUwMDA3MDQ5MQ.GuGLTP.0X99om2Vqsxk10KCnyAHGCFr0NzYqz5PtJl-8w")
