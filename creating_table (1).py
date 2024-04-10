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