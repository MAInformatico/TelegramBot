def avg():
        lineas =  open('history_temperature.txt')
        sum=0
        count=0
        for linea in lineas:
                if linea == ' ':
                        pass
                else:
                    sum+=float(linea)
                count+=1
        return str(round(sum/count,2))

def show():
    print('The average is: ' + avg() + '\n')

show()