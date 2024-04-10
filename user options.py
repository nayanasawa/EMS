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