country = input('What country do you come from?')
if country.lower() == 'kenya':
    province = input("What province/state do you live in? ")
    if province in('Nairobi',\
        'central', 'Eastern'):
        tax = 0.08
    elif province == 'Mombasa':
        tax = 0.05
    else:
        tax = 0.5
    print(tax)