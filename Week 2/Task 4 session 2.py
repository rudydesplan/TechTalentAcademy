# As an extension to the motorbike task that costs £2000 and loses 10% of its value every year. 
# Set up a function that performs the calculation by passing in parameters.
# Then using a loop, print the value of the bike every following year until it falls below 1000£

original_price = float(input("what is the original price of the motorbike ?"))
loses = float(input("loss of its value every year in pourcentage ")) / 100.0
year = 0.0
price = original_price
age = year
while price > 1000 and age >= 0 :
    print(f"The value of the bike is {price} pounds after {age} years")
    price -= (loses * price)
    age += 1.0
print("the value of the bike has now fallen below 1000 pounds")