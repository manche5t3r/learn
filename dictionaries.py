from pprint import pprint

product = {
    "name": "iPhone 14",
    "stock": 24,
    "price": 65432.1,
    'country': 'RUS'
}

product['memory'] = 256
product['name'] = 'iPhone 14 Pro'

phones = ['iPhone 14', "Samsung Galaxy S23", 'Xiaomi 13']
product['recomended'] = phones
product['recomended'].append('iPhone 13')

stock = [{'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1,'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
         {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
         {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}]

stock[0]['recomended'].append('OnePlus 11')
stock[1]['price'] = stock[1]['price'] - 14000

print(type(stock))
print(type(stock[0]))
print(type(stock[0]['recomended']))
print(type(stock[0]['recomended'][0]))

regions = {
    'city': 'Moscow',
    'temperature': '20'
}
print(regions)
print(regions['city'])
regions['temperature'] = int(regions['temperature']) - 5
print(regions)
print(regions.get('country'))
print(regions.get('country', 'Russia'))
print(len(regions))

regions['date'] = '27.05.2019'
print(regions)
print(len(regions))