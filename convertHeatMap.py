import numpy as np
lines = open('heatmap_data.txt').read().split('\n')
output = ""
for line in lines:
    line = line.split(" ")
    for i in range(len(line)):
        if not i == len(line)-1:
            if len(line[i])>=5:
                output += line[i][0:5] + "\t"
            else:
                output += line[i] + "\t"

        else:
            if len(line[i])>=5:
                output += line[i][0:5]
            else:
                output += line[i]
    output += "\n"

with open('heatmap_data1.txt', 'w') as f:
    f.write(output)
