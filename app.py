# loading weather from file to list
weatherFilePath = "./weather_history.txt"
f = open(weatherFilePath, "r")
header = f.readline().split()
labels = [header[0], header[2], header[5], header[8], header[13]]
values = []
for line in f: 
    record = line.split()
    values.append([record[0], record[2], record[5], record[8], record[13]])

# loading asthma factors from file to list
asthmaFactorsFilePath = "./asthma_factors_history.txt"
f = open(asthmaFactorsFilePath, "r")
days = []
for line in f: 
    line = line.split()
    day = []
    for el in line:
        day.append(el)
    days.append(day)

# tests
print(">>> Weather <<<")
print(labels)
print(values)

print(">>> Asthma factors <<<")
print(days)