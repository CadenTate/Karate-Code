import fileManipulatorFunctions as fmf
from generalFunctions import smartInput
import tkinter as tk

path = r"C:\Users\ctate0455\Desktop\LessonPlanMaker\databank.txt"

option = smartInput("Add Skill (0), Read Skill (1), Read File (2): ",int,(0,2))

match option:
    case 0:
        name = input("Skill Name: ")
        keypointOne = input("Keypoint One: ")
        keypointTwo = input("Keypoint Two: ")
        keypointThree = input("Keypoint Three: ")
        fmf.addSkill(path,name,[keypointOne,keypointTwo,keypointThree])
    case 1:
        name = smartInput("Skill Name: ",str)
        fmf.readSkill(path, name)
    case 2:
        fmf.readFile(path)
    case 3:
        fmf.createLessonPlan()