def pobierz_distro():
    plik = open("/etc/os-release", "r")
    for linia in plik:
        if linia.startswith("PRETTY_NAME"):
            wartosc = linia.split("=")[1]
            wartosc = wartosc.strip().strip('"')
            plik.close()
            return wartosc
    plik.close()
    return "Nie mozna odczytac info"
    


import platform
import os

def pobierz_kernel():
    return platform.release()

def pobierz_shell():
    return os.environ.get("SHELL", "nieznany")

def pobierz_uptime():
    plik = open("/proc/uptime", "r")
    tresc = plik.read()
    plik.close()
    sekundy = float(tresc.split()[0])
    godziny = int(sekundy // 3600)
    minuty = int((sekundy % 3600) // 60)
    return f"{godziny}h {minuty}m"

def pobierz_ram():
    total = 0 
    avalible = 0
    plik = open("/proc/meminfo", "r")
    for linia in plik:
        if linia.startswith("MemTotal"):
            total = int(linia.split()[1]) 
        if linia.startswith("MemAvailable"):
            avalible = int(linia.split()[1])
    
