import math
inputFile = open('a.txt', 'r')#input file here
outputFile = open("a_out.txt", "w") #output file here

fiveNumbers = inputFile.readline().split("\n")[0].split()
d= int(fiveNumbers[0])
i= int(fiveNumbers[1])
s= int(fiveNumbers[2])
v= int(fiveNumbers[3])
f= int(fiveNumbers[4])

intersections={}
streetsDict = {}
carPaths = []
sortedStreets = {}
streetPriority = {}
for i in range(s):
    desc = inputFile.readline().split()
    streetsDict[desc[2]] = desc
for i in range(v):
    path = inputFile.readline().split()
    timeRequired = 0;
    for street in path[1:]:
        streetDesc = streetsDict[street]
        timeRequired+=int(streetDesc[3])
    if(timeRequired<=d):
        carPaths.append(path)
        for street in path[1:]:
            if(streetsDict[street][1] in intersections and street not in intersections[streetsDict[street][1]]):
                intersections[streetsDict[street][1]].append(street)
            else:
                intersections[streetsDict[street][1]] = [street]
            
            if(street in sortedStreets):
                sortedStreets[street] = [sortedStreets[street][0]+1, int(streetsDict[street][3])]
            else:
                sortedStreets[street] = [1, int(streetsDict[street][3])]


for s in sortedStreets:
    streetPriority[s] = sortedStreets[s][0]/sortedStreets[s][1]



intersectionsToUse = [];
for i in intersections:
    for j in intersections[i]:
        if(j in streetPriority):
            intersectionsToUse.append(i)
            break

        

outputFile.write(str(len(intersections)) + "\n")

for i in intersectionsToUse:
    outputFile.write(i + "\n")
    outputFile.write(str(len(intersections[i])) + "\n")
    for s in intersections[i]:
        duration = math.ceil(streetPriority[s]*2)
        outputFile.write(s + " " + str(duration)+"\n")



inputFile.close()
outputFile.close()
