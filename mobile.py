mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
import random
exchange_rate = mobile_data['exchnage_rate']
released_phones = mobile_data['data']

for phone in released_phones:
    brand = phone.get('name')
    price = float(phone.get('price').split()[0]) # could be function ***
    price_in_bdt = round(price * exchange_rate, 2)
    made_in = phone.get('made')

    sentence_one_group = [
        f'{brand} is a feature haevy phone which costs BDT {price_in_bdt} approximately.',
        f'{brand} is a latest technology mobile phone which price is around BDT {price_in_bdt}.',
        f'Newly released {brand} market price is almost BDT {price_in_bdt}.',
    ]
    sentence_two_group = [
        f'This awesome {brand} is manufactured in {made_in}.',
        f'{brand} is made in {made_in}.',
        f'{brand} is built in {made_in}.',
    ]

    sentence_one = random.choice(sentence_one_group)
    sentence_two = random.choice(sentence_two_group)
    content = f'{sentence_one} {sentence_two}'
    print(content)