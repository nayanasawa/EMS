import mysql
from mysql.connector import connect, Error
from datetime import datetime

import datetime
import csv
# from mysql.connector import connect, Error
from faker import Faker
# import datetime
import random

# Define global variables for cursor and connection
cursor = None
connection = None


def connect_to_mysql(host, user, password, database):
    try:
        connection = connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection  # Return the connection object
        else:
            print("Failed to connect to MySQL database")
            return None
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None


# Function to create MySQL table
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS emss1 (
                employee_id INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                Age INT,
                Address VARCHAR(255),
                Mobile_Number VARCHAR(15),  -- Assuming mobile number is 15 characters max
                Gender ENUM('male', 'female', 'other'),  -- Using ENUM for gender with predefined values
                Education_Details VARCHAR(255),  -- Adjust the size according to your needs
                Salary DECIMAL(10, 2),  -- Assuming salary can have decimal values
                Annual_salary DECIMAL(10, 2),  -- Assuming annual salary can have decimal values
                DOJ DATE,
                Department VARCHAR(255),
                Position VARCHAR(255),
                Project_Name VARCHAR(255),
                Tech_Stack VARCHAR(255),
                Manager VARCHAR(255)
            )
        """)
        print("Table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")
    finally:
        if connection.is_connected():
            cursor.close()


# Function to insert random data into the table
def insert_random_data(connection, num_records=100):
    global cursor  # Add global declaration
    try:
        cursor = connection.cursor()
        fake = Faker('en_IN')

        for _ in range(num_records):
            name = fake.first_name() + " " + fake.last_name()
            age = fake.random_int(min=24, max=55)  # Adjusted maximum age
            address = f"{fake.building_number()} {fake.street_name()} {fake.city()}"
            # Generate mobile number ensuring the desired format
            mobile_number = "+91" + str(fake.random_element(elements=(6, 7, 8, 9))) + ''.join(
                [str(random.randint(0, 9)) for _ in range(9)])
            gender = fake.random_element(elements=("Male", "Female"))
            education_details = fake.random_element(elements=("B.tech", "Mtech", "MBA", "BBA", "BSC", "BCOM"))
            salary = fake.random_int(min=30000, max=150000)  # Adjusted salary range
            annual_salary = salary * 12
            doj = fake.date_between(start_date=datetime.date(2022, 1, 1), end_date=datetime.date(2022, 12, 31))
            department = fake.random_element(elements=("Engineering", "HR", "Sales", "Finance", "Marketing"))
            position = fake.random_element(elements=(
            "Manager", "Executive Manager", "Developer", "Data Analyst", "Data Scientist", "Cyber Security Engineer",
            "IT Systems Security Manager", "Applications Architect"))
            project_name = fake.random_element(elements=(
            "Community Connector", "Neighborhood Network", "Local Link", "Unity Hub", "Social Circle",
            "Harmonious Haven", "Civic Connect", "Neighborly Nexus", "UBER EATS", "UBER MEETS", "UBER CONNECT"))
            tech_stack = fake.random_element(elements=("Python", "SQL", "Flutter", "React", "Java"))
            # Randomly select manager name from the provided list
            manager = random.choice([
                "Ranbir Das", "Nakul Hari", "Indranil Rajagopalan", "Krish Dhar", "Rati Jha", "Rati Agarwal",
                "Kabir Khatri",
                "Neysa Suri", "Adira Vasa", "Ojas Dixit", "Ahana Ghose", "Riaan Dara", "Madhup Dhaliwal", "Piya Das",
                "Shamik Sami", "Rohan Desai", "Urvi Batra", "Dhanuk Vig", "Nishith Sengupta", "Rhea Ghose",
                "Mohanlal Das",
                "YuvrajLal", "Taimur Raja", "Nirvaan Edwin", "Rhea Sinha", "Renee Ganesh", "Abram Mane", "Tara Basak",
                "Jayesh Reddy", "Kaira Sathe", "Yasmin Majumdar", "Prerak Sha", "Myra Karpe", "Hazel Raj",
                "Madhup Devi",
                "Nakul Bumb", "Advika Mahal", "Manjari Ramesh", "Dhanush Anand", "Taimur Warrior", "Ryan Warrior",
                "Anvi Lall",
                "Pranay Kanda", "Keya Wason", "Gokul Batta", "Pranay Badal", "Hazel Krishna", "Aaryahi Hayre",
                "Jivika Sood",
                "Vedika Acharya", "Rasha Thaman", "Drishya Ganguly", "Biju Bansal", "Miraya Zachariah",
                "Diya Choudhary",
                "Kavya Bail", "Zara Devi", "Shalv Lanka", "Aaryahi Kapur", "Stuvan Balakrishnan", "Nakul Behl",
                "Rati Divan",
                "Pari Guha", "Dhruv Walia", "Dhruv Rama", "Nishith Dey", "Nitara Grover", "Kimaya Handa", "Pihu Mani",
                "Jhanvi Jain", "Manjari Lata", "Oorja Kara", "Mahika Dalal", "Aarush Hari", "Onkar Ram",
                "Ivan Sankaran",
                "Purab Mangal", "Hiran Rajan", "Kanav Bhavsar", "Aarush Bhasin", "Jayesh Banik", "Miraya Ratti",
                "Pihu Badal",
                "Yasmin Bhatnagar", "Jayan Shukla", "Mamooty Tandon", "Vedika Rajan", "Anya Gade", "Elakshi Thaker",
                "Parinaaz Bala",
                "Rasha Dhaliwal", "Ahana Kar", "Piya Chaudry", "Anay Gulati", "Neelofar Rattan", "Reyansh Gupta",
                "Damini Vala",
                "Shalv Gokhale", "Adira Kata", "Anvi Dube"
            ])

            # Insert data into the table
            cursor.execute("""
                INSERT INTO emss1 (Name, Age, Address, Mobile_Number, Gender, Education_Details, Salary, Annual_salary, DOJ, Department, Position, Project_Name, Tech_Stack, Manager)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (name, age, address, mobile_number, gender, education_details, salary, annual_salary, doj, department,
                  position, project_name, tech_stack, manager))

        connection.commit()
        print("Random data inserted successfully.")
    except Error as e:
        print(f"Error inserting random data: {e}")
    finally:
        if connection.is_connected():
            cursor.close()

# Function to validate emp_id
def validate_employee_id(employee_id):
    return employee_id.isdigit()  # Basic validation, can be extended

# Function to validate name input
def validate_name(name):
    if not name.replace(" ", "").isalpha():
        print("Give me a valid name.")
        return False
    elif len(name) > 20:
        print("Name length should not exceed 20 characters.")
        return False
    else:
        return True


# Function to validate age input
def validate_age(age):
    if not age.isdigit():
        print("Give me a valid age.")
        return False
    else:
        age_int = int(age)
        if age_int < 20 or age_int > 55:
            print("Age should be between 23 and 55.")
            return False
        else:
            return True
# Function to validate address
def validate_address(address):
    num_count = sum(c.isdigit() for c in address)
    if num_count < 1 or num_count > 2:
        print("Address should start with one or two numbers.")
        return False
    elif not address[num_count:].replace(" ", "").isalpha():
        print("Address should only contain letters (and spaces) after the initial numbers.")
        return False
    else:
        return True


# Function to validate mobile number input
def validate_mobile_number(mobile_number):
    if not mobile_number.startswith("+91"):
        print("Mobile number should start with +91.")
        return False
    elif len(mobile_number) != 13 or not mobile_number[3:].isdigit():
        print("Mobile number should contain only digits after +91.")
        return False
    elif not set(mobile_number[3:4]) <= set("6789"):
        print("Mobile number should contain only one digit from 8, 7, 6, 9 after +91.")
        return False
    else:
        return True


# Function to validate gender input
def validate_gender(gender):
    gender = gender.strip().upper()  # Remove leading and trailing whitespace and convert to uppercase
    if len(gender) != 1 or gender not in ["M", "F", "O"]:
        print("Gender should be either 'M', 'F', or 'O' (Others), without spaces, digits, or special characters.")
        return False
    else:
        return True


# Function to validate education details input
def validate_education_details(education):
    if not education.replace(" ", "").isalpha():
        print("Education details should only contain alphabets.")
        return False
    else:
        return True


# Function to validate monthly salary input
def validate_salary(salary):
    if salary.isdigit() and len(salary) >= 4:
        return True
    else:
        print("Salary should be a 4-digit number.")
        return False


#import datetime

import datetime
#from datetime import datetime


def validate_date_of_joining(doj):
    try:
        # Check if the date of joining follows the format YYYY-MM-DD
        datetime.datetime.strptime(doj, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Date of joining should follow the format YYYY-MM-DD.")
        return False

    # Get the current date
    current_date = datetime.date.today()

    # Extract year, month, and day from the date of joining
    year, month, day = map(int, doj.split('-'))

    # Check if the year is not greater than the current year
    if year > current_date.year:
        print("Year should not be greater than the current year.")
        return False

    # Check if the month is not greater than 12
    if month > 12:
        print("Month should not be greater than 12.")
        return False

    # Check if the day is not greater than 31
    if day > 31:
        print("Day should not be greater than 31.")
        return False

    return True


# Function to validate department input
def validate_department(department):
    if not department.replace(" ", "").isalpha():
        print("Department should only contain alphabets.")
        return False
    else:
        return True


# Function to validate position input
def validate_position(position):
    if not position.replace(" ", "").isalpha():
        print("Position should only contain alphabets.")
        return False
    else:
        return True


# Function to validate project name input
def validate_project_name(project_name):
    if not project_name.replace(" ", "").isalpha():
        print("Project name should only contain alphabets.")
        return False
    else:
        return True


# Function to validate tech stack input
def validate_tech_stack(tech_stack):
    if not tech_stack.replace(" ", "").isalpha():
        print("Tech stack should only contain alphabets.")
        return False
    else:
        return True


# Function to validate annual salary input
def validate_annual_salary(annual_salary):
    if not annual_salary.isdigit():
        print("Annual salary should contain only numbers.")
        return False
    else:
        annual_salary_int = int(annual_salary)
        if annual_salary_int < 300000:
            print("Annual salary should be more than 300,000.")
            return False
        else:
            return True


# Function to validate education details input
def validate_manager(manager):
    if not manager.replace(" ", "").isalpha():
        print("manager details should only contain alphabets.")
        return False
    else:
        return True


def add_new_employee(connection):
    if connection is None:
        print("No connection to MySQL database.")
        return

    try:
        cursor = connection.cursor()
        # Get employee details from user input
        name = input("Enter name: ")
        if not name:
            print("Name cannot be empty.")
            return
        elif not validate_name(name):
            return

        age = input("Enter age: ")
        if not age:
            print("Age cannot be empty.")
            return
        elif not validate_age(age):
            return

        address = input("Enter address: ")
        if not address:
            print("Address cannot be empty.")
            return
        elif not validate_address(address):
            return

        mobile_number = input("Enter mobile number: ")
        if not mobile_number:
            print("Mobile number cannot be empty.")
            return
        elif not validate_mobile_number(mobile_number):
            return

        gender = input("Enter gender: ")
        if not gender:
            print("Gender cannot be empty.")
            return
        elif not validate_gender(gender):
            return

        education_details = input("Enter education details: ")
        if not education_details:
            print("Education details cannot be empty.")
            return
        elif not validate_education_details(education_details):
            return

        salary = input("Enter salary: ")
        if not salary:
            print("Salary cannot be empty.")
            return
        elif not validate_salary(salary):
            return

        doj = input("Enter date of joining (YYYY-MM-DD): ")
        if not doj:
            print("Date of joining cannot be empty.")
            return
        elif not validate_date_of_joining(doj):
            return

        department = input("Enter department: ")
        if not department:
            print("Department cannot be empty.")
            return
        elif not validate_department(department):
            return

        position = input("Enter position: ")
        if not position:
            print("Position cannot be empty.")
            return
        elif not validate_position(position):
            return

        project_name = input("Enter project name: ")
        if not project_name:
            print("Project name cannot be empty.")
            return
        elif not validate_project_name(project_name):
            return

        tech_stack = input("Enter tech stack: ")
        if not tech_stack:
            print("Tech stack cannot be empty.")
            return
        elif not validate_tech_stack(tech_stack):
            return

        annual_salary = input("Enter annual salary: ")
        if not annual_salary:
            print("Annual salary cannot be empty.")
            return
        elif not validate_annual_salary(annual_salary):
            return

        manager = input("Enter Manager name: ")
        if not manager:
            print("Manager name cannot be empty.")
            return
        elif not validate_manager(manager):
            return

        # Insert new employee data into MySQL table
        cursor.execute("""
            INSERT INTO emss1 (Name, Age, Address, Mobile_Number, Gender, Education_Details, Salary, DOJ, Department, Position, Project_Name, Tech_Stack, Annual_Salary,manager)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
        """, (
            name, age, address, mobile_number, gender, education_details, salary, doj, department, position,
            project_name, tech_stack, annual_salary, manager))

        connection.commit()
        print("New employee added successfully")

    except Error as e:
        print(f"Error adding new employee: {e}")
        # Handle the error appropriately

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
# employee_id
def find_employee_id_by_name(connection, employee_name):
    cursor = connection.cursor()
    try:
        # Query to find the employee ID by name
        cursor.execute("SELECT employee_id FROM emss1 WHERE Name = %s", (employee_name,))

        # Fetch all rows to consume the entire result set
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(f"The ID of {employee_name} is {row[0]}.")
        else:
            print(f"No employee found with the name {employee_name}.")
    except Error as e:
        print(f"Error finding employee ID: {e}")
    finally:
        cursor.close()
        cursor.close()

def view_employee_details(connection):
    cursor = connection.cursor()

    # Get the ID of the employee whose details to view
    employee_id = input("Enter the ID of the employee: ")

    # Query the database to retrieve the details of the employee
    try:
        cursor.execute("""
            SELECT * FROM emss1 WHERE employee_id = %s AND is_delete = 0
        """, (employee_id,))

        # Fetch all results
        employee_details = cursor.fetchall()

        if employee_details:
            print(f"Details for Employee ID {employee_id}:")
            for idx, employee in enumerate(employee_details, start=1):
                print(f"\nEmployee Details {idx}:")
                print("ID:", employee[0])  # assuming employee_id is the first column
                print("Name:", employee[1])
                print("Age:", employee[2])
                print("Address:", employee[3])
                print("Mobile Number:", employee[4])
                print("Gender:", employee[5])
                print("Education Details:", employee[6])
                print("Salary:", employee[7])
                print("Annual Salary:", employee[8])
                print("DOJ:", employee[9])
                print("Department:", employee[10])
                print("Position:", employee[11])
                print("Project Name:", employee[12])
                print("Tech Stack:", employee[13])
                print("Manager:", employee[14])
        else:
            cursor.execute("""
                SELECT is_delete FROM emss1 WHERE employee_id = %s
            """, (employee_id,))
            is_deleted = cursor.fetchone()
            if is_deleted and is_deleted[0] == 1:
                print("Employee is inactive.")
            else:
                print("Employee not found.")

    except Error as e:
        print(f"Error retrieving employee details: {e}")
    finally:
        cursor.close()

def update_employee_info(connection, cursor):
    while True:
        try:
            employee_id = input("Enter employee ID: ")
            if not validate_employee_id(employee_id):
                print("Invalid Employee ID. Please enter a valid ID.")
                continue
            select_query = "SELECT * FROM emss1 WHERE employee_id = %s"
            cursor.execute(select_query, (employee_id,))
            employee = cursor.fetchone()
            if employee:
                if employee[-1] == 1:  # Check if is_delete is set to 1
                    print("Employee with ID", employee_id, "is inactive.")
                    continue
            if employee:
                print("ID:", employee[0])  # assuming employee_id is the first column
                print("Name:", employee[1])
                print("Age:", employee[2])
                print("Address:", employee[3])
                print("Mobile Number:", employee[4])
                print("Gender:", employee[5])
                print("Education Details:", employee[6])
                print("Salary:", employee[7])
                print("Annual Salary:", employee[8])
                print("DOJ:", employee[9])
                print("Department:", employee[10])
                print("Position:", employee[11])
                print("Project Name:", employee[12])
                print("Tech Stack:", employee[13])
                #  print("Annual Salary:", employee[13])
                print("Manager:", employee[14])
                # Menu for selecting information to update
                print("\nSelect the information you want to update:")
                print("1. Age")
                print("2. Address")
                print("3. Gender")
                print("4. Education Details")
                print("5. Date of Joining")
                print("6. Department")
                print("7. Position")
                print("8. Annual Salary")
                print("9. Project")
                print("10. Manager")
                print("11. Tech Stack")
                print("12. Mobile Number")
                print("0. Exit")

                choice = input("Enter your choice (0-12): ")

                if choice == '0':
                    break

                if choice == '1':
                    # Update age
                    age = None
                    while age is None or not validate_age(age):
                        age = input("Enter new age: ").strip()
                        if not validate_age(age):
                            print("Age must be a number between 20 and 55.")
                    update_query = "UPDATE emss1 SET Age=%s WHERE employee_id=%s"
                    cursor.execute(update_query, (age, employee_id))
                    connection.commit()
                    print("Age updated successfully!")

                elif choice == '2':
                    # Update address
                    address = None
                    while not address:
                        address = input("Enter new address: ").strip()
                        if not address:
                            print("Address cannot be blank.")
                        elif not validate_address(address):
                            print("Invalid address format.")
                    update_query = "UPDATE emss1 SET Address=%s WHERE employee_id=%s"
                    cursor.execute(update_query, (address, employee_id))
                    connection.commit()
                    print("Address updated successfully!")

                elif choice == '3':
                    # Update gender
                    gender = None
                    while not gender or not validate_gender(gender):
                        gender = input("Enter new gender (male/female/other): ").strip().lower()
                        if not validate_gender(gender):
                            print("Invalid gender. Please enter 'male', 'female', or 'other'.")
                    update_query = "UPDATE emss1 SET Gender=%s WHERE employee_id=%s"
                    cursor.execute(update_query, (gender, employee_id))
                    connection.commit()
                    print("Gender updated successfully!")

                elif choice == '4':
                    # Update education details
                    education_details = None
                    while not education_details:
                        education_details = input("Enter new education details: ").strip()
                        if not education_details:
                            print("Education details cannot be blank.")
                        elif not validate_education_details(education_details):
                            print("Invalid education details format.")
                    update_query = "UPDATE emss1 SET Education_Details=%s WHERE employee_id=%s"
                    cursor.execute(update_query, (education_details, employee_id))
                    connection.commit()
                    print("Education details updated successfully!")

                elif choice == '5':
                    # Update date of joining
                    doj = None
                    while not doj:
                        doj_input = input("Enter new date of joining (YYYY-MM-DD): ").strip()
                        if not doj_input:
                            print("Date of joining cannot be empty.")
                        elif not validate_date_of_joining(doj_input):
                            print("Invalid date format. Date of joining should follow the format YYYY-MM-DD.")
                        else:
                            doj = doj_input
                    update_query = "UPDATE emss1 SET DOJ=%s WHERE employee_id=%s"
                    cursor.execute(update_query, (doj, employee_id))
                    connection.commit()
                    print("Date of Joining updated successfully!")

                elif choice == '6':
                    # Update department
                    department = None
                    while not department:
                        department = input("Enter new department: ").strip()
                        if not department:
                            print("Department cannot be blank.")
                        elif not validate_department(department):
                            print("Invalid department format.")
                    update_query = "UPDATE emss1 SET Department=%s WHERE employee_id=%s"
                    cursor.execute(update_query, (department, employee_id))
                    connection.commit()
                    print("Department updated successfully!")

                elif choice == '7':
                    # Update position
                    position = None
                    while not position:
                        position = input("Enter new position: ").strip()
                        if not position:
                            print("Position cannot be blank.")
                        elif not validate_position(position):
                            print("Invalid position format.")
                    update_query = "UPDATE emss1 SET Position=%s WHERE employee_id=%s"
                    cursor.execute(update_query, (position, employee_id))
                    connection.commit()
                    print("Position updated successfully!")

                elif choice == '8':
                    # Update annual salary
                    annual_salary = None
                    while not annual_salary:
                        annual_salary_input = input("Enter new annual salary: ").strip()
                        if not annual_salary_input:
                            print("Annual salary cannot be empty.")
                        elif not validate_annual_salary(annual_salary_input):
                            print("Invalid annual salary format.")
                        else:
                            annual_salary = annual_salary_input
                    update_query = "UPDATE emss1 SET Annual_Salary=%s WHERE employee_id=%s"
                    cursor.execute(update_query, (annual_salary, employee_id))
                    connection.commit()
                    print("Annual Salary updated successfully!")

                elif choice == '9':
                    # Update project
                    project = None
                    while not project:
                        project = input("Enter new project: ").strip()
                        if not project:
                            print("Project cannot be blank.")
                        elif not validate_project_name(project):
                            print("Invalid project name format.")
                    update_query = "UPDATE emss1 SET Project_Name=%s WHERE employee_id=%s"
                    cursor.execute(update_query, (project, employee_id))
                    connection.commit()
                    print("Project updated successfully!")

                elif choice == '10':
                    # Update manager
                    manager = None
                    while not manager:
                        manager = input("Enter new manager: ").strip()
                        if not manager:
                            print("Manager name cannot be blank.")
                        elif not validate_manager(manager):
                            print("Invalid manager name format.")
                    update_query = "UPDATE emss1 SET Manager=%s WHERE employee_id=%s"
                    cursor.execute(update_query, (manager, employee_id))
                    connection.commit()
                    print("Manager updated successfully!")

                elif choice == '11':
                    # Update tech stack
                    tech_stack = None
                    while not tech_stack:
                        tech_stack = input("Enter new tech stack: ").strip()
                        if not tech_stack:
                            print("Tech stack cannot be blank.")
                        elif not validate_tech_stack(tech_stack):
                            print("Invalid tech stack format.")
                    update_query = "UPDATE emss1 SET Tech_Stack=%s WHERE employee_id=%s"
                    cursor.execute(update_query, (tech_stack, employee_id))
                    connection.commit()
                    print("Tech Stack updated successfully!")

                elif choice == '12':
                    # Update mobile number
                    mobile_number = None
                    while not mobile_number:
                        mobile_number = input("Enter new mobile number: ").strip()
                        if not mobile_number:
                            print("Mobile number cannot be blank.")
                        elif not validate_mobile_number(mobile_number):
                            print("Invalid mobile number format.")
                    update_query = "UPDATE emss1 SET Mobile_Number=%s WHERE employee_id=%s"
                    cursor.execute(update_query, (mobile_number, employee_id))
                    connection.commit()
                    print("Mobile Number updated successfully!")

                else:
                    print("Invalid choice. Please enter a number between 0 and 12.")
            else:
                print("Employee not found. Please enter a valid Employee ID.")
        except ValueError:
            print("Invalid Employee ID. Please enter a valid ID.")


# Function to delete employee records who worked less than 1 month
# Function to delete employee records whose DOJ is more than one month ago
def delete_inactive_emss1(connection):
    cursor = connection.cursor()

    try:
        # Calculate today's date
        current_date = datetime.date.today()
        # Calculate the date 1 month ago
        one_month_ago = current_date - datetime.timedelta(days=30)

        # Ask for the employee ID to delete
        employee_id = int(input("Enter the Employee ID to delete: "))

        # Update the 'is_delete' column to mark the employee record as inactive
        cursor.execute("UPDATE emss1 SET is_delete = 1 WHERE DOJ <= %s AND employee_id = %s", (one_month_ago, employee_id))
        connection.commit()
        print("Employee record marked as inactive successfully")
    except Error as e:
        print(f"Error marking employee record as inactive: {e}")
    finally:
        if connection.is_connected():
            cursor.close()


# Function to list all employees in the organization with department, position, gender, and employee name
# Function to list all employees in the organization
def list_all_emss1(connection):
    cursor = connection.cursor()
    try:
        # Query the database to retrieve all active employees' details
        cursor.execute("SELECT Distinct Name, Department, Position, Gender FROM emss1 WHERE is_delete = 0")
        # Fetch all results
        active_emss1 = cursor.fetchall()
        if active_emss1:
            print("\nAll Active Employees in the Organization:")
            for idx, employee in enumerate(active_emss1, start=1):
                print(f"\nEmployee {idx}:")
                print("Name:", employee[0])
                print("Department:", employee[1])
                print("Position:", employee[2])
                print("Gender:", employee[3])
        else:
            print("No active employees found in the organization.")
    except Error as e:
        print(f"Error listing all emss1: {e}")
    finally:
        if connection.is_connected():
            cursor.close()



def calculate_total_monthly_salary(connection):
    cursor = connection.cursor()

    try:
        # Query to retrieve the total monthly salary for each distinct active employee
        cursor.execute("""
            SELECT DISTINCT Name, Annual_Salary / 12 AS Monthly_Salary
            FROM emss1
            WHERE is_delete = 0
        """)

        # Fetch all results
        results = cursor.fetchall()

        if results:
            print("Total Monthly Salary for Each Active Employee:")
            for idx, employee in enumerate(results, start=1):
                print(f"\nEmployee {idx}:")
                print("Name:", employee[0])
                print("Total Monthly Salary:", employee[1])
        else:
            print("No active employees found.")

    except Error as e:
        print(f"Error calculating total monthly salary: {e}")

    finally:
        cursor.close()



import csv


# Function to export employee data to a CSV file
import csv

def export_employee_data_to_csv(connection, csv_file_path):
    try:
        cursor = connection.cursor()

        # SQL query to select all active employee data
        query = """
            SELECT Name, Age, Address, Mobile_Number, Gender, Education_Details, Salary, DOJ, Department, Position, Project_Name, Tech_Stack, Annual_Salary, manager
            FROM emss1
            WHERE is_delete = 0
        """
        # Execute the query
        cursor.execute(query)
        # Fetch all results
        results = cursor.fetchall()
        # Write data to CSV file
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write header row
            writer.writerow(['Name', 'Age', 'Address', 'Mobile_Number', 'Gender', 'Education_Details', 'Salary', 'DOJ',
                             'Department', 'Position', 'Project_Name', 'Tech_Stack', 'Annual_Salary', 'manager'])
            # Write data rows
            writer.writerows(results)

        print(f"Employee data exported to '{csv_file_path}' successfully.")

    except Error as e:
        print(f"Error exporting employee data to CSV: {e}")

    finally:
        if connection.is_connected():
            cursor.close()



def assign_projects(connection):
    try:
        cursor = connection.cursor()

        # SQL query to select active employees without assigned projects
        select_query = """
            SELECT Name
            FROM emss1
            WHERE Project_Name IS NULL AND is_delete = 0
        """
        # Execute the select query
        cursor.execute(select_query)
        # Fetch all results
        emss1_without_projects = cursor.fetchall()
        if emss1_without_projects:
            for employee in emss1_without_projects:
                # SQL query to select a project not assigned to any active employee
                update_query = """
                    UPDATE emss1
                    SET Project_Name = (
                        SELECT Project_Name
                        FROM (
                            SELECT DISTINCT Project_Name
                            FROM emss1
                            WHERE Project_Name NOT IN (
                                SELECT Project_Name
                                FROM emss1
                                WHERE Name = %s AND is_delete = 0
                            )
                        ) AS temp
                        LIMIT 1
                    )
                    WHERE Name = %s AND is_delete = 0
                """
                # Execute the update query
                cursor.execute(update_query, (employee[0], employee[0]))
                connection.commit()

            print("Projects assigned successfully.")

        else:
            print("All active employees already have projects assigned.")

    except Error as e:
        print(f"Error assigning projects: {e}")

    finally:
        if connection.is_connected():
            cursor.close()



def view_employee_projects(connection):
    cursor = connection.cursor()

    # Get employee's name
    employee_name = input("Enter the name of the employee: ")

    try:
        # Retrieve present project details for the employee
        cursor.execute("""
            SELECT Project_Name, Tech_Stack, Annual_Salary
            FROM emss1
            WHERE Name = %s AND is_delete = 0
        """, (employee_name,))
        present_projects = cursor.fetchall()

        # Retrieve distinct past project details for the employee
        cursor.execute("""
            SELECT DISTINCT Project_Name
            FROM emss1
            WHERE Name = %s AND Project_Name NOT IN (
                SELECT Project_Name
                FROM emss1
                WHERE Name = %s AND is_delete = 0
            ) AND is_delete = 0
        """, (employee_name, employee_name))
        past_projects = cursor.fetchall()

        # Display present project details
        if present_projects:
            print("\nPresent Projects:")
            for project in present_projects:
                print(f"Project Name: {project[0]}, Tech Stack: {project[1]}, Annual Salary: {project[2]}")
        else:
            print("No present projects found for the employee.")

        # Display past project details
        if past_projects:
            print("\nPast Projects:")
            for project in past_projects:
                print(f"Project Name: {project[0]}")
        else:
            print("No past projects found for the employee.")

    except Error as e:
        print(f"Error viewing employee projects: {e}")
    finally:
        cursor.close()



def update_employee_project(connection):
    cursor = connection.cursor()

    try:
        # Get employee's name
        employee_name = input("Enter the name of the employee: ")

        # Check if the employee is active
        cursor.execute("SELECT * FROM emss1 WHERE Name = %s AND is_delete = 0", (employee_name,))
        employee = cursor.fetchone()

        if employee:
            # Get the new project details
            new_project_name = input("Enter the new project name: ")
            new_tech_stack = input("Enter the new tech stack: ")
            new_annual_salary = input("Enter the new annual salary: ")

            # Update the employee's current project
            cursor.execute("""
                UPDATE emss1
                SET Project_Name = %s, Tech_Stack = %s, Annual_Salary = %s
                WHERE Name = %s AND is_delete = 0
            """, (new_project_name, new_tech_stack, new_annual_salary, employee_name))

            connection.commit()

            print("Employee's project details updated successfully.")
        else:
            print("Employee not found or inactive. Please enter a valid and active employee name.")

    except Error as e:
        connection.rollback()
        print(f"Error updating project details: {e}")
    finally:
        cursor.close()


def add_tech_stack_for_employee(connection):
    cursor = connection.cursor()

    # Get employee's name
    employee_name = input("Enter the name of the employee: ")

    # Get the tech stack
    tech_stack = input("Enter the tech stack for the employee: ")

    try:
        # Check if the employee exists and is active
        cursor.execute("""
            SELECT 1 FROM emss1 WHERE Name = %s AND is_delete = 0
        """, (employee_name,))
        existing_employee = cursor.fetchone()

        if existing_employee:
            # Insert or update the employee's tech stack
            cursor.execute("""
                INSERT INTO emss1 (Name, Tech_Stack)
                VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE Tech_Stack = VALUES(Tech_Stack)
            """, (employee_name, tech_stack))

            connection.commit()

            print("Tech stack added successfully.")
        else:
            print("Employee not found or is inactive.")

    except Error as e:
        connection.rollback()
        print(f"Error adding tech stack: {e}")

    finally:
        cursor.close()

def view_employee_tech_stack(connection):
    cursor = connection.cursor()

    # Get employee's name
    employee_name = input("Enter the name of the employee: ")

    try:
        # Query to retrieve department and tech stack based on employee's name, considering only active employees
        cursor.execute("""
            SELECT Department, Tech_Stack
            FROM emss1
            WHERE Name = %s AND is_delete = 0
        """, (employee_name,))

        employee_info = cursor.fetchone()

        if employee_info:
            department, tech_stack = employee_info
            if department.lower() == 'engineering' or department.upper() == 'ENGINEERING':
                print(f"Tech Stack of {employee_name}: {tech_stack}")
            else:
                print(f"{employee_name} does not belong to the engineering department.")
        else:
            print("Employee not found or is inactive.")

    except Error as e:
        print(f"Error retrieving employee's information: {e}")

    finally:
        cursor.close()

def search_employee_by_name(connection):
    cursor = connection.cursor()

    # Get the name to search for
    search_name = input("Enter the name of the employee to search: ")

    try:
        # Query to search for active employees by name
        cursor.execute("""
            SELECT DISTINCT Name, Age, Address, Mobile_Number, Gender, Education_Details, Salary, DOJ, Department, Position, Project_Name, Tech_Stack, Annual_Salary
            FROM emss1
            WHERE Name = %s AND is_delete = 0
        """, (search_name,))

        # Fetch all matching results
        results = cursor.fetchall()

        if results:
            print("Search Results:")
            for idx, employee in enumerate(results, start=1):
                print(f"\nEmployee {idx}:")
                print("Name:", employee[0])
                print("Age:", employee[1])
                print("Address:", employee[2])
                print("Mobile Number:", employee[3])
                print("Gender:", employee[4])
                print("Education Details:", employee[5])
                print("Salary:", employee[6])
                print("Date of Joining:", employee[7])
                print("Department:", employee[8])
                print("Position:", employee[9])
                print("Project Name:", employee[10])
                print("Tech Stack:", employee[11])
                print("Annual Salary:", employee[12])
        else:
            print("No matching employees found.")

    except Error as e:
        print(f"Error searching for employees: {e}")

    finally:
        cursor.close()



from mysql.connector import connect, Error

def search_employee_by_tech_stack(connection):
    cursor = connection.cursor()

    # Options menu for selecting the tech stack
    print("Select Tech Stack:")
    print("1. Java")
    print("2. React")
    print("3. SQL")
    print("4. Flutter")
    print("5. Python")
    print("6. Other")  # For other tech stacks not listed
    option = input("Enter your choice (1-6): ")

    tech_stacks = {
        '1': 'Java',
        '2': 'React',
        '3': 'SQL',
        '4': 'Flutter',
        '5': 'Python',
        '6': 'Other'
    }

    selected_stack = tech_stacks.get(option)
    if selected_stack:
        if option == '6':
            # If user selects "Other," prompt for the tech stack name
            selected_stack = input("Enter the tech stack name to be searched: ")

        try:
            # Query to search for active employees by selected tech stack
            cursor.execute("""
                      SELECT DISTINCT Name, Age, Address, Mobile_Number, Gender, Education_Details, Salary, DOJ, Department, Position, Project_Name, Tech_Stack, Annual_Salary
                      FROM emss1
                      WHERE Tech_Stack LIKE %s AND is_delete = 0
                  """, ('%' + selected_stack + '%',))  # Using wildcard to search for partial matches

            # Fetch all matching results
            results = cursor.fetchall()

            if results:
                print(f"\nSearch Results for {selected_stack}:")
                for idx, employee in enumerate(results, start=1):
                    print(f"\nEmployee {idx}:")
                    print("Name:", employee[0])
                    print("Age:", employee[1])
                    print("Address:", employee[2])
                    print("Mobile Number:", employee[3])
                    print("Gender:", employee[4])
                    print("Education Details:", employee[5])
                    print("Salary:", employee[6])
                    print("Date of Joining:", employee[7])
                    print("Department:", employee[8])
                    print("Position:", employee[9])
                    print("Project Name:", employee[10])
                    print("Tech Stack:", employee[11])
                    print("Annual Salary:", employee[12])
            else:
                print(f"No matching employees found for {selected_stack} tech stack.")

        except Error as e:
            print(f"Error searching for employees: {e}")

    else:
        print("Invalid option. Please enter a number from 1 to 6.")

    cursor.close()


def search_employee_by_project_name(connection):
    cursor = connection.cursor()

    # Get the project name to search for
    project_name = input("Enter the project name to search: ")

    try:
        # Query to search for active employees by project name
        cursor.execute("""
            SELECT DISTINCT Name, Age, Address, Mobile_Number, Gender, Education_Details, Salary, DOJ, Department, Position, Project_Name, Tech_Stack, Annual_Salary
            FROM emss1
            WHERE Project_Name LIKE %s AND is_delete = 0
        """, ('%' + project_name + '%',))  # Using wildcard to search for partial matches

        # Fetch all matching results
        results = cursor.fetchall()

        if results:
            print("Search Results:")
            for idx, employee in enumerate(results, start=1):
                print(f"\nEmployee {idx}:")
                print("Name:", employee[0])
                print("Age:", employee[1])
                print("Address:", employee[2])
                print("Mobile Number:", employee[3])
                print("Gender:", employee[4])
                print("Education Details:", employee[5])
                print("Salary:", employee[6])
                print("Date of Joining:", employee[7])
                print("Department:", employee[8])
                print("Position:", employee[9])
                print("Project Name:", employee[10])
                print("Tech Stack:", employee[11])
                print("Annual Salary:", employee[12])
        else:
            print("No matching employees found.")

    except Error as e:
        print(f"Error searching for employees: {e}")

    finally:
        cursor.close()


def sort_emss1_by_salary(connection):
    cursor = connection.cursor()

    try:
        print("Sort Employees by Salary:")
        print("1. Highest 5 Salaries")
        print("2. Lowest 5 Salaries")
        print("3. Total Sorted Salaries")
        option = input("Enter your choice (1, 2, 3): ")

        if option == '1':
            cursor.execute("""
                SELECT Name, Annual_Salary
                FROM emss1
                WHERE Annual_Salary IS NOT NULL AND is_delete = 0
                ORDER BY Annual_Salary DESC
                LIMIT 5
            """)
        elif option == '2':
            cursor.execute("""
                SELECT Name, Annual_Salary
                FROM emss1
                WHERE Annual_Salary IS NOT NULL AND is_delete = 0
                ORDER BY Annual_Salary ASC
                LIMIT 5
            """)
        elif option == '3':
            cursor.execute("""
                SELECT Name, Annual_Salary
                FROM emss1
                WHERE Annual_Salary IS NOT NULL AND is_delete = 0
                ORDER BY Annual_Salary
            """)
        else:
            print("Invalid option.")
            return

        sorted_salaries = cursor.fetchall()

        if sorted_salaries:
            print("Sorted Employees:")
            for employee in sorted_salaries:
                print(f"Name: {employee[0]}, Annual Salary: {employee[1]}")
        else:
            print("No employees found with salary data.")

    except Error as e:
        print(f"Error sorting employees by salary: {e}")
    finally:
        cursor.close()



def assign_managers(connection):
    try:
        cursor = connection.cursor()

        # SQL query to select active employees without assigned managers
        select_query = """
            SELECT Name
            FROM emss1
            WHERE Manager IS NULL AND is_delete = 0
        """

        # Execute the select query
        cursor.execute(select_query)

        # Fetch all results
        employees_without_managers = cursor.fetchall()

        if employees_without_managers:
            for employee in employees_without_managers:
                # SQL query to select an active manager not assigned to any other active employee
                update_query = """
                    UPDATE emss1 AS e1
                    JOIN (
                        SELECT Manager
                        FROM emss1
                        WHERE Manager IS NOT NULL AND is_delete = 0
                        GROUP BY Manager
                        HAVING COUNT(*) = 1
                        LIMIT 1
                    ) AS e2 ON e1.Manager = e2.Manager
                    SET e1.Manager = e2.Manager
                    WHERE e1.Name = %s AND e1.Manager IS NULL
                """
                # Execute the update query
                cursor.execute(update_query, (employee[0],))
                connection.commit()

            print("Managers assigned successfully.")

        else:
            print("All active employees already have managers assigned.")

    except Error as e:
        print(f"Error assigning managers: {e}")

    finally:
        if connection.is_connected():
            cursor.close()



def view_manager_details(connection):
    try:
        cursor = connection.cursor()

        # Get the manager's name
        manager_name = input("Enter the name of the manager: ")

        # SQL query to view mentees of the specified manager (considering only active employees)
        query = """
            SELECT 
                Name
            FROM 
                emss1
            WHERE 
                Manager = %s AND is_delete = 0
        """

        # Execute the query with the manager's name as parameter
        cursor.execute(query, (manager_name,))

        # Fetch all mentees' details
        mentees = cursor.fetchall()

        # Print the results
        if mentees:
            print(f"Mentees of Manager {manager_name}:")
            for mentee in mentees:
                print(f"Mentee: {mentee[0]}")
        else:
            print(f"No active mentees found for manager: {manager_name}")

    except mysql.connector.Error as error:
        print(f"Error viewing manager details: {error}")

    finally:
        if connection.is_connected():
            cursor.close()



# Function to import employee data from a CSV file

# Function to insert data from CSV file into MySQL table
def import_employee_data(connection, file_path):
    try:
        cursor = connection.cursor()

        # Get the maximum existing employee_id from the table
        cursor.execute("SELECT MAX(employee_id) FROM emss1")
        result = cursor.fetchone()
        max_employee_id = result[0] if result[0] is not None else 2000  # If no records exist, start from 2000

        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                max_employee_id += 1  # Increment the employee_id
                row[0] = max_employee_id  # Assign the new employee_id to the row
                try:
                    # Convert 'Age' to integer before insertion
                    row[2] = int(row[2])
                    cursor.execute("""
                        INSERT INTO emss1(employee_id, Name, Age, Address, Mobile_Number, Gender,
                                           Education_Details, Salary, Annual_Salary, DOJ, Department,
                                           Position, Project_Name, Tech_Stack, Manager, Is_Delete)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, row)
                except (ValueError, IndexError) as e:
                    print(f"Error inserting row {row}: {e}")
            connection.commit()
        print("Data inserted successfully")
    except Error as e:
        print(f"Error inserting data into MySQL table: {e}")



def main():
    host = "127.0.0.1"
    user = "root"
    password = "Nayan@12345"
    database = "new"

    # Connect to MySQL database
    connection = connect_to_mysql(host, user, password, database)
    if connection:
        create_table(connection)
        insert_random_data(connection, num_records=100)
        # insert_data_from_csv(connection, '/home/nineleaps/Downloads/all.csv')

    while True:
        print("\nMenu:")
        print("1.  Add a new employee")
        print("2.  View a particular employee's details")
        print("3.  Update employee information")
        print("4.  Delete employee record ")
        print("5.  List all employees in the organization")
        print("6.  Calculate total monthly salary for each employee")
        print("7.  Export employee data to a CSV file")
        print("8.  Assign projects to employees ")
        print("9.  View employee projects ")
        print("10  Update employee project ")
        print("11. Add tech stack for employees")
        print("12. View employee's known tech stack")
        print("13. Search by employee name ")
        print("14. Search employees by tech stack")
        print("15  Search employee by project name")
        print("16 sort employees by salary ")
        print("17 Assign Manager")
        print("18 View Manager Details")
        print("19 Import employee data from a CSV file")
        print("20 employee_id")
        print("21  Exit")
        option = input("Enter your choice (1, 2, 3, 4, 5, 6, 7, 8 ,9 , 10 ,11, 12 , 13 , 14 ,15, 16 , 17, 18,19,20,21): ")

        if option == '1':
            add_new_employee(connection)
        elif option == '2':
            view_employee_details(connection)
        elif option == '3':
            cursor = connection.cursor()
            update_employee_info(connection, cursor)

        elif option == '4':
            delete_inactive_emss1(connection)
        elif option == '5':
            list_all_emss1(connection)
        elif option == '6':
            calculate_total_monthly_salary(connection)
        elif option == '7':
            export_employee_data_to_csv(connection, csv_file_path="/home/nineleaps/Downloads/useme11.csv")
        elif option == '8':
            assign_projects(connection)
        elif option == '9':
            view_employee_projects(connection)
        elif option == '10':
            update_employee_project(connection)
        elif option == '11':
            add_tech_stack_for_employee(connection)
        elif option == '12':
            view_employee_tech_stack(connection)
        elif option == '13':
            search_employee_by_name(connection)
        elif option == '14':
            search_employee_by_tech_stack(connection)
        elif option == '15':
            search_employee_by_project_name(connection)
        elif option == '16':
            sort_emss1_by_salary(connection)
        elif option == '17':
            assign_managers(connection)
        elif option == '18':
            view_manager_details(connection)
        elif option == '19':
            file_path = input("Enter the path to the CSV file: ")
            import_employee_data(connection, file_path)
            # You can process the imported employee data here
            print("Employee data imported successfully.")
        elif option == '20':
            employee_name = input("Enter the name of the employee: ")
            find_employee_id_by_name(connection, employee_name)
        elif option == '21':
            break
        else:
            print("Invalid option. Please try again.")

    if connection.is_connected():
        connection.close()
        print("MySQL connection closed.")


if __name__ == "__main__":
    main()

