# Conditional Statements
season = 'spring'
if season == 'win':
    print('win')
elif season == 'test':
    print('test')
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')

phone_balance = 10
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

# Boolean Expressions


# For and While Loops
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")

for i in range(3):
    print(i)
print('done!')

print(list(range(0,-5)))

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = {}

for word in book_title:
   word_counter[word] = word_counter.get(word,0)+1
print(word_counter)


for key, value in word_counter.items():
    print('{}:{}'.format(key,value))



# Break and Continue


# Zip and Enumerate


# List Comprehensions