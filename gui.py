import tkinter as tk

window = tk.Tk()

readFileButton = tk.Button(text="Read File",width=15,height=1)
addSkillButton = tk.Button(text="Add Skill",width=15,height=1)
readSkillButton = tk.Button(text="Read Skill",width=15,height=1)
for button in (addSkillButton,readSkillButton,readFileButton):
    button.pack()
window.mainloop()