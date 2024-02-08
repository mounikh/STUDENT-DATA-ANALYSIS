import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the Excel file
df = pd.read_csv('education_data.csv')

# Calculate the average age of male and female students
avg_age_male = df[df['gender'] == 'Male']['age'].mean()
avg_age_female = df[df['gender'] == 'Female']['age'].mean()
print("Average age of male students: ", avg_age_male)
print("Average age of female students: ", avg_age_female)

# Calculate the grade distribution for male and female students
grade_dist_male = df[df['gender'] == 'Male']['grade'].value_counts()
grade_dist_female = df[df['gender'] == 'Female']['grade'].value_counts()
print("\nGrade distribution of male students:")
print(grade_dist_male)
print("\nGrade distribution of female students:")
print(grade_dist_female)

# Calculate the overall grade distribution
grade_dist_overall = df['grade'].value_counts()
print("\nOverall grade distribution:")
print(grade_dist_overall)

# Calculate the attendance percentage for male and female students
attendance_male = df[df['gender'] == 'Male']['attendance'].mean()
attendance_female = df[df['gender'] == 'Female']['attendance'].mean()
print("\nAverage attendance percentage of male students: ", attendance_male)
print("Average attendance percentage of female students: ", attendance_female)

# Calculate the average attendance percentage
average_attendance = df['attendance'].mean()
print("\nAverage attendance percentage: ", average_attendance)

# Get the number of male and female students
num_male = df[df['gender'] == 'Male'].shape[0]
num_female = df[df['gender'] == 'Female'].shape[0]
print("\nNumber of male students: ", num_male)
print("Number of female students: ", num_female)

# Get the number of students in each subject
subject_counts = df['subject'].value_counts()
print("\nSubject counts:")
print(subject_counts)

# Calculate the minimum, maximum, and median age of students
min_age = df['age'].min()
max_age = df['age'].max()
median_age = df['age'].median()
print("\nMinimum age: ", min_age)
print("Maximum age: ", max_age)
print("Median age: ", median_age)

# Create a bar chart of the grade distribution
grade_dist_plot = df['grade'].value_counts().plot(kind='bar')
plt.title('Grade Distribution')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.show()

# Create a pie chart of the overall grade distribution
labels = grade_dist_overall.index
sizes = grade_dist_overall.values
colors = ['#f7b6d2', '#ffebd2', '#d2ebf7', '#b6d2f7', '#d2f7b6']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Overall Grade Distribution')
plt.show()
