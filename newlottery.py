import random

a = []

for i in range(6):
    n = int(input("Enter number (1-50): "))

    if (n>50 or n<1): 
         print("Enter numbers betweeen 1 and 50")
    else:
      a.append(n)

    

draws = random.sample(range(1, 51), 6)

print("Your numbers:", a)
print("Winning numbers", draws)

matches = set(a) & set(draws)
number = len(matches)

if number == 6:
    print("Congrats, you won!")
else: 
    print("Try Again")



