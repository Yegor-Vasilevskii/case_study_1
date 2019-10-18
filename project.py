import requests
print ("Введите из какой валюты будем переводить", end='\n')
a = input('')
print("Введите в какую валюту необходимо перевести", end='\n')
b = input('')
print("Введите сумму", end='\n')
summa = float(input(''))
if a == "RUB":
    if b == 'USD':
        RUB_to_USD = requests.get ('https://api.exchangerate-api.com/v4/latest/RUB').json()['rates']['USD']
        s_1 = RUB_to_USD * summa
      print(s_1)
    else:
        RUB_to_EUR = requests.get ('https://api.exchangerate-api.com/v4/latest/RUB').json()['rates']['EUR']
        s_2 = RUB_to_EUR * summa
      print(s_2)
else:
    if b == 'USD':
        KZT_to_USD = requests.get ('https://api.exchangerate-api.com/v4/latest/KZT').json()['rates']['USD']
        s_3 = KZT_to_USD * summa
      print(s_3)
    else:
        KZT_to_EUR = requests.get ('https://api.exchangerate-api.com/v4/latest/KZT').json()['rates']['EUR']
        s_4 = KZT_to_EUR * summa
      print(s_4)
pass