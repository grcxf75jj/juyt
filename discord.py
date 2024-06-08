import http.client
import json
import time

with open('./config.json') as f:
    config_data = json.load(f)
    channel_id = config_data['Config'][0]['channelid']  # config.json
    token = config_data['Config'][0]['token']  # config.json
    message = config_data['Config'][0]['message']  # config.json

header_data = { 
    "Content-Type": "application/json", 
    "User-Agent": "DiscordBot", 
    "Authorization": token  
} 

def get_connection(): 
    return http.client.HTTPSConnection("discord.com", 443) 
