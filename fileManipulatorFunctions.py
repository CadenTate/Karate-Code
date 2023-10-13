from typing import List, IO, Optional
from openpyxl import Workbook, styles

def openDatabase(database:str, mode:str) -> Optional[IO]:
    file = None
    try:
        file = open(database, mode)
        print("Opened Successfully")
    except Exception as e:
        print(f"File Failed to Open: {e}")
    return file
    
def addSkill(database:str, name:str, keypoints:List[str]) -> None:
    file = openDatabase(database, "a")
    if file is not None:    
        try:
            file.write(f"\n{name},{keypoints}")
            print("Skill Added Successfully")
        except Exception as e:
            print(f"Failed to Add Skill: {e}")
        finally:
            file.close()

def readFile(database:str) -> None:
    file = openDatabase(database, "r")
    if file is not None:
        try:
            print(f"File Read Successfully\n{file.read()}")
        except Exception as e:
            print(f"Failed to Read File: {e}")

def readSkill(database:str,skillName:str) -> Optional[str]:
    file = openDatabase(database,"r")
    if file is not None:
        for line in file:
            if skillName in line:
                print(f"Read Successfully\n{line}")
                return line
    print(f"{skillName} Not Found")

def createFile(name:str) -> Optional[IO]:
    file = None
    try:
        file = open(name,"x")
    except:
        print("File already exists")
    return file

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
        skillOne = skillOne.split(",")
        sheet["A9"] = skillOne[0]

    wb.save(f"{Class} Qtr {quarter} Week {week}.xlsx")
    wb.close()

    return saveLocation

def formatSpreadsheet(sheet):
    cols = ["A","B","C","D","E"]
    width = [15.13,5.13,25.13,16.38,12.63]

    for i, col in enumerate(cols):
        sheet.column_dimensions[col].width = width[i]
        sheet.cell(1,i+1).alignment = styles.Alignment("center")

def initialSetup(sheet):
    # Headings
    sheet["A1"] = "Section"
    sheet["B1"] = "Time"
    sheet["C1"] = "Excercise / Layers"
    sheet["D1"] = "Format / Equipment"
    sheet["E1"] = "Key Points"

    # Section 1
    sheet["A2"] = "Bow In"
    sheet["B2"] = "2"
    sheet["C2"] = "Bow In"
    sheet["D2"] = "Line Up"
    sheet["E2"] = "Stand Still"
    sheet["E3"] = "Participate"

    # Section 2
    sheet["A4"] = "Warm Up"
    sheet["E4"] = "Fast"
    sheet["E5"] = "Participate"