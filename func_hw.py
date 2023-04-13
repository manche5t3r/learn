#First task
def get_summ(one, two, delemiter='&'):
    one = str(one)
    two = str(two)
    return str(one + delemiter + two)

result = get_summ('Learn', 'python')
print(result.upper())

#Second task
def format_price(price):
    price = int(price)
    return f'Price: {price} rub.'

formated = format_price(56.24)
print(formated)