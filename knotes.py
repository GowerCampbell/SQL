"Connecting Python and SQL(Structured Query Language)"
"========================="
# Data manipulation and analysis | Used for Managing structured data


# Recall the importance of connecting python for data manipulation and analysis
# Explain the basic concepts of database connectivity in python.
# Implement Pythin scripts to innteract with SQL databases
# Execute SQL quires from python and retrieve data

"Database Connectivity"
# The ability of an application or software system to establish a connection
# and interact with a database mangement system (DBMS)
# Operations: daya retrieval, insertion update and deletion

'Data Access'
# Enables applications to acces and retrieve databases crucial for data driven
# applications.
# Application layer
# Database Driver
# Database management system

'Data Manupulation'
# Database connectivity, applications can manipulate daya within the
# database

'REal-Time Updates'
# To reflect the changes in the underlying data for data-driven applications

'Scalability'
# Scale to handle increasing data volumes and user loads
# Being resources friendly to limit the information using normallised
# database. On current or lock tables as you can't log in 

'Security'
# Database connectivity allows applications to implement secuirity measures 
# such as authentication, encryption and authorisation of data available

'Integration'
# Enables seamless sharing of multiple data sources to anaylyse/retrieve
# from other databases

'Performance Optimisation'
# Executing queries directly on the database server, leveraging the database
# processing power and indexing capabilities as users can share their connection


'Benefits'
# Python is a compelling choice for building database-driven application
# across a wide range range of domains and industries

# Ease of use
# Extensive libary support
# Ingreation in machine learning
# Strong cross comunity platform
# Rapid development capabiliies

"DATABASE INTERACTION: SQLite"
# Lightweight, self-contained in one one fule for SQL database engine.
# Used for small scale projects

# - Zero Configuration: Self-Contained
# - Single File: Ease of distribution
# - SQL Support: Compatable with SQL Syntax

"DATABASE INTERACTION: SQLAlchemy"
# Idle for abstraction as we can just say ADD USER to connect and different
# applications to be used in the 
# Imparative code language as we mimic a declaratife approach as if to tell a
# story to make it a high level interface with interacting with SQL databases
# abastracting away many of the complexities. Its a level of declartive 
# as it uses object relational mapping (ORM) Libary. Using python classes
# to create tables such as when we import tableu module
'Key fearures'
# Enables seamless interaction to define database models
# Allows us to construct SQL quiries and makes it easier to write complex quiries
# Cross Database Compatability SQL Alchemy supports multiple SQL database
# engines allowing applications to switch between different databases.

# To use SQLAlchemy you install it using pip install sqakchemy

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

"Structured Query Language"
# Composed of commands to create databases or table structures

'Data Definition Language (DDL)'
# Defines databases
# Defines Views\
# Defines access rights

'Data Manipulation Language (DML)'
# Insert
# Update
# Delete
# SELECT

'Important Keywords'
# CREATE TABLE
# NOT NULL: Ensures that column doesnt contain null
# UNIQUE: Ensures that there are no repetitions
# PRIMARY KEY: Defines a primary key
# FOREIGN KEY: Defines a Foreign Key
# DROP TABLE: Deletes a table entirely

#  CREATE TABLE table_name(
# column1_name datatype constraints,
# column1_name datatype constraints,
# ...
#)

'Retrieving Data'
# Using the SELECT to retreieve data

# SELECT * FROM employes 
# to select all columns

# Toselect a specfic columns
# SELECT specific columns 


'SQL: Ordering Data'
# Know when we use the ORDER BY 
# Default is ORDER BY ACSENDING or DESCENDING ORDER
# 
# Sorting criteria

'Modifying Data'
# Using UPDATE table_name
# SET column1 =value 1
# where condition

'Removing Records'
# USING THE DELETE statement to remove to existing so add a condition
# to not delete table

# DELETE FROM 

"SQL SPECIAL OPERATIONS"

# BETWEEN: Checks if a value wothin ranges and age and salary to give 
# and find

# Example: 

# NULL: Good for data clean up 

# LIKE: TO check if anything matches to find a given pattern

# IN: Checks if a value is in a given list, creating a list to give it
# some names in the return as long as its in the list to retirn records with
# multiple values

# EXISTS: Checks if a query returns any rows, is it in there 
# and if it doesnt

# DISTINCT: Limits unique values 

# If you DELETE will never you give me an error and by using EXIST and if the 
# value comes back then DELETE and if it returns then their is an error message
# Giving better feedback 

'Aggregate Functions'

# COUNT:
# MIN:
# MAX:
# AVG:

'Accessing Multiple Tables'
# INNER JOIN: Records match in both tables
# LEFT JOIN: All values in A and matching values in B
# FULL OUTER JOIN: All Values in both tables



'SQL Removing Tables'
# DROP TABLE (Table no longer exists)

'SQLite vs SQL'
# Can be expressed in many ways
# Like 'UK' English vs. "US" English

'SQLITE'
# Native to python
# Self-contained
# ACID 
# Transactional
# Ensureces daya integrity
# Severless
# Easy to port

# import sqlite3

# db = sqlite3.connect('data/sudent_db')
# cursor = db.cursor()

# cursor.execute("
#                CREATE TABLE student(id INTEGER PRIMARY KEY, name TEXT
#                                     grade INTEGER
# )")

# db.commit

# Using "cursor.execute" to keep inserting information example:
# ("INSERT INTO student(name, grade)
# VALUES(?,?)", (name1,grade1))

# dbcommit()

students_ = [(name1,grade1),(name2,grade2),(name3,grade3)] # Tuple (requirement)
# cursor.executemany("INSERT INTO student(name,grade)VALUES(?,?)", student_)
# executemany is an insert that will keep running for every.... because
# Also to avoid naming conflicts we added student_ 

# AUTOINCREMENT
# REAL
# INSERT OR REPLACE: If it exists as you retrieve and then replace into or 
# merge into together so it overrwrites

# If i have a moderater so I need to prove so you need a statement that is 
# an additional record to prove to you. As you must remember that inside the 
# curoser ("SELECT * FROM employee")

# The above is more efficient as the rows will be loaded into memory

