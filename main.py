
d ={
"name": 'Иван',
"mid_name": 'Иванов',
"balance": 10000
}



def f(x):
    return x**2


text = f"""Дорогой {d['name']} {d['mid_name']}, баланс вашего лицевого счета
составляет {d.get('balance')} $"""

print(text)