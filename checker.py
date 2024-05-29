import re

class checker:

    def get_ips(self,thefile): #read all the IP from thefile parameter. Return a list containing the IPs
        logfile = list(open(str(thefile), 'r').read().split('\n'))
        newip = []
        for entry in logfile:
            ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', entry)
            for ip in ips:
                newip.append(ip)
        return newip

    def read_file(self,thefile): #Return a dictionary after read IP and hostname form a file and store them in the mentioned dictionary with key: IP and value: hostname.
        with open(str(thefile),'r') as f: #format file: "IP<space>hostname"
            auxlist = []
            ip_not_found = True
            for line in f:
                ip_not_found = False
                auxlist.append(line.rstrip())

        dictionary = {}
        for i in range(len(auxlist)):
            auxlist[i] = auxlist[i].split(" ")
        dictionary = dict(auxlist)

        return dictionary

    def get_hostname(self, ip,thefile): #given a IP, return the hostname
        data = self.readFile(thefile)
        return data.get(ip)


    def get_temperature(self):
        with open("temperature.txt", "r") as f: #verify path
            value = f.read()

        return value

    def get_hosts(self):
        hosts_list = []
        keylist = self.getIPs("hosts.txt") #get IPs from hosts.txt (more details about it on: https://github.com/MAInformatico/Raspberry-Pi-Monitoring-Network/tree/master/RaspberryPiFiles )
        for i in range(len(keylist)):
            hosts_list.append(self.getHostname(keylist[i],"dictionary.txt")) #where dictionary.txt is the file that contains my "DNS file" Please, create your own file dictionary.txt

        if "None" in hosts_list:
            print("Unknown device")
            return "There is an unknown devices!!"
        #print(hostsList)
        else:
            return hosts_list

