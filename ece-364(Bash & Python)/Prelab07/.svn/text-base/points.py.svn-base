import sys
import os
import math
import copy

class PointND:

    def __init__(self,*args):
        for item in args:
            if type(item) != float:
                raise ValueError("Cannot instantiate an object with non-float values.")
        self.t = args
        self.n = len(args)


    def __str__(self):
        res = [round(x,2) for x in self.t]
        res1 = [format(x, '.2f') for x in res]
        res1 = ", ".join(res1)
        res2 = "("+res1+")"
        return res2


    def __hash__(self):
        return hash(self.t)


    def distanceFrom(self,other):
        if self.n != other.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")
        distance = []
        for i in range(len(self.t)):
            distance.append(pow(self.t[i] - other.t[i],2))
        return math.sqrt(sum(distance))


    def nearestPoint(self,points):
        if len(points) == 0:
            raise ValueError("Input cannot be empty.")

        min_dist = 1000000
        closest = 0

        for p in points:
            dist = self.distanceFrom(p)
            if dist < min_dist:
                min_dist = dist
                closest = p
        return closest

    def clone(self):
        return copy.deepcopy(self)


    def __add__(self, other):
        if type(other) != float:
            if self.n != other.n:
                raise ValueError("Cannot operate on points with different cardinalities.")
            res=[]
            for i in range(len(self.t)):
                res.append(self.t[i] + other.t[i])

            point = PointND(*tuple(res)[0:])
            return point
        else:
            res=[]
            for i in range(len(self.t)):
                res.append(self.t[i] + other)
            point = PointND(*tuple(res)[0:])
            return point

    def __radd__(self,other):
         res=[]
         for i in range(len(self.t)):
             res.append(self.t[i] + other)
         point = PointND(*tuple(res)[0:])
         return point

    def __sub__(self, other):
        if type(other) != float:
            if self.n != other.n:
                raise ValueError("Cannot operate on points with different cardinalities.")
            res=[]
            for i in range(len(self.t)):
                res.append(self.t[i] - other.t[i])

            point = PointND(*tuple(res)[0:])
            return point
        else:
            res=[]
            for i in range(len(self.t)):
                res.append(self.t[i] - other)
            point = PointND(*tuple(res)[0:])
            return point

    def __mul__(self, other):
         res=[]
         for i in range(len(self.t)):
             res.append(self.t[i] * other)

         point = PointND(*tuple(res)[0:])
         return point

    def __rmul__(self, other):
         res=[]
         for i in range(len(self.t)):
             res.append(self.t[i] * other)

         point = PointND(*tuple(res)[0:])
         return point

    def __truediv__(self, other):
         res=[]
         for i in range(len(self.t)):
             res.append(self.t[i] / other)

         point = PointND(*tuple(res)[0:])
         return point

    def __neg__(self):
         res=[]
         for i in range(len(self.t)):
             res.append(self.t[i] * -1)

         point = PointND(*tuple(res)[0:])
         return point

    def __getitem__(self, item):
        return self.t[item]

    def __eq__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        for i in range(len(self.t)):
            if self.t[i] == other.t[i]:
                continue
            else:
                return False
        return True

    def __ne__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        for i in range(len(self.t)):
            if self.t[i] != other.t[i]:
                continue
            else:
                return False
        return True

    def __gt__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        list = [0.0]*self.n
        origin = PointND(*tuple(list)[0:])
        if self.distanceFrom(origin) <=  other.distanceFrom(origin):
            return False
        return True

    def __ge__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        list = [0.0]*self.n
        origin = PointND(*tuple(list)[0:])
        if self.distanceFrom(origin) <  other.distanceFrom(origin):
            return False
        return True

    def __lt__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        list = [0.0]*self.n
        origin = PointND(*tuple(list)[0:])
        if self.distanceFrom(origin) >=  other.distanceFrom(origin):
            return False
        return True

    def __le__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        list = [0.0]*self.n
        origin = PointND(*tuple(list)[0:])
        if self.distanceFrom(origin) >  other.distanceFrom(origin):
            return False
        return True


class Point3D(PointND):

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.t = (self.x,self.y,self.z)
        self.n = len(self.t)
        for item in self.t:
            if type(item) != float:
                raise ValueError("Cannot instantiate an object with non-float values.")

class PointSet:

    def __init__(self):
        self.points = set()
        self.n = 0


    def __init__(self, **kwargs):
        if kwargs.get('pointList') == []:
            raise ValueError("'pointList' input parameter cannot be empty.")
        elif kwargs.get('pointList') == None:
            raise KeyError("'pointList' input parameter not found.")
        else:
            self.points = set()
            self.n = kwargs.get('pointList')[0].n
            for pt in kwargs.get('pointList'):
                if pt.n == self.n:
                    self.points.add(pt)
                else:
                    raise ValueError("Expecting a point with cardinality {0}.".format(self.n))

    def addPoint(self,p):
        if p.n != self.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        self.points.add(p)

    def count(self):
        return len(set(self.points))


    def computeBoundingHyperCube(self):
        pts = set(self.points)
        min_val = 1000
        min_pt = 0
        max_val = 0
        max_pt = 0
        min_arr=[]
        max_arr=[]

        for i in range(self.n):
            for pt in self.points:
                if pt.t[i] < min_val:
                    min_val = pt.t[i]
                if pt.t[i] > max_val:
                    max_val = pt.t[i]
            min_arr.append(min_val)
            max_arr.append(max_val)
            min_val = 1000
            max_val = 0
        min_res = PointND(*tuple(min_arr)[0:])
        max_res = PointND(*tuple(max_arr)[0:])

        return (min_res,max_res)

    def computeNearestNeighbors(self,otherPointSet):
        result = []
        element = []
        min_dist = 1000
        clo_pt = 0
        dist = 0

        for pt1 in self.points:
            element.append(pt1)
            for pt2 in otherPointSet.points:
                dist = pt1.distanceFrom(pt2)
                if dist < min_dist:
                    min_dist = dist
                    clo_pt = pt2
            element.append(clo_pt)
            result.append(tuple(element))
            element=[]
            min_dist = 1000

        return result

    def __add__(self, other):
        if other.n != self.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        (self.points).add(other)
        return self

    def __sub__(self, other):
        for pt in self.points:
            if pt == other:
                self.points.remove(pt)
                return self
        return self

    def __contains__(self, item):
        if item in self.points:
            return True
        return False