import fileManipulatorFunctions as fm
import generalFunctions as gf

path = r"C:\Users\ctate0455\Desktop\LessonPlanMaker\databank.txt"

option = gf.smartInput("Add Skill (0), Read Skill (1), Read File (2): ",int,(0,2))

match option:
    case 0:
        name = input("Skill Name: ")
        keypoints = input("Keypoints: ")
        fm.addSkill(path,name,keypoints.split(","))