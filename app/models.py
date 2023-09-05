from config import session
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable= False)
    price = Column(Integer)

    reviews = relationship('Review', back_populates= 'restaurant')
    
    @classmethod    
    def fanciest(cls):
        fanciest_restaurant = max(cls.query.all(), key=lambda restaurant: restaurant.price)
        return fanciest_restaurant
    
    def all_reviews(self):
        return [review.full_review() for review in self.reviews]

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable= False)
    last_name = Column(String, nullable= False)

    reviews = relationship('Review', back_populates= 'customer')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def favorite_restaurant(self):
        sorted_reviews = sorted(self.reviews, key=lambda review: review.star_rating, reverse=True)
        return sorted_reviews[0].restaurant
    
    def add_review(self, restaurant, rating):
        new_review = Review(restaurant = restaurant, customer = self, star_rating = rating)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
        reviews_to_delete = session.query(Review).filter_by(restaurant=restaurant, customer=self).all()
        for review in reviews_to_delete:
            session.delete(review)

        session.commit()
    
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    restaurant = relationship('Restaurant', back_populates= 'reviews')
    customer = relationship('Customer', back_populates= 'reviews')

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars" 
    

                           

    

