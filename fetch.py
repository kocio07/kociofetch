blue = "\033[34m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
purple = "\033[35m"
cyan = "\033[36m"
bold = "\033[1m"
reset = "\033[0m"
logo = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡖⠒⠲⠶⢤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣀⣀⣀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢷⡀⠀⠀⠀⠀⠉⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣤⣄⠀
⠀⣰⡿⠟⠛⠋⠉⠉⠉⠉⠉⠉⠙⠛⠛⠛⠻⠶⣶⣦⣤⣿⣦⡀⠀⠀⠀⠀⠈⠻⣦⣀⢀⣀⣀⣤⣴⠶⠾⠿⠟⠛⠛⠉⠉⠁⠀⠀⠙⡇
⣸⣏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠾⠛⠋⠁⢀⡀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇
⠘⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀
⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀
⠀⠀⠈⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡶⠾⠷⣶⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠛⠻⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀
⠀⠀⠀⠀⠘⠷⣤⡀⠀⠀⠀⠀⣰⡿⠋⢀⣴⡟⠛⣧⠀⠀⠀⠀⠀⠀⠀⠈⣱⡟⠻⣦⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⢀⣾⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠿⣶⣄⠀⣼⡟⠂⠀⢸⡟⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠸⡇⠀⠀⢻⣆⠀⠀⠀⢀⣀⣶⣟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⢺⣟⠒⠶⠶⣤⡄⠀⣿⠀⠀⠀⢺⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⢠⣷⠀⠀⠀⢻⡜⠛⠛⠉⠉⠉⣽⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠷⣤⡀⠀⠀⠀⣿⡀⠀⠀⠀⢻⣄⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⣤⡾⠁⠀⠀⠀⢸⡇⠀⠀⠀⣠⡾⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⢻⡇⠀⢀⣈⡀⠀⠀⠀⠀⠉⠉⠀⠀⠚⠚⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠀⣀⡀⠀⢰⣞⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⠁⠛⠋⠿⠷⠀⠀⠀⠀⠀⠀⠀⢀⠀⣀⣀⣀⡀⣠⡀⠀⠀⠀⠀⠘⠻⠿⠿⠉⠀⠀⠀⠙⢿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⢿⣌⠉⠉⢹⡇⠀⠀⠀⠀⠀⠀⠀⢀⣄⣀⣀⣀⣀⣀⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠋⠙⠻⣦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠙⢷⣤⣼⠃⠀⠀⢀⣀⣠⣤⡶⠟⠋⠉⠋⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣟⠛⠛⠛⠛⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⢶⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
linie_logo = logo.strip("\n").split("\n")
szerekosc = max(len(linia) for linia in linie_logo) + 2


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
	plik.close()
	uzyty_gb = (total - avalible) / 1024 /1024
	total_gb = total / 1024 / 1024
	return f"{uzyty_gb:.1f}GB / {total_gb:.1f}GB"

def pobierz_cpu():
	plik = open("/proc/cpuinfo", "r")
	for linia in plik:
		if linia.startswith("model name"):
			plik.close()
			return linia.split(":")[1].strip()
	plik.close()
	return "Nieznany CPU"

def pobierz_baterie():
	plik = open("/proc/cpuinfo", "r")






def main():
	distro = pobierz_distro()
	kernel = pobierz_kernel()
	uptime = pobierz_uptime()
	ram = pobierz_ram()
	cpu = pobierz_cpu()
	shell = pobierz_shell()
	info = [
		f"{blue}distro:{reset} {distro}",
		f"{red}kernel:{reset} {kernel}",
		f"{green}uptime:{reset} {uptime}",
		f"{yellow}ram:{reset} {ram}",
		f"{purple}cpu: {reset} {cpu}",
		f"{cyan}shell: {reset} {shell}",
	]
	
	for i in range(max(len(linie_logo), len(info))):
		lewa = linie_logo[i] if i < len(linie_logo) else ""
		prawa = info[i] if i < len(info) else ""
		print(f"{lewa:<{szerekosc}}{prawa}")

main()




