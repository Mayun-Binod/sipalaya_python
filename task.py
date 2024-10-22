# wap to print that takes age as i/p from user and returns their yeas of birth like this " you were born in xyz AD" using f string

from datetime import datetime

current_year = datetime.now().year
age = int(input("Enter your age please: "))
year_of_births= current_year - age
print(f"You were born in {year_of_births} AD")

