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