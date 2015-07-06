from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurant.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
myFirstRestaurant = Restaurant(name = "Piazza palace")
session.add(myFirstRestaurant) 
session.commit()


session.query(Restaurant).all()

cheesepiazza = MenuItem(name = "Cheese Piazza", course = "Entree", description = "Made with all natural ingredients",
						price = "$8.99", restaurant = myFirstRestaurant)
session.add(cheesepiazza) 
session.commit()

session.query(MenuItem).all()


firstresult = session.query(Restaurant).first()
firstresult.name	

items = session.query(MenuItem).all()
for item in items:
	print item

veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for vg in veggieBurgers:
   print vg.id	
   print vg.price
   print vg.restaurant.name
   print "\n"

UrbanVeggieBurger =  session.query(MenuItem).filter_by(id = 8).one()  
print UrbanVeggieBurger.price

UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()


#Delete
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print spinach.restaurant.name
session.delete(spinach)
session.commit()
