import requests
import json
API_KEY = '3163e4fa-d516-4b57-8756-a35edc552510'
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
PARAMETERS = {
    'start': 1,
    'limit': 10,
    'convert': 'USD'
}
HEADERS = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}
def get_crypto():
    response = requests.get(URL, headers=HEADERS, params=PARAMETERS)
    data = response.json()['data']
    return [{
        'name': currency['name'],
        'symbol': currency['symbol'],
        'price': currency['quote']['USD']['price'],
        'market_cap': currency['quote']['USD']['market_cap']
    } for currency in data]
def search_cryptocurrency(data, search_name):
  search_name = search_name.lower().strip()
  for currency in data:
    if search_name == currency['name'].lower():
      return currency
  return 0
def print_cryptoCur(currency):
    print("––––––––––––––––––––––––––––––––––--")
    print(f"|{currency['name']} ({currency['symbol']})")
    print(f"|Price:\t\t${currency['price']}")
    print(f"|Market_cap:\t{currency['market_cap']}")
    print("––––––––––––––––––––––––––––––––––--\n")
def print_cryptoAll(data):
    for currency in data:
        print_cryptoCur(currency)
def main():
    data = get_crypto()
    while True:
        search = input("\nВведите название криптовалюты || 'all' || 'exit': ")
        if search == "exit":
            break
        elif search == "all":
            print_cryptoAll(data)
        else:
            result = search_cryptocurrency(data, search)
            if result:
                print_cryptoCur(result)
            else:
                print("Криптовалюта не найдена.")
if __name__ == '__main__':
    main()
