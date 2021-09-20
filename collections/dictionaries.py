

catalog = {}
catalog['John'] = '6990567345'
catalog['Nick'] = '6910671234'
catalog['Tom'] = '6710909876'

catalog2 = {
    'John': '6990567345',
    'Nick': '6910671234',
    'Tom': '6710909876'
}

for key in catalog:
    print(key, catalog[key])

if 'Peter' in catalog:
    print(catalog['Peter'])
else:
    print('Peter not in catalog')
