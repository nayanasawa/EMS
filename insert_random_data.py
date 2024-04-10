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
