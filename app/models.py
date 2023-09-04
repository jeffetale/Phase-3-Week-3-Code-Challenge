from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship('Review', back_populates= 'restaurant')
                           
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates= 'customer')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey=True)
    customer_id = Column(Integer, ForeignKey=True)

    restaurant = relationship('Restaurant', back_populates= 'reviews')
    customer = relationship('Customer', back_populates= 'reviews')

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars" 
    

                           

    

