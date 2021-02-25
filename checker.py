class checker:

    def getTemperature(self):
        with open("temperature.txt", "r") as f: #verify path
            value = f.read()

        return value



