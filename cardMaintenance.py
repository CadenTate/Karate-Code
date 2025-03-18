import pandas as pd
import tkinter as tk
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")

file = "Membership_" + date + ".csv"

df = pd.read_csv(file)

# Need 1, 2, 3, 4, 12

# print(df[['Participant First Name', 'Participant Last Name', 'Customer First Name', 'Customer Last Name', 'Last Attendance']])

df["Clean Days"] = pd.to_numeric(df["Last Attendance"]
                                 .astype(str)
                                 .str.strip("'")
                                 .str[:-9], 
                                 errors="coerce").fillna(0).astype(int)  # Turns NA to 0 and converts all to int

# print(list(filter(lambda x: x <= 6, df["Clean Days"])))
# print(len(list(filter(lambda x: x > 6 and x <= 13, df["Clean Days"]))))
# print(list(filter(lambda x: x > 13 and x <= 20, df["Clean Days"])))
# print(list(filter(lambda x: x > 20, df["Clean Days"])))

print("ONE WEEK\n", df.loc[(df["Clean Days"] > 6) & (df["Clean Days"] <= 13), ['Participant First Name', "Participant Last Name", 'Clean Days']])
print("\nTWO WEEKS\n", df.loc[(df["Clean Days"] > 13) & (df["Clean Days"] <= 20), ['Participant First Name', "Participant Last Name", 'Clean Days']])
print("\nTHREE WEEKS\n", df.loc[(df["Clean Days"] > 20) & (df["Clean Days"] <= 27), ['Participant First Name', "Participant Last Name", 'Clean Days']])
print("\nFOUR OR MORE WEEKS\n", df.loc[(df["Clean Days"] > 27), ['Participant First Name', "Participant Last Name", 'Clean Days']])

# GUI
# def submit():
#     path = path_var.get()

# root = tk.Tk()

# root.title("Attendance MIA Portal   ")
# root.geometry("600x400")

# path_var = tk.StringVar()

# pathLabel = tk.Label(text="Path to File: ")
# pathEntry = tk.Entry(root, textvariable = path_var)
# submitButton = tk.Button(root, text = "Submit", command = submit)

# pathLabel.grid(row=0, column=0)
# pathEntry.grid(row=0, column=1)
# submitButton.grid(row=1, column=1)

# root.mainloop()

