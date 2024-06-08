import discord

# Inisialisasi klien Discord
client = discord.Client()

@client.event
async def on_message(message):
    # Cek apakah pesan yang diterima adalah dari pengguna (bukan dari bot)
    if message.author != client.user:
        # Cek apakah pesan mengandung kata kunci tertentu
        if "halo" in message.content.lower():
            # Balas dengan pesan tertentu
            await message.channel.send("Halo! Apa kabar?")

# Token bot Discord Anda
TOKEN = 'your_bot_token_here'

# Jalankan klien Discord
client.run(TOKEN)
