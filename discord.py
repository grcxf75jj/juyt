import http.client
import json
import time

with open('./config.json') as f:
    config_data = json.load(f)
    token = config_data['Config'][0]['token']  # config.json

header_data = { 
    "Content-Type": "application/json", 
    "User-Agent": "DiscordBot", 
    "Authorization": token  
} 

def get_connection(): 
    return http.client.HTTPSConnection("discord.com", 443) 
