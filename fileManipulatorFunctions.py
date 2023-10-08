from typing import List

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
    file = createFile(f"{Class} Qtr {quarter} Week {week}.txt")
    if file != None:
        for skill in skills:
            file.write(readSkill(database,skill))
        print("File Created Successfuly")
    else:
        print("Error creating lesson plan")