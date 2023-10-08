from typing import List
from openpyxl import Workbook
from openpyxl import styles

def openFile(path:str, mode:str) -> str:
    file = None
    try:
        file = open(path, mode)
        print("Opened Successfully")
    except Exception as e:
        print(f"File Failed to Open: {e}")
    return file
    
def addSkill(path:str, name:str, keypoints:List[str]):
    file = openFile(path, "a")
    try:
        file.write(f"\n{name},{keypoints}")
        print("Skill Added Successfully")
    except Exception as e:
        print(f"Failed to Add Skill: {e}")
    file.close()

def readFile(path:str):
    file = openFile(path, "r")
    try:
        print(f"File Read Successfully\n{file.read()}")
    except Exception as e:
        print(f"Failed to Read File: {e}")

def readSkill(path:str,name:str):
    file = openFile(path,"r")
    for line in file:
        if name in line:
            print(f"Read Successfully\n{line}")
            return line
    print(f"{name} Not Found")

def createFile(name:str):
    file = None
    try:
        file = open(name,"x")
    except:
        print("File already exists")
    return file

def createLessonPlan(database:str,Class:str,quarter:int,week:int,skills:List[str]):
    wb = Workbook()
    sheet = wb.active
    sheet["A1"] = "Section"
    sheet["B1"] = "Time"
    sheet["C1"] = "Excercise / Layers"
    sheet["D1"] = "Format / Equipment"
    sheet["E1"] = "Key Points"

    sheet["A2"] = "Bow In"
    sheet["B2"] = "2"
    sheet["C2"] = "Bow In"
    sheet["D2"] = "Line Up"
    sheet["E2"] = "Stand Still"

    formatSpreadsheet(sheet)
    wb.save(f"{Class} Qtr {quarter} Week {week}.xlsx")
    wb.close()

def formatSpreadsheet(sheet):
    cols = ["A","B","C","D","E"]
    width = [15.13,5.13,25.13,16.38,12.63]

    for i, col in enumerate(cols):
        sheet.column_dimensions[col].width = width[i]
        sheet.cell(1,i+1).alignment = styles.Alignment("center")

def addSkillToSpreadsheet():