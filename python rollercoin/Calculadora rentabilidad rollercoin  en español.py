import json
import urllib.request

current_hashrate = float(input("introduce tu hashrate (TH/s): "))

network_powers = [float(input("BTC network power (EH/s): ")), float(input("DOGE network power (EH/s): ")), float(input("ETH network power (EH/s): "))]
rewards = [0.00009, 240, 0.0017]
names = ["BTC", "DOGE", "ETH"]

r = urllib.request.urlopen("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cdogecoin%2Cethereum&vs_currencies=usd")
data = json.loads(r.read())
prices = [data["bitcoin"]["usd"], data["dogecoin"]["usd"], data["ethereum"]["usd"]]


current_hashrate /= 1000000

earnings = []
for i, (network_power, reward, price) in enumerate(zip(network_powers, rewards, prices)):
    currency_gain = reward * (current_hashrate / network_power)
    earnings.append(currency_gain * float(price))

max_index = earnings.index(max(earnings))

print("\n---------------------------\n\n{} es el mas rentable\n{}$ per block\n".format(names[max_index], earnings[max_index]))
input("Presiona enter para cerrar")