import fileManipulatorFunctions as fmf
from generalFunctions import smartInput
import tkinter as tk

dataBase = r"databank.txt"
saveLocation = r"C:\Users\ctate0455\Desktop\Lesson Plans"

while True:
    option = smartInput("Add Skill (0), Read Skill (1), Read File (2), Create Lesson Plan (3), Edit Lesson Plan (4): ",int,(0,4))

    match option:
        case 0:
            fmf.addSkill(dataBase)
        case 1:
            name = smartInput("Skill Name: ",str)
            print(fmf.readSkill(dataBase, name))
        case 2:
            print(fmf.readFile(dataBase))
        case 3:
            Class = smartInput("Class: ")
            qtr = smartInput("Quarter: ")
            week = smartInput("Week: ")
            skillOne = smartInput("Skill One: ")
            skillTwo = smartInput("Skill Two: ")
            fmf.createLessonPlan(saveLocation,dataBase,Class,qtr,week,skillOne,skillTwo)
        case 4: 
            pass