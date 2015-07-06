from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from puppies import Base, Shelter, Puppy
#from flask.ext.sqlalchemy import SQLAlchemy
from random import randint
import datetime
import random


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()

pups = session.query(Puppy).all()
"""for x in range(len(pups)):
	for pup in pups:
		if pup[x] <= pup[x + 1]:
			print pup.name
		elif pup[x]	> pup[x + 1]:
			pup[x], pup[x + 1] = pup[x + 1], pup[x]
			print pup.name"""

for pup in pups:
	print pup.name
				

