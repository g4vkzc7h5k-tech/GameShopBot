import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")

OWNER_ID = 473186764178194432

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=",",
    intents=intents
)


class ShopDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Create Order",
                emoji="🛒",
                description="Create a new order"
            ),
        ]

        super().__init__(
            placeholder="Choose an option...",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Create Order":
            await interaction.response.send_message(
                "🛒 Order system is coming soon!",
                ephemeral=True
            )


class ShopView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ShopDropdown())


@bot.event
async def on_ready():
    print(f"{bot.user} is online!")


@bot.command()
async def sendshop(ctx):

    if ctx.author.id != OWNER_ID:
        return

    embed = discord.Embed(
        title="🛒 GameShop",
        description=(
            "Welcome to GameShop!\n\n"
            "Use the dropdown menu below to start your order."
        ),
        color=0x5865F2
    )

    embed.set_footer(
        text="GameShop • Digital Store"
    )

    await ctx.send(
        embed=embed,
        view=ShopView()
    )


bot.run(TOKEN)
