province = input("Whats province do you live in?")
tax = 0
if province == 'Rift velley':
    tax = 0.7
elif province == 'Nairobi':
    tax = 0.5
elif province == 'central':
    tax = 0.42
else:
    tax = 0.05
print(tax)