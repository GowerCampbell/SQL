"""
Connecting Python and SQL (Structured Query Language)
====================================================
This script demonstrates how to connect Python with SQL databases, execute queries, 
and retrieve data using SQLite and SQLAlchemy.

SQL (Structured Query Language) is a powerful tool for managing and manipulating relational databases.
This script covers:
- Database connectivity
- Executing SQL queries from Python
- Using SQLite (lightweight database) and SQLAlchemy (ORM for database abstraction)
- Querying and modifying data
- Using foreign keys to access multiple tables
- SQL syntax, functions, and operations
"""

# Import necessary libraries
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# --------------------------
# DATABASE INTERACTION: SQLite
# --------------------------

def sqlite_demo():
    """
    Demonstrates SQLite database interaction:
    - Creating a table
    - Inserting data
    - Retrieving data
    """
    # Connect to SQLite database (or create it if it doesn’t exist)
    conn = sqlite3.connect('student_db.sqlite')
    cursor = conn.cursor()
    
    # CREATE TABLE - Defines the structure of the database table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  # Unique identifier
            name TEXT NOT NULL,  # Name of student (NOT NULL ensures no empty values)
            grade INTEGER NOT NULL  # Grade of student
        )
    """)
    conn.commit()
    
    # INSERT INTO - Adds new records to the table
    students_data = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
    cursor.executemany("INSERT INTO students (name, grade) VALUES (?, ?)", students_data)
    conn.commit()
    
    # SELECT - Retrieves data from the table
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    for row in results:
        print(row)  # Prints each student's data
    
    # Close connection
    conn.close()

# --------------------------
# DATABASE INTERACTION: SQLAlchemy
# --------------------------

Base = declarative_base()

def sqlalchemy_demo():
    """
    Demonstrates SQLAlchemy interaction:
    - Creating a table with ORM
    - Inserting and querying data
    - Using ForeignKey to establish relationships
    """
    # Create an SQLite database connection
    engine = create_engine('sqlite:///student_db.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Define a Student model using ORM
    class Student(Base):
        __tablename__ = 'students'
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        grade = Column(Integer, nullable=False)
    
    # Define a Course model to demonstrate FOREIGN KEY relationships
    class Course(Base):
        __tablename__ = 'courses'
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        student_id = Column(Integer, ForeignKey('students.id'))  # Foreign key linking to Student table
        student = relationship("Student")  # Establishing relationship
    
    # Create tables
    Base.metadata.create_all(engine)
    
    # Insert sample data
    student1 = Student(name='David', grade=88)
    student2 = Student(name='Eve', grade=92)
    session.add_all([student1, student2])
    session.commit()
    
    # Query data using SQLAlchemy ORM
    students = session.query(Student).all()
    for student in students:
        print(f"{student.id}: {student.name} - {student.grade}")
    
    # Close session
    session.close()

# --------------------------
# EXECUTING SQL QUERIES
# --------------------------

def execute_sql_query():
    """
    Demonstrates executing SQL queries manually:
    - SELECT: Retrieving specific columns
    - ORDER BY: Sorting data
    """
    conn = sqlite3.connect('student_db.sqlite')
    cursor = conn.cursor()
    
    # SELECT specific columns
    cursor.execute("SELECT name, grade FROM students ORDER BY grade DESC")
    results = cursor.fetchall()
    
    for row in results:
        print(f"Student: {row[0]}, Grade: {row[1]}")  # Display student details
    
    conn.close()

# --------------------------
# SQL FUNCTIONS & OPERATIONS
# --------------------------
"""
Common SQL functions:
- COUNT(): Counts the number of records
- AVG(): Computes average of a numeric column
- MIN()/MAX(): Finds min/max value in a column
- DISTINCT: Returns unique values
"""

def sql_functions_demo():
    conn = sqlite3.connect('student_db.sqlite')
    cursor = conn.cursor()
    
    # COUNT - Count total students
    cursor.execute("SELECT COUNT(*) FROM students")
    print("Total Students:", cursor.fetchone()[0])
    
    # AVG - Find average grade
    cursor.execute("SELECT AVG(grade) FROM students")
    print("Average Grade:", cursor.fetchone()[0])
    
    # MIN/MAX - Find lowest and highest grades
    cursor.execute("SELECT MIN(grade), MAX(grade) FROM students")
    min_max = cursor.fetchone()
    print(f"Lowest Grade: {min_max[0]}, Highest Grade: {min_max[1]}")
    
    conn.close()

# --------------------------
# MAIN FUNCTION
# --------------------------

if __name__ == "__main__":
    print("Running SQLite Demo...")
    sqlite_demo()
    
    print("\nRunning SQLAlchemy Demo...")
    sqlalchemy_demo()
    
    print("\nExecuting SQL Query...")
    execute_sql_query()
    
    print("\nRunning SQL Functions Demo...")
    sql_functions_demo()
