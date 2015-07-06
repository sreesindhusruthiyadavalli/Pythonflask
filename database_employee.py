import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#Class 
class Employee(Base):
	#table
	__tablename__ = 'employee'

	#Mapper
	name = Column(String(250), nullable = False)
	id = Column(Integer, primary_key = True)



class Address(Base):
	__tablename__ = 'address'


	street = Column(String(80), nullable = False)
	Zip = Column(String, nullable = False)
	employee_id = Column(Integer, ForeignKey('employee.id'))

	employee = relationship(Employee)



engine = create_engine('sqlite:///employeeData.db')

Base.metadata.create_all(engine)