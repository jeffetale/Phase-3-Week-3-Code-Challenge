from debug import session
from models import Restaurant, Customer, Review

restaurant1 = Restaurant(name='Kwa Mathe', price = '200')
restaurant2 = Restaurant(name= 'KFC', price = '350')

customer1 = Customer(first_name= "John", last_name= "Doe")
customer2 = Customer(first_name= "Mary", last_name= "Jane")

review1 = Review(star_rating= 5, restaurant= restaurant1, customer= customer1)
review2 = Review(star_rating= 3, restaurant= restaurant2, customer= customer2)

session.add(restaurant1)
session.add(restaurant2)
session.add(customer1)
session.add(customer2)
session.add(review1)
session.add(review2)

session.commit()