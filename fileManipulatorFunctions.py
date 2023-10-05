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
        print("Added Successfully")
    except Exception as e:
        print(f"Failed to Add: {e}")
    file.close()

def readFile(path:str):
    file = openFile(path, "r")
    try:
        print(f"Read Successfully\n{file.read()}")
    except Exception as e:
        print(f"Failed to Read File: {e}")

def readSkill(path:str,name:str):
    file = openFile(path,"r")
    for line in file:
        if name in line:
            print(f"Read Successfully\n{line}")
            return
    print(f"{name} Not Found")

def createFile(name:str):
    file = None
    try:
        file = open(name,"x")
    except:
        print("File already exists")
    return file

def createLessonPlan(Class:str,quarter:int,week:int,skill:str):
    file = createFile(f"{Class}{quarter}{week}.txt")
    if file == None:
        return