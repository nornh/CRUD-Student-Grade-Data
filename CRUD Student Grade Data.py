import sys
import csv
import os
import pyinputplus as pypi
from tabulate import tabulate

# Function to display value data
def ShowData(dbDataNilai):
    print("\nData Graduation Rate of Maju Jaya Junior High School\n")
    data = list(dbDataNilai.values())[1:]
    header = dbDataNilai['column']
    print(tabulate(data, header, tablefmt="pretty"))

def SubMenu():
    print("\nData on graduation scores of Maju Jaya Junior High School students\n")
    while True:
        # Display the main sub menu of the menu program
        choice = ["List of Overall Student Grades",
                  "Search for Student Score List",
                  "Back"]
        response = pypi.inputMenu(choices=choice, numbered=True)
        if response == choice[0]:
            ShowData(dbDataNilai)
        elif response == choice[1]:
            CariData()
        elif response == choice[2]:
            main()

def CariData():
    print("\nSearch for Student Score List\n")
    while True:
        choice = ["Search Graduation Data List",
                  "Search Student Name",
                  "Back"]
        response = pypi.inputMenu(choices=choice, numbered=True)
        if response == choice[0]:
            Ket = pypi.inputStr(prompt='Enter a description (Pass/No Pass):',
                                applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])
            print("List of Searched Data")
            for i, value in dbDataNilai.items():
                if Ket in value:
                    print(f"""
                            NO.ID\t\t : {value[0]}
                            Name\t : {value[1]}
                            Finall Score\t : {value[7]}
                            Description\t : {value[8]}\n
                            """)
                    continue
                elif i == 'column':
                    continue
                elif i == len(dbDataNilai) - 1:
                    print("Not Available")
                    break
        elif response == choice[1]:
            # displays a list of specific student grade data
            NamaSiswa = pypi.inputStr(prompt='Enter the student name: ',
                                      applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])
            for i, value in dbDataNilai.items():
                if i == 'column':
                    continue
                if NamaSiswa in value:
                    print("List of Searched Data")
                    print(f"""
                        No.ID\t\t : {value[0]}
                        Name\t : {value[1]}
                        Minimum Criteria Score : {value[2]}
                        INA Score\t : {value[3]}
                        ENG Score\t :  {value[4]}
                        Scie Score\t : {value[5]}
                        Math Score\t : {value[6]}
                        Finall Score\t : {value[7]}
                        Description\t : {value[8]}\n
                        """)
                    break
                elif i == len(dbDataNilai) - 1:
                    print("Not Available")
                    CariData()
        else:
            SubMenu()

def AddData():
    NamaSiswa = ""  # Declare NamaSiswa outside the loop
    while True:
        choice = ["Display Overall Data",
                  "Add New Student Data",
                  "Back"]
        response = pypi.inputMenu(choices=choice, numbered=True)

        if response == choice[0]:
            ShowData(dbDataNilai)
        elif response == choice[1]:
            while True:
                print("""
                      Instructions for filling in the ID number
                      Example:
                            No.ID = 2023001
                      =======Example Explanation=======
                      The first two digits of the student's entry year (2020) = 20
                      Two numbers following the student's graduation year (2023) = 23
                      Last three digits of student registration number 001
                      """)
                indukSiswa = pypi.inputInt(prompt='Input ID Number\t: ', greaterThan=0, blockRegexes=[r'[a-zA-Z]'])
                
                # Check if ID already exists
                if str(indukSiswa) in dbDataNilai:
                    print("ID number already exists. Please enter a different ID.")
                    continue
                elif len(str(indukSiswa)) != 7:
                    print("ID number must be 7 digits")
                    continue
                else:
                    print("\n--------Input New Data--------")
                    NamaSiswa = pypi.inputStr(prompt='Name\t\t\t: ', applyFunc=lambda x: x.capitalize(),
                                              blockRegexes=[r'[0-9]'])
                    NKKM = pypi.inputFloat(prompt='Minimum criteria score\t: ', greaterThan=0,
                                           blockRegexes=[r'[a-zA-Z]'])
                    NBIndo = pypi.inputFloat(prompt='INA score\t\t: ', greaterThan=0, blockRegexes=[r'[a-zA-Z]'])
                    NBIng = pypi.inputFloat(prompt='ENG score\t\t: ', greaterThan=0, blockRegexes=[r'[a-zA-Z]'])
                    NIPA = pypi.inputFloat(prompt='Sciene score\t\t: ', greaterThan=0, blockRegexes=[r'[a-zA-Z]'])
                    NMTK = pypi.inputFloat(prompt='Math score\t\t: ', greaterThan=0, blockRegexes=[r'[a-zA-Z]'])
                    NA = (NBIndo + NBIng + NIPA + NMTK) / 4

                    if NA >= NKKM:
                        Ket = "Pass"
                    else:
                        Ket = "No Pass"

                    # print the recalled data
                    print("\n\n--------New Data Student--------")
                    print(f"ID Nummber \t\t: {indukSiswa}")
                    print(f"Name\t\t\t: {NamaSiswa}")
                    print(f"Minimum Criteria Score\t: {NKKM}")
                    print(f"INA Score\t\t: {NBIndo}")
                    print(f"ENG Score\t\t: {NBIng}")
                    print(f"Science Score\t\t: {NIPA}")
                    print(f"Math Score\t\t: {NMTK}")
                    print(f"Final Score\t\t: {NA}")
                    print(f"Description\t\t: {Ket}\n")

                    # Ask for confirmation before adding to the table
                    confirmation = pypi.inputYesNo(prompt="Do you want to add this data? (yes/no): ")
                    if confirmation == "yes":
                        dbDataNilai.update({
                            indukSiswa: [
                                indukSiswa,
                                NamaSiswa,
                                NKKM,
                                NBIndo,
                                NBIng,
                                NIPA,
                                NMTK,
                                NA,
                                Ket
                            ]
                        })
                        ShowData(dbDataNilai)
                        break
                    else:
                        print("Data not added.\n")
                        break
        else:
            main()

def UbahData():
    while True:
        choice = ["Display Overall Data",
                  "Edit Student Grade Data List", 
                  "Back"]
        response = pypi.inputMenu(choices=choice, numbered=True)

        if response == choice[0]:
            ShowData(dbDataNilai)
        elif response == choice[1]:
            while True:
                print("""
                      Instructions for filling in the ID number
                      Example:
                            No.ID = 2023001
                      =======Example Explanation=======
                      The first two digits of the student's entry year (2020) = 20
                      Two numbers following the student's graduation year (2023) = 23
                      Last three digits of student registration number 001
                      """)
                indukSiswa = pypi.inputInt(prompt='Input ID Number: ', greaterThan=0, blockRegexes=[r'[a-zA-Z]'])

                # Convert indukSiswa to string
                indukSiswa_str = str(indukSiswa)

                try:
                    # Check if ID exists before attempting to edit
                    if indukSiswa_str in dbDataNilai:
                        # Get the student data
                        student_data = dbDataNilai[indukSiswa_str]
                        
                        # Display the current data
                        print("\nCurrent Data:")
                        print(f"No.ID\t\t : {student_data[0]}")
                        print(f"Name\t : {student_data[1]}")
                        print(f"Minimum Criteria Score\t : {student_data[2]}")
                        print(f"INA Score\t\t: {student_data[3]}")
                        print(f"ENG Score\t\t: {student_data[4]}")
                        print(f"Science Score\t\t: {student_data[5]}")
                        print(f"Math Score\t\t: {student_data[6]}")
                        print(f"Final Score\t\t: {student_data[7]}")
                        print(f"Description\t\t: {student_data[8]}\n")

                        # Prompt for the field to edit
                        field_choices = ["Minimum criteria score", "INA score", "ENG score", "Science score", "Math Score"]
                        field_response = pypi.inputMenu(choices=field_choices, numbered=True)
                        
                        # Prompt for the updated value
                        update_val = pypi.inputFloat(prompt=f'{field_response}: ', greaterThan=0, blockRegexes=[r'[a-zA-Z]'])
                        
                        # Save the original data for later comparison
                        original_data = student_data.copy()
                        
                        # Update the data
                        student_data[field_choices.index(field_response) + 2] = update_val
                        
                        # Process calculating the final score
                        NA = sum(student_data[3:7]) / 4
                        
                        # Update the final score and description
                        student_data[7] = NA
                        student_data[8] = "Pass" if NA >= student_data[2] else "No Pass"
                        
                        # Display the updated data
                        print("\nUpdated Data:")
                        print(f"No.ID\t\t : {original_data[0]}")
                        print(f"Name\t : {original_data[1]}")
                        print(f"Modified Data\t : {field_response} - {original_data[field_choices.index(field_response) + 2]} to {update_val}\n")
                        
                        # Ask for confirmation before saving changes
                        confirmation = pypi.inputYesNo(prompt="Do you want to save these changes? (yes/no): ")
                        if confirmation == "yes":
                            print("Changes saved successfully.")
                            UbahData()
                        else:
                            # If the user chooses not to save changes, revert to the original data
                            dbDataNilai[indukSiswa_str] = original_data
                            print("Changes reverted.")
                            UbahData()
                            break
                    else:
                        print("ID number not found. Please try again.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            break
        else:
            main()


def delete():
    while True:
        choice = ["Display Overall Data",
                  "Delete Student Grade Data List",
                  "Back"]
        response = pypi.inputMenu(choices=choice, numbered=True)
        if response == choice[0]:
            ShowData(dbDataNilai)
        
        elif response == choice[1]:
            print("""
                  Instructions for filling in the ID number
                  Example:
                        No.ID = 2023001
                  =======Example Explanation=======
                  The first two digits of the student's entry year (2020) = 20
                  Two numbers following the student's graduation year (2023) = 23
                  Last three digits of student registration number 001
                  """)
            indukSiswa = pypi.inputInt(prompt='Input ID Number: ', greaterThan=0, blockRegexes=[r'[a-zA-Z]'])
            
            # Convert indukSiswa to string
            indukSiswa_str = str(indukSiswa)

            # Check if ID does not exist before attempting to delete
            if indukSiswa_str not in dbDataNilai.keys():
                print("ID number is not available")
                continue

            elif len(indukSiswa_str) != 7:
                print("ID number must be 7 digits")
                continue

            # Delete data based on student identification number
            else:
                student_data = dbDataNilai[indukSiswa_str]
                print("Student grade data to be deleted")
                print(f"""
                        No.ID\t\t : {student_data[0]}
                        Name\t : {student_data[1]}
                        Minimum Criteria Score\t : {student_data[2]}
                        INA Score\t : {student_data[3]}
                        ENG Score\t :  {student_data[4]}
                        Science Score\t : {student_data[5]}
                        Math Score\t : {student_data[6]}
                        Final Score\t : {student_data[7]}
                        Description\t : {student_data[8]}\n
                        """)
                responsedelete = pypi.inputYesNo(prompt="Continue to delete? (yes/no) ")
                if responsedelete == "yes":
                    del dbDataNilai[indukSiswa_str]
                    ShowData(dbDataNilai)
                    break  # Exit the loop after deleting data
                elif responsedelete == "no":
                    break  # Exit the loop if deletion is not confirmed
        else:
            main()
            break  # Exit the loop after returning to the main menu


def main():
    global dbDataNilai
    while True:
        # Display the program's main view
        print(
            """
            Report Graduation Data at Maju Jaya Junior High School
            """
        )
        # Input the feature to be executed
        prompt = "Choose the menu number you want to run\n"
        choice = ["Displays a list of student grade data",
                  "Add student data",
                  "Change student data",
                  "Delete student data",
                  "Exit"]
        response = pypi.inputMenu(prompt=prompt, choices=choice, numbered=True)

        # Fitur menampilkan daftar nilai siswa
        if response == choice[0]:
            SubMenu()
        # Fitur menambahkan daftar nilai siswa
        elif response == choice[1]:
            AddData()
        # Fitur mengubah daftar nilai siswa
        elif response == choice[2]:
            UbahData()
        # Fitur menghapus daftar nilai siswa
        elif response == choice[3]:
            delete()
        # Fitur exit program
        else:
            keluar = pypi.inputYesNo("Are you sure you want to quit? (yes/no) ")
            if keluar == "no":
                continue
            else:
                # Pada bagian penyimpanan data
                with open(pathDataNilai, 'w', newline='') as fileDataNilai:
                    writer = csv.writer(fileDataNilai, delimiter=';')
                    columns = dbDataNilai['column']
                    writer.writerow(columns)

                    # Mulai dari indeks 1 untuk menghindari header
                    for values in list(dbDataNilai.values())[1:]:
                        if isinstance(values, list):
                            writer.writerow(values)
                print("Data saved successfully.")
                sys.exit()

# Setting the path of the database file
pathDataNilai = r'E:\MyProject\CRUD-Student-Grade-Data\DataNilai.csv'
# Check the database contents, if empty, display a message.
if os.path.getsize(pathDataNilai) == 0:
    print('Database is empty, please enter available Data first')
else:
    #Importing the database file
    with open(pathDataNilai, 'r') as fileDataNilai:
        reader = csv.reader(fileDataNilai, delimiter=";")
        headingsDataNilai = next(reader)
        dbDataNilai = {"column": headingsDataNilai}

        for row in reader:
            dbDataNilai.update(
                {
                    str(row[0]): [
                        int(row[0]),
                        str(row[1]),
                        float(row[2]),
                        float(row[3]),
                        float(row[4]),
                        float(row[5]),
                        float(row[6]),
                        float(row[7]),
                        str(row[8])
                    ]
                }
            )
    # Run the main program
    main()