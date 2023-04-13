price = 100
discount = 5

def discounted(price, discount, max_discount=20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Max discount can\'t be more than 100')
    if discount >= max_discount:
        price_with_discounted = price
    else:
        price_with_discounted = price - price * discount / 100
    return price_with_discounted

print(discounted(100,5))
print(discounted(100,50))
print(discounted(100,50, max_discount=60))

product = {'name': 'iPhone 14 Pro', 'price': 99000.0, 'discount': 20}
product['with_discount'] = discounted(product['price'], product['discount'])
print(product)