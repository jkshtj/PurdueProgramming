import os
import sys

class Simulation:
    def __init__(self,simnNo,simDate,chipName,chipCount,chipCost):
        self.simulationNumber = simnNo
        self.simulationDate = simDate
        self.chipName = chipName
        self.chipCount = chipCount
        self. chipCost = chipCost
        self.simulationCost = self.chipCount * self.chipCost

    def __str__(self):
        str = "{0}: {1:03d}, {2}, ${3:06.2f}".format(self.chipName,self.simulationNumber,self.simulationDate,self.simulationCost)
        return(str)

class Employee:
    def __init__(self,employeeName,employeeID):
        self.employeeName = employeeName
        self.employeeID = employeeID
        self.simulationsDict = {}

    def addSimulation(self,sim):
        if self.simulationsDict.get(sim.simulationNumber) != None:
            self.simulationsDict[sim.simulationNumber] = sim
        else:
            self.simulationsDict[sim.simulationNumber] = sim

    def getSimulation(self,simNo):
        return self.simulationsDict.get(simNo)

    def __str__(self):
        str = "{0}, {1}: {2:02d} Simulations".format(self.employeeID,self.employeeName,len(self.simulationsDict.keys()))
        return str

    def getWorkload(self):
        string=""
        #string += str(self) +"\n"
        for key,value in self.simulationsDict.items():
            string += str(self.simulationsDict.get(key)) + "\n"
        list = string.splitlines()
        list=sorted(list)
        string=""
        string+= str(self) +"\n"
        string += "\n".join(list)
        return(string)

    def addWorkload(self,fileName):
        with open(fileName,"r") as f:
            all_lines = f.readlines() ## first line of no use
            for line in all_lines[2:]:
                list = line.split()
                sim = Simulation(int(list[0]),list[1],list[2],int(list[3]),float(list[4][1:]))
                self.simulationsDict[sim.simulationNumber] = sim

class Facility:
    def __init__(self,facilityName):
        self.facilityName = facilityName
        self.employeesDict = {}

    def addEmployee(self,employee):
        if self.employeesDict.get(employee.employeeName) != None:
            self.employeesDict[employee.employeeName] = employee
        else:
            self.employeesDict[employee.employeeName] = employee

    def getEmployees(self,*args):
        list=[]
        for name in args:
            list.append(self.employeesDict.get(name))
        return list

    def __str__(self):
        list=[]
        string=""
        first_line = "{0}: {1:02d} Employees".format(self.facilityName,len(self.employeesDict.keys()))
        for key,value in self.employeesDict.items():
            nsim = len(value.simulationsDict.keys())
            str_nsim = '{0:02d}'.format(nsim)
            string += value.employeeID + ", " + value.employeeName + ": " + str_nsim + " Simulations"
            list.append(string)
            string=""
        list = sorted(list)
        final_string = ""
        final_string += first_line + "\n"
        final_string += "\n".join(list)
        return final_string

    def getSimulation(self,simNo):
        for key1,value1 in self.employeesDict.items():
            for key2,value2 in value1.simulationsDict.items():
                if value2.simulationNumber == simNo:
                    return value2
        return None