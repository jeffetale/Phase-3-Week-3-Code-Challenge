from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":

    
    # Import models
    from app.models import Customer  

    # Create a new customer instance
    new_customer = Customer(first_name="John", last_name="Doe")
    new_customer_1 = Customer(first_name="Gib", last_name="Raltar")

    # Add the customer to the session and commit to the database
    session.add(new_customer)
    session.add(new_customer_1)
    session.commit()

    # Verify that the customer has been added
    john_doe = session.query(Customer).filter_by(first_name="John", last_name="Doe").first()
    print(f"New customer ID: {john_doe.id}")
    
    gib_raltar = session.query(Customer).filter_by(first_name="Gib", last_name="Raltar").first()
    print(f"New customer ID: {gib_raltar.id}")
