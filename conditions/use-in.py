province = input("What province do you live in? ")
tax = 0

if province in('Rift velley' ,'Western','central'):
    tax = 0.7
elif province == 'Nairobi':
    tax = 0.5
else:
    tax = 0.42
print(tax)