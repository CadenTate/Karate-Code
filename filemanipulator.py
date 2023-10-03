def openFile(path:str, mode:str) -> str:
    file = None
    try:
        file = open(path, mode)
        print("Opened Successfully")
    except Exception as e:
        print(f"File Failed to Open: {e}")
    return file
    
def addSkill(path:str, name:str):
    file = openFile(path, "a")
    try:
        file.write(f"\n{name}")
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