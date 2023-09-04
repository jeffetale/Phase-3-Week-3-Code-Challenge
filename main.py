from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI


engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    from app.models import Customer  # Import your models

    # Create a new customer instance
    new_customer = Customer(first_name="John", last_name="Doe")

    # Add the customer to the session and commit to the database
    session.add(new_customer)
    session.commit()

    # Verify that the customer has been added
    john_doe = session.query(Customer).filter_by(first_name="John", last_name="Doe").first()
    print(f"New customer ID: {john_doe.id}")
