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

def main():
	distro = pobierz_distro()
	kernel = pobierz_kernel()
	uptime = pobierz_uptime()
	ram = pobierz_ram()
	cpu = pobierz_cpu()
	shell = pobierz_shell()

	print(f"distro: {distro}")
	print(f"kernel: {kernel}")
	print(f"uptime {uptime}")
	print(f"ram {ram}")
	print(f"cpu {cpu}")
	print(f"shell {shell}")




main()


