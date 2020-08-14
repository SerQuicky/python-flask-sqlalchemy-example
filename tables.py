from app import db
from entities.brand.model import *
from entities.vehicle.model import *

# script for the creation of the tables
# just execute python tables.py once before you test the APIs

if __name__ == "__main__":
    print("Initiating creation of the entity tables")
    print("Wait for the process to finish")
    db.create_all()
    print("Tables were created")
