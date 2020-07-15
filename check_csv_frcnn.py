import csv

file=open("All_bajaj_2.csv", "r")
reader = csv.reader(file)
count = 0
for line in reader:
    if int(line[7]) > int(line[2]):
        fl = open('incorrect.csv', 'a+')
        datavd = line[0]+","+line[3]+","+line[7]+","+line[2]
        fl.write(datavd)
        fl.write('\n')
        fl.flush()

        print(line[0], line[3])
        print(line[7], line[2])
        count += 1
print(count)
