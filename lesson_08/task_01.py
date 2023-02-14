import csv


name = input('Name: ')
surname = input('Surname: ')
age = int(input('Age: '))


with open('file_07.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name', 'surname', 'age'])
    writer.writerow([name, surname, age])