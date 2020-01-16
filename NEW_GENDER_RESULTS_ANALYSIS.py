import os
import pandas as pd

path = "/Users/sararodriguez/Desktop"

os.chdir(path)
print(os.getcwd())

#idiot code test for 0% mean and 0% standard deviation for correct answers
for filename in os.listdir(os.getcwd()):
    # load excel files
    if 'IdiotTest00.xlsx' in filename:

        print(filename)
        data = pd.read_excel(filename, skiprows=3)

        # calculating the mean
        mean1 = data['correct'].mean()

        print('Mean of correct answers: ' + str(mean1))

#idiot code test for 100% mean and 0% standard deviation for correct answers
for filename in os.listdir(os.getcwd()):
    # load excel files
    if 'IdiotTest01.xlsx' in filename:

        print(filename)
        data = pd.read_excel(filename, skiprows=3)

        # calculating the mean and standard deviation
        mean1 = data['correct'].mean()
        print('Mean of correct answers: ' + str(mean1))

#code for 'philadelphia tests results' files

# change current directory
path = "/Users/sararodriguez/Desktop/New_Gender_Results"
os.chdir(path)
print(os.getcwd())

os.listdir(os.getcwd())
print(os.listdir(os.getcwd()))

for filename in os.listdir(os.getcwd()):
    # load csv files
    if 'new_gender_' in filename:

        print(filename)
        data = pd.read_csv(filename, skiprows=3)

        # calculating the mean
        mean1 = data['correct'].mean()
        print('Mean of correct answers: ' + str(mean1))

import statistics

data2 = [0.92, 0.8, 0.92, 0.98, 0.72, 0.88, 0.80, 0.82, 0.94, 0.84, 0.72, 0.80, 0.88, 0.66, 0.58, 0.80, 0.74,
         0.82, 0.82, 0.90, 0.90, 0.78, 0.80, 0.60,0.94, 0.90, 0.84, 0.92, 0.92, 0.80, 0.64, 0.82, 0.72, 0.80,
         0.76, 0.82, 0.92, 0.90, 0.70, 0.92, 0.88, 0.72, 0.78, 0.80, 0.82, 0.88, 0.92, 0.70]

x = statistics.mean(data2)
print(x)

y = statistics.stdev(data2)
print(y)


