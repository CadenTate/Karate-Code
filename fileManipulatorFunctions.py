from typing import List, IO, Optional
from openpyxl import Workbook, styles

# Opens the database
def openDatabase(database:str, mode:str) -> Optional[IO]:
    file = None
    try:
        file = open(database, mode)
        print("Opened Successfully")
    except Exception as e:
        print(f"File Failed to Open: {e}")
    return file

# Adds skill to database in <name,[keypoints]> format
def addSkill(database:str, type:str,name:str, keypoints:List[str]) -> None:
    file = openDatabase(database, "a")
    if file is not None:    
        try:
            file.write(f"\n{type},{name},{keypoints[0]},{keypoints[1]},{keypoints[2]}")
            print("Skill Added Successfully")
        except Exception as e:
            print(f"Failed to Add Skill: {e}")
        finally:
            file.close()

# Calls openDatabase then returns the file
def readFile(database:str) -> None:
    file = openDatabase(database, "r")
    if file is not None:
        try:
            return file.read()
        except Exception as e:
            print(f"Failed to Read File: {e}")
        file.close()

# Returns searched for skill
def readSkill(database:str,skillName:str) -> Optional[str]:
    file = openDatabase(database,"r")
    if file is not None:
        for line in file:
            line = line.split(",")
            if line[1] == skillName:
                return line
    print(f"{skillName} Not Found")

# Creates a new file
def createFile(name:str) -> Optional[IO]:
    file = None
    try:
        file = open(name,"x")
    except:
        print("File already exists")
    return file

# Creates a new Lesson plan
def createLessonPlan(saveLocation:str,database:str,Class:str,quarter:int,week:int,skillOneName:str,skillTwoName:str) -> str:
    wb = Workbook()
    sheet = wb.active

    if sheet is None:
        return "Workbook Creation Error"

    initialSetup(sheet)
    formatSpreadsheet(sheet)
        
    skillOne = readSkill(database,skillOneName)
    skillTwo = readSkill(database,skillTwoName)

    if skillOne != None:
        sheet["A9"] = skillOne[0] # type: ignore
        sheet["C9"] = skillOne[1] # type: ignore
        sheet["E9"] = skillOne[2] # type: ignore
        sheet["E10"] = skillOne[3] # type: ignore
        sheet["E11"] = skillOne[4] # type: ignore


    if skillTwo != None:
        skillTwo = skillTwo.split(",")
        sheet["A17"] = skillTwo[0] # type: ignore
        sheet["C17"] = skillTwo[1] # type: ignore
        sheet["E17"] = skillTwo[2] # type: ignore
        sheet["E18"] = skillTwo[3] # type: ignore
        sheet["E19"] = skillTwo[4] # type: ignore
        

    wb.save(f"{Class} Qtr {quarter} Week {week}.xlsx")
    wb.close()

    return saveLocation

# Initial formating of spreadsheet
def formatSpreadsheet(sheet):
    cols = ["A","B","C","D","E"]
    width = [15,5,25,15,15]

    for i, col in enumerate(cols):
        sheet.column_dimensions[col].width = width[i]
        sheet.cell(1,i+1).alignment = styles.Alignment("center")

# Adds Lesson Plan constants
def initialSetup(sheet):
    # Headings
    sheet["A1"] = "Section"
    sheet["B1"] = "Time"
    sheet["C1"] = "Excercise / Layers"
    sheet["D1"] = "Format / Equipment"
    sheet["E1"] = "Key Points"

    # Bow In
    sheet["A2"] = "Bow In"
    sheet["B2"] = "2"
    sheet["C2"] = "Bow In"
    sheet["D2"] = "Line Up"
    sheet["E2"] = "Stand Still"
    sheet["E3"] = "Participate"

    # Warm up
    sheet["A4"] = "Warm Up"
    sheet["E4"] = "Fast"
    sheet["E5"] = "Participate"

    # Mat Chat
    sheet["A15"] = "Mat Chat"
    sheet["D15"] = "Horseshoe"
    sheet["E15"] = "Sit Still"
    sheet["E16"] = "Listening"

    # HEF
    sheet["A24"] = "High Energy Finish"
    sheet["B24"] = "6"

    # Announcements
    sheet["A27"] = "Announcements"
    sheet["B27"] = "3"
    sheet["C27"] = "Announcements"
    sheet["D27"] = "Line Up"
    sheet["E27"] = "Stand Still"
    sheet["E28"] = "Quiet"

    # End Class
    sheet["A29"] = "End Class"
    sheet["B29"] = "2"
    sheet["D29"] = "Line Up"