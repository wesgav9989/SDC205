# Wesley Gavitt
# WESGAV9989
# 4.7 Performance Assessment

import pandas as pd
import matplotlib.pyplot as plt

print("WESGAV9989")

students = [
    "Wesley", "James", "Maria", "Ava", "Liam",
    "Sophia", "Noah", "Olivia", "Mason", "Emma"
]

subjects = ["Math", "Science"]

grades = [
    [95, 90],
    [88, 84],
    [92, 89],
    [76, 81],
    [85, 87],
    [91, 94],
    [79, 83],
    [98, 96],
    [82, 80],
    [87, 86]
]

gradeFrame = pd.DataFrame(
    grades,
    index=students,
    columns=subjects
)

# Calculate average of each subject
averageGrades = gradeFrame.mean()

# Convert to DataFrame so output matches sample
averageFrame = pd.DataFrame(
    averageGrades,
    columns=["Grade"]
)

averageFrame.index.name = "Subject"

print()
print(averageFrame)

# Bar chart
averageFrame.plot.bar(
    y="Grade",
    legend=False
)

plt.title("Average Grade by Subject")
plt.xlabel("")
plt.ylabel("")
plt.show()
