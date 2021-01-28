province = input("What province do you live in? ")
tax = 0

if province == 'Rift velley' or province == 'central':
    tax = 0.7
elif province == 'Nairobi':
    tax = 0.5
else:
    tax = 0.42
print(tax)