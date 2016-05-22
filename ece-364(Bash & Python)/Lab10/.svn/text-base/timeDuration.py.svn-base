import os
import sys
import re

class TimeSpan:

    def __init__(self,weeks,days,hours):
        if type(weeks) != int:
            raise TypeError("This class only accepts integers")
        if type(days) != int:
            raise TypeError("This class only accepts integers")
        if type(hours) != int:
            raise TypeError("This class only accepts integers")

        if weeks < 0:
            raise ValueError("Values cannot be negative")
        if days < 0:
            raise ValueError("Values cannot be negative")
        if hours < 0:
            raise ValueError("Values cannot be negative")

        if(hours >= 24):
            days = days + hours//24
            hours = hours % 24

        if(days >= 7):
            weeks = weeks + days//7
            days = days % 7

        self.weeks = weeks
        self.days = days
        self.hours = hours

    def __str__(self):
        res= ""
        res += "{0:02d}".format(self.weeks) + "W " +str(self.days) + "D " + "{0:02d}".format(self.hours) + "H"
        #print(res)
        return res

    def getTotalHours(self):
        total = self.weeks * (7*24) + (self.days*24) + self.hours
        return int(total)

    def __add__(self, other):
        if type(other) != TimeSpan:
            raise TypeError("Timespan instance expected")
        self.weeks = self.weeks + other.weeks
        self.days = self.days + other.days
        self.hours = self.hours + other.hours

    def __mul__(self, other):
        if type(other) != int:
            raise TypeError("Int expected")
        if other <= 0:
            raise  ValueError("int cannot be 0")
        self.weeks = self.weeks * other
        self.days = self.days * other
        self.hours = self.hours * other

    def __rmul__(self, other):
        if type(other) != int:
            raise TypeError("Int expected")
        if other <= 0:
            raise  ValueError("int cannot be 0")
        self.weeks = self.weeks * other
        self.days = self.days * other
        self.hours = self.hours * other