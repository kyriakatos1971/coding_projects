from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "0d133bc0c59ffc5e7dfa"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL+endpoint
    data = get(url).json()['results']

    data = list(data.items())

    data.sort()

    return data

   # 

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol","")
        print(f"{_id} - {name} - {symbol}")


def exchange_rate(ccy1, ccy2):
    endpoint = f"api/v7/convert?q={ccy1}_{ccy2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL+endpoint
    data = get(url).json()

    

    if len(data)==0:
        print('Invalid currencies.')
        return

    rate =  list(data.values())[0]
    print(f"{ccy1} -> {ccy2} = {rate}")
    return rate



def convertor(currency1, currency2, amount):
    rate = exchange_rate(currency1,currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount")
        return
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")


    




def main():
    #data = get_currencies()
    #print_currencies(data)

    currencies = get_currencies()
    print("Welcome to the online currency converter")
    print("List - lists the available currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Please enter a command (q to quit) ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            baseCurrency = input("Enter a base currency ID: ").upper()
            targetCurrency = input("Enter a target currency ID: ").upper()
            amt = input(f"Enter an amount in {baseCurrency}: ")
            convertor(baseCurrency,targetCurrency,amt)
            #print(converter)
        elif command == "rate":
            baseCurrency = input("Enter a base currency ID: ").upper()
            targetCurrency = input("Enter a target currency ID: ").upper()
            exchange_rate(baseCurrency, targetCurrency)
        else:
            print("Unrecognized command!")




    #rate = exchange_rate("CHF","EUR")
    #print(rate)
    #converter = convertor("CHF", "EUR",100)
    #print(converter)



#Main Call to main()
if __name__ == '__main__':
    main()
