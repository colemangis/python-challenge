import os
import csv
import inspect

print(os.listdir('Resources/'))
file_path = os.path.join('Resources','budget_data.csv')
print(file_path)
max(int(l.split(',')[1]) for l in open(file_path).readlines())

#with open(file_path) as file:
    
