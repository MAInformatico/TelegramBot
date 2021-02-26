class checker:

    def getTemperature(self):
        with open("temperature.txt", "r") as f: #verify path
            value = f.read()

        return value

    def getHosts(self):
        with open("hosts.txt","r") as f:
            hosts = f.read()

        return hosts

