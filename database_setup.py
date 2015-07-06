import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


#CLass code

class Restaurant(Base):
	#Table representation
	__tablename__ = 'restaurant'

	#Mapper
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)

	@property 
	def serialize(self):
		return {
            	'name': self.name,
            	'id': self.id,
        	}


class MenuItem(Base):
	#Table representation
	__tablename__ = 'menu_item'

	#Mapper
	name = Column(Integer, nullable = False)
	id = Column(Integer, primary_key = True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

	restaurant = relationship(Restaurant)
	
	@property
	def serialize(self):
		return {
	            'name': self.name,
	            'description': self.description,
	            'id': self.id,
	            'price': self.price,
	            'course': self.course,
	        }




######End of file######################################
engine = create_engine('sqlite:///restaurant.db')

Base.metadata.create_all(engine)

