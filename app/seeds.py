'''
from app.debug import session
from models import Restaurant, Customer, Review


restaurant1 = Restaurant(name='Kwa Mathe', price = '200')
restaurant2 = Restaurant(name= 'KFC', price = '350')

customer1 = Customer(first_name= "John", last_name= "Doe")
customer2 = Customer(first_name= "Mary", last_name= "Jane")
customer3 = Customer(first_name= "Wraith", last_name= "Valkyrie")

review1 = Review(star_rating= 5, restaurant= restaurant1, customer= customer1)
review2 = Review(star_rating= 3, restaurant= restaurant2, customer= customer2)

print("Sample Restaurants:")
print(restaurant1.__dict__)  # Print the attributes of restaurant1
print(restaurant2.__dict__)  # Print the attributes of restaurant2

print("\nSample Customers:")
print(customer1.__dict__)  # Print the attributes of customer1
print(customer2.__dict__)  # Print the attributes of customer2
print(customer3.__dict__)  # Print the attributes of customer2

print("\nSample Reviews:")
print(review1.__dict__)  # Print the attributes of review1
print(review2.__dict__)  # Print the attributes of review2

session.add(restaurant1)
session.add(restaurant2)
session.add(customer1)
session.add(customer2)
session.add(customer3)
session.add(review1)
session.add(review2)

session.commit()

'''