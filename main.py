from config import *

if __name__ == "__main__":

    # Import models
    from app.models import Restaurant, Customer, Review

    # New customer instance
    new_customer = Customer(first_name="John", last_name="Doe")
    new_customer_1 = Customer(first_name="Gib", last_name="Raltar")
    new_customer_2 = Customer(first_name="Wraith", last_name="Valkyrie")

    #New restaurant instance
    restaurant1 = Restaurant(name='Kwa Mathe', price = '200')
    restaurant2 = Restaurant(name= 'KFC', price = '350')
    restaurant3 = Restaurant(name= 'Kibandaski', price = '50')
    
    #New review instance
    review1 = Review(star_rating= 4, restaurant= restaurant1, customer= new_customer)
    review2 = Review(star_rating= 3, restaurant= restaurant2, customer= new_customer_1)
    review3 = Review(star_rating= 10, restaurant= restaurant3, customer= new_customer)

    # Add the customer, restaurants and reviews to the session and commit to the database
    session.add(new_customer)
    session.add(new_customer_1)
    session.add(new_customer_2)
    session.add(restaurant1)
    session.add(restaurant2)
    session.add(restaurant3)
    session.add(review1)
    session.add(review2)
    session.add(review3)
    session.commit()

    # Testing out my models and the database
    john_doe = session.query(Customer).filter_by(first_name="John", last_name="Doe").first()
    print(f"New customer ID: {john_doe.id}")
    
    gib_raltar = session.query(Customer).filter_by(first_name="Gib", last_name="Raltar").first()
    print(f"New customer ID: {gib_raltar.id}")

    print(f"John Doe's full name: {john_doe.full_name()}")
    print(f"Gib Raltar's full name: {gib_raltar.full_name()}")

    favorite_restaurant = john_doe.favorite_restaurant()
    print(f"{john_doe.full_name()}'s favorite restaurant: {favorite_restaurant.name}")

    # Delete reviews for a restaurant
    john_doe.delete_reviews(restaurant1)

