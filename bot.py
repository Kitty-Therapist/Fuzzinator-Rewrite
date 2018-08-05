import asyncio
import datetime
import time

import discord
import configparser
import sys
import os
import traceback
from pathlib import Path
from discord.ext import commands
from discord import abc
from cryptography.fernet import Fernet

# Checking Configs Exist
if not os.path.exists('config'):
    os.makedirs('config')
    
config_file = Path('config.ini')
if config_file.exists() is not True:
    sys.exit("I'm sorry, but I couldn't find your config file. Make sure to copy the config.ini.example as config.ini and insert your settings.")

# Parsing the Config
config = configparser.ConfigParser()
config.read('config.ini')

#Load in AES Key
try:
    print("Loading AES-Key")
    keyFile = open('encryption_key.txt', 'r')
except:
    print("No stored AES-Key was found. Generating a new key.")
    newKeyFile = open('encryption_key.txt', 'w')
    newKeyFile.write("This file is used to store the encryption key for end user Data in the DB. Do not edit or remove this file as this would make your stored data forever useless.\n")
    newKeyFile.write("----- Start of the AES-Key -----\n")
    newKeyFile.write(Fernet.generate_key().decode() + "\n")
    newKeyFile.write("-----  End of the AES-key  -----")
    newKeyFile.close()
    keyFile = open('encryption_key.txt', 'r')

key = str.encode(keyFile.readlines()[2])
keyFile.close()

#DB Magic
async def db_setup():
    connection = await asyncpg.connect(host=config['Credentials']['host'], user=config['Credentials']['user'], password=config['Credentials']['password'], database=config['Credentials']['database'])
    await connection.execute('''CREATE TABLE IF NOT EXISTS permissions(
                                role_id VARCHAR(25) NOT NULL,
                                permission TEXT NOT NULL,
                                ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT) 
                                COLLATE utf8mb4_unicode_ci;''')
    #To Be Continued                         
