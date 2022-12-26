import requests, os

def Fivem():
    req = requests.get("https://runtime.fivem.net/client/FiveM.exe", allow_redirects=True)
    open("FiveM.exe", "wb").write(req.content)

def Discord():
    req = requests.get("https://dl.discordapp.net/distro/app/stable/win/x86/1.0.9008/DiscordSetup.exe", allow_redirects=True)
    open("DiscordSetup.exe", "wb").write(req.content)

def Firefox():
    req = requests.get("https://cdn.stubdownloader.services.mozilla.com/builds/firefox-stub/ar/win/60dbabd81bd85d2e1c66aa3bab7d7e3479f27399e2e1551a459d5c55590739d7/Firefox%20Installer.exe", allow_redirects=True)
    open("Firefox Installer.exe", "wb").write(req.content)

def Valorant():
    req = requests.get("https://valorant.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.live.ap.exe", allow_redirects=True)
    open("live.live.ap.exe", "wb").write(req.content)

def Revo_Uninstaller():
    req = requests.get("https://cdn.discordapp.com/attachments/1052940646693994498/1052941688290672670/revosetup.exe", allow_redirects=True)
    open("revosetup.exe", "wb").write(req.content)

def zip():
    req = requests.get("https://cdn.discordapp.com/attachments/1052940646693994498/1052941612642209854/7z2201-x64.exe", allow_redirects=True)
    open("7z2201-x64.exe", "wb").write(req.content)

def logo():
    os.system("title Downloader 1.0")

print("""\n        ███╗░░██╗░█████╗░░█████╗░████████╗░░░██╗░██╗░░█████╗░███████╗░░███╗░░███████╗
        ████╗░██║██╔══██╗██╔══██╗╚══██╔══╝██████████╗██╔══██╗██╔════╝░████║░░██╔════╝
        ██╔██╗██║██║░░██║██║░░██║░░░██║░░░╚═██╔═██╔═╝██║░░██║██████╗░██╔██║░░██████╗░
        ██║╚████║██║░░██║██║░░██║░░░██║░░░██████████╗██║░░██║╚════██╗╚═╝██║░░╚════██╗
        ██║░╚███║╚█████╔╝╚█████╔╝░░░██║░░░╚██╔═██╔══╝╚█████╔╝██████╔╝███████╗██████╔╝
        ╚═╝░░╚══╝░╚════╝░░╚════╝░░░░╚═╝░░░░╚═╝░╚═╝░░░░╚════╝░╚═════╝░╚══════╝╚═════╝░\n\n""")

def Main():
    logo()
    op = input(f"Welcome : {os.getlogin()}\n1.Download Fivem\n2.Download Discord\n3.Download Firefox\n4.Download Valorant\n5.Download Revo Uninstaller\n6.Download 7zip\n")
    if op == "1":
        Fivem()
    elif op == "2":
        Discord()
    elif op == "3":
        Firefox()
    elif op == "4":
        Valorant()
    elif op == "5":
        Revo_Uninstaller()
    elif op == "6":
        zip()

Main()
