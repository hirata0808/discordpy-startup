from os import getenv
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 531871814176210944:
        txtRoom = client.get_channel(531871814176210948)
        if before.channel is None:
            msg = f'**{member.name}**さんが **かおす** に参加しましたけど...'
            await txtRoom.send(msg)


@client.event
async def on_message(message):
    if message.content.startswith("ありがとねぇ"):
        m = "どういたしまして...ですけど..."
        await message.channel.send(m)

    if message.content.startswith("やあ"):
        await message.channel.send("こんにちは...ですけど")


token = getenv('DISCORD_BOT_TOKEN')
client.run(token)
