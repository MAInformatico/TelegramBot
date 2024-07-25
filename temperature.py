import os, sys, subprocess
#from avg import avg

#getting the current system temperature
command  = "sudo /usr/bin/vcgencmd measure_temp"
currentResult = os.popen(command).read()
currentResult = currentResult[5:9]
#reading the file
with open('temperature.txt', 'r') as f:
    lineas = [linea.split("=") for linea in f]
f.close()
temperatureReaded = ' '
#reading the file's temperature
for linea in lineas:
    temperatureReaded = linea[0]

#parsing
temperatureReaded = temperatureReaded[:4]

f = open('temperature.txt', 'w')
if currentResult > temperatureReaded:
    f.write ("The temperature is increased, current temperature: \n" + currentResult + "\n")
else:
    f.write ("The temperature is decreased, current temperature: \n" + currentResult + "\n")
f.close()

f = open('history_temperature.txt','a')
f.write(currentResult + '\n')
f.close()