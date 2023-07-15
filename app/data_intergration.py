import pickle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .database import Base
from .models import Minerals

# Create the engine and connect to the database
engine = create_engine('sqlite:///app/mineral_ir_data.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create the 'mineral_data' table in the database if it doesn't exists
Base.metadata.create_all(engine)


# Load data from the pickle file
with open('./app/data/processed_data.pkl', 'rb') as f:
    data = pickle.load(f)

# Insert data into the table
for mineral in data:
    m = Minerals(
        id = int(mineral["ID"]),
        r_id = mineral["RRUFFID"],
        name = mineral["NAMES"],
        locality = mineral["LOCALITY"],
        source = mineral["SOURCE"],
        description = mineral["DESCRIPTION"],
        owner = mineral["OWNER"],
        status = mineral["STATUS"],
        url = mineral["URL"],
        csv_path = mineral["CSV_PATH"],
        ideal_chemistry = mineral["IDEAL CHEMISTRY"],
        measured_chemistry = mineral["MEASURED CHEMISTRY"])
    session.add(m)

# # Commit the changes and close the session
session.commit()
session.close()