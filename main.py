import fileManipulatorFunctions as fmf
from generalFunctions import smartInput
import tkinter as tk

path = r"C:\Users\Caden\Desktop\Code\LessonPlanMaker\databank.txt"

while True:
    option = smartInput("Add Skill (0), Read Skill (1), Read File (2), Create Lesson Plan (3): ",int,(0,3))

    match option:
        case 0:
            name = smartInput("Skill Name: ")
            keypointOne = smartInput("Keypoint One: ")
            keypointTwo = smartInput("Keypoint Two: ")
            keypointThree = smartInput("Keypoint Three: ")
            fmf.addSkill(path,name,[keypointOne,keypointTwo,keypointThree])
        case 1:
            name = smartInput("Skill Name: ",str)
            fmf.readSkill(path, name)
        case 2:
            fmf.readFile(path)
        case 3:
            Class = smartInput("Class: ")
            qtr = smartInput("Quarter: ")
            week = smartInput("Week: ")
            skills = smartInput("Skills: ")
            print(skills)
            fmf.createLessonPlan(path,Class,qtr,week,skills.split(","))