# A motorbike costs £2000 and loses 10% of its value every year. 
# Using a loop, print the value of the bike every following year until it falls below 1000£

original_price = 2000.0
year = 0.0
price = original_price
age = year
while price > 1000 and age >= 0 :
    print(f"The value of the bike is {price} pounds after {age} years")
    price -= (0.1 * price)
    age += 1.0
print("the value of the bike has now fallen below 1000 pounds")
