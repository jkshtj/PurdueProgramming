import unittest
from points import *


class PointNDTestSuite(unittest.TestCase):

    def test_tupleExists(self):

        p = PointND(1.2, 3.4, 5.6, 7.8)

        expectedValue = 1.2, 3.4, 5.6, 7.8
        actualValue = p.t

        self.assertEqual(expectedValue, actualValue)

    def test_cardinalityExists(self):

        p = PointND(9.10, 1.2, 3.4, 5.6, 7.8)

        expectedValue = 5
        actualValue = p.n

        self.assertEqual(expectedValue, actualValue)

    def test_initializer(self):

        with self.subTest(key="correct input"):

            p = PointND(-3.0, 1.2, 3.1415, 2.7)
            self.assertIsNotNone(p)

        with self.subTest(key="integer input"):

            self.assertRaises(ValueError, PointND, 9, 3.1415, 2.7)

        with self.subTest(key="list input"):

            self.assertRaises(ValueError, PointND, [9, 3.1415, 2.7])

        with self.subTest(key="string input"):

            self.assertRaises(ValueError, PointND, 'pi', 9, 3.1415, 2.7)

    def test_printPoint(self):

        p = PointND(6.9584, -2.7017, 3.1415, 0.0040)

        expectedValue = "(6.96, -2.70, 3.14, 0.00)"
        actualValue = str(p)

        self.assertEqual(expectedValue, actualValue)

    def test_hashExists(self):

        p = PointND(1.0, 2.0, 3.0, 4.0, 5.0)

        expectedValue = hash((1.0, 2.0, 3.0, 4.0, 5.0))
        actualValue = hash(p)

        self.assertEqual(expectedValue, actualValue)

    def test_distanceFrom(self):

        p = PointND(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)

        with self.subTest(key="normalOperation"):

            q = PointND(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

            expectedValue = 3.0
            actualValue = p.distanceFrom(q)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="wrongCardinality"):

            q = PointND(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

            self.assertRaises(ValueError, p.distanceFrom, q)

    def test_nearestPoint(self):

        p = PointND(0.0, 0.0)

        with self.subTest(key="pointList"):

            pointList = [PointND(1.5, 2.7), PointND(1.0, 1.0), PointND(-2.0, 3.0)]
            q = p.nearestPoint(pointList)

            expectedValue = 1.0, 1.0
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="emptyList"):

            self.assertRaises(ValueError, p.nearestPoint, [])

    def test_clone(self):

        p = PointND(3.14, 0.0, 2.71, -1.0, 10.10)
        q = p.clone()

        with self.subTest(key="normalOperation"):

            expectedValue = 3.14, 0.0, 2.71, -1.0, 10.10
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            self.assertIsNot(p, q)

    def test_pointAddition(self):

        p1 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
        p2 = PointND(0.5, 0.4, 0.3, 0.2, 0.1)
        p3 = PointND(0.5, 0.4, 0.1)

        q = p1 + p2

        with self.subTest(key="normalOperation"):

            expectedValue = 1.5, 2.5, 3.5, 3.6, 4.6
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            self.assertTrue(q is not p1 and q is not p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x + y, p1, p3)

    def test_floatAddition(self):

        p1 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)

        with self.subTest(key="normalOperation1"):

            q = p1 + 10.0
            expectedValue = 11.0, 12.1, 13.2, 13.4, 14.5
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="normalOperation2"):

            q = 10.0 + p1
            expectedValue = 11.0, 12.1, 13.2, 13.4, 14.5
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            q = p1 + 10.0
            self.assertTrue(q is not p1)

    def test_pointSubtraction(self):

        p1 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
        p2 = PointND(0.5, 0.6, 0.7, 0.9, 0.5)
        p3 = PointND(0.5, 0.4, 0.1)

        q = p1 - p2

        with self.subTest(key="normalOperation"):

            expectedValue = 0.5, 1.5, 2.5, 2.5, 4.0
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            self.assertTrue(q is not p1 and q is not p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x - y, p1, p3)

    def test_floatSubtraction(self):

        p1 = PointND(11.0, 12.1, 13.2, 13.4, 14.5)
        q = p1 - 10.0

        with self.subTest(key="normalOperation"):

            expectedValue = 1.0, 2.1, 3.2, 3.4, 4.5
            actualValue = tuple(round(i, 5) for i in q.t)

            self.assertAlmostEqual(expectedValue, actualValue, 5)

        with self.subTest(key="Identity"):

            self.assertTrue(q is not p1)

    def test_multiplication(self):

        p1 = PointND(11.0, 12.1, 13.2, 13.4, 14.5)

        with self.subTest(key="normalOperation1"):

            q = p1 * 10.0
            expectedValue = 110.0, 121.0, 132.0, 134.0, 145.0
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="normalOperation2"):

            q = 10.0 * p1
            expectedValue = 110.0, 121.0, 132.0, 134.0, 145.0
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            q = p1 * 10.0
            self.assertTrue(q is not p1)

    def test_division(self):

        p1 = PointND(110.0, 121.0, 132.0, 134.0, 145.0)

        with self.subTest(key="normalOperation"):

            q = p1 / 10.0
            expectedValue = 11.0, 12.1, 13.2, 13.4, 14.5
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            q = p1 / 10.0
            self.assertTrue(q is not p1)

    def test_negation(self):

        p1 = PointND(1.2, -6.9, 5.7, -8.8)
        q = -p1

        with self.subTest(key="normalOperation"):

            expectedValue = -1.2, 6.9, -5.7, 8.8
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            self.assertTrue(q is not p1)

    def test_indexing(self):

        p1 = PointND(1.2, -6.9, 5.7, -8.8)

        expectedValue = -8.8
        actualValue = p1[3]

        self.assertEqual(expectedValue, actualValue)

    def test_equality(self):

        p1 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
        p2 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
        p3 = PointND(1.0, 2.1, 3.2)

        with self.subTest(key="normalOperation"):

            self.assertTrue(p1 == p2)

        with self.subTest(key="Identity"):

            self.assertTrue(p1 is not p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x == y, p1, p3)

    def test_inequality(self):

        p1 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
        p2 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
        p3 = PointND(1.0, 2.1, 3.2)

        with self.subTest(key="normalOperation"):

            self.assertFalse(p1 != p2)

        with self.subTest(key="Identity"):

            self.assertTrue(p1 is not p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x != y, p1, p3)

    def test_greaterThan(self):

        p1 = PointND(1.0, 2.1, 9.2)
        p2 = PointND(1.0, 2.1, 3.2)
        p3 = PointND(1.0, 2.1, 3.2, 5.5)

        with self.subTest(key="normalOperation"):

            self.assertTrue(p1 > p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x > y, p1, p3)

    def test_greaterThanOrEqual(self):

        p1 = PointND(1.0, 2.1, 3.2)
        p2 = PointND(1.0, 2.1, 3.2)
        p3 = PointND(1.0, 2.1, 3.2, 5.5)

        with self.subTest(key="normalOperation"):

            self.assertTrue(p1 >= p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x > y, p1, p3)

    def test_lessThan(self):

        p1 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
        p2 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
        p3 = PointND(1.0, 2.1, 3.2, 5.5)

        with self.subTest(key="normalOperation"):

            self.assertFalse(p1 < p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x < y, p1, p3)

    def test_lessThanOrEqual(self):

        p1 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
        p2 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
        p3 = PointND(1.0, 2.1, 3.2, 5.5)

        with self.subTest(key="normalOperation"):

            self.assertTrue(p1 <= p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x <= y, p1, p3)


class Point3DTestSuite(unittest.TestCase):

    def test_coordinatesExists(self):

        p = Point3D(1.2, 3.4, 5.6)

        expectedValue = 1.2, 3.4, 5.6
        actualValue = p.x, p.y, p.z

        self.assertEqual(expectedValue, actualValue)

    def test_tupleExists(self):

        p = Point3D(1.2, 3.4, 5.6)

        expectedValue = 1.2, 3.4, 5.6
        actualValue = p.t

        self.assertEqual(expectedValue, actualValue)

    def test_cardinalityExists(self):

        p = Point3D(9.10, 1.2, 3.4)

        expectedValue = 3
        actualValue = p.n

        self.assertEqual(expectedValue, actualValue)

    def test_initializer(self):

        with self.subTest(key="correct input"):

            p = Point3D(-3.0, 2.7, 3.1415)
            self.assertIsNotNone(p)

        with self.subTest(key="integer input"):

            self.assertRaises(ValueError, Point3D, 9, 3.1415, 2.7)

        with self.subTest(key="list input"):

            self.assertRaises(ValueError, Point3D, [9, 3.1415, 2.7])

        with self.subTest(key="string input"):

            self.assertRaises(ValueError, Point3D, 'pi', 9, 3.1415)

    def test_printPoint(self):

        p = Point3D(6.9584, 2.7017, 3.1415)

        expectedValue = "(6.96, 2.70, 3.14)"
        actualValue = str(p)

        self.assertEqual(expectedValue, actualValue)

    def test_hashExists(self):

        p = Point3D(3.0, 4.0, 5.0)

        expectedValue = hash((3.0, 4.0, 5.0))
        actualValue = hash(p)

        self.assertEqual(expectedValue, actualValue)

    def test_distanceFrom(self):

        p = Point3D(4.0, 0.0, 3.0)

        with self.subTest(key="normalOperation"):

            q = Point3D(0.0, 0.0, 0.0)

            expectedValue = 5.0
            actualValue = p.distanceFrom(q)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="wrongCardinality"):

            q = PointND(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

            self.assertRaises(ValueError, p.distanceFrom, q)

    def test_nearestPoint(self):

        p = Point3D(0.0, 0.0, 0.0)

        with self.subTest(key="pointList"):

            pointList = [Point3D(1.5, 2.7, 0.0), Point3D(1.0, 1.0, 0.0), Point3D(-2.0, 3.0, 0.0)]
            q = p.nearestPoint(pointList)

            expectedValue = 1.0, 1.0, 0.0
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="emptyList"):

            self.assertRaises(ValueError, p.nearestPoint, [])

    def test_clone(self):

        p = Point3D(3.14, 2.71, -1.0)
        q = p.clone()

        with self.subTest(key="normalOperation"):

            expectedValue = 3.14, 2.71, -1.0
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            self.assertIsNot(p, q)

    def test_pointAddition(self):

        p1 = Point3D(1.0, 2.1, 3.2)
        p2 = Point3D(0.5, 0.4, 0.3)
        p3 = PointND(0.5, 0.4, 0.1, 0.0)

        q = p1 + p2

        with self.subTest(key="normalOperation"):

            expectedValue = 1.5, 2.5, 3.5
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            self.assertTrue(q is not p1 and q is not p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x + y, p1, p3)

    def test_floatAddition(self):

        p1 = Point3D(1.0, 2.1, 3.2)

        with self.subTest(key="normalOperation1"):

            q = p1 + 10.0
            expectedValue = 11.0, 12.1, 13.2
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="normalOperation2"):

            q = 10.0 + p1
            expectedValue = 11.0, 12.1, 13.2
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            q = p1 + 10.0
            self.assertTrue(q is not p1)

    def test_pointSubtraction(self):

        p1 = Point3D(1.0, 2.1, 3.2)
        p2 = Point3D(0.5, 0.6, 0.7)
        p3 = PointND(0.5, 0.4, 0.1, 0.0)

        q = p1 - p2

        with self.subTest(key="normalOperation"):

            expectedValue = 0.5, 1.5, 2.5
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            self.assertTrue(q is not p1 and q is not p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x - y, p1, p3)

    def test_floatSubtraction(self):

        p1 = Point3D(11.0, 12.1, 13.2)
        q = p1 - 10.0

        with self.subTest(key="normalOperation"):

            expectedValue = 1.0, 2.1, 3.2
            actualValue = tuple(round(i, 5) for i in q.t)

            self.assertAlmostEqual(expectedValue, actualValue, 5)

        with self.subTest(key="Identity"):

            self.assertTrue(q is not p1)

    def test_multiplication(self):

        p1 = Point3D(13.2, 13.4, 14.5)

        with self.subTest(key="normalOperation1"):

            q = p1 * 10.0
            expectedValue = 132.0, 134.0, 145.0
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="normalOperation2"):

            q = 10.0 * p1
            expectedValue = 132.0, 134.0, 145.0
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            q = p1 * 10.0
            self.assertTrue(q is not p1)

    def test_division(self):

        p1 = Point3D(132.0, 134.0, 145.0)

        with self.subTest(key="normalOperation"):

            q = p1 / 10.0
            expectedValue = 13.2, 13.4, 14.5
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            q = p1 / 10.0
            self.assertTrue(q is not p1)

    def test_negation(self):

        p1 = Point3D(1.2, -6.9, -5.7)
        q = -p1

        with self.subTest(key="normalOperation"):

            expectedValue = -1.2, 6.9, 5.7
            actualValue = q.t

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            self.assertTrue(q is not p1)

    def test_indexing(self):

        p1 = Point3D(-1.2, -6.9, 5.7)

        expectedValue = -1.2
        actualValue = p1[0]

        self.assertEqual(expectedValue, actualValue)

    def test_equality(self):

        p1 = Point3D(3.2, 3.4, 4.5)
        p2 = Point3D(3.2, 3.4, 4.5)
        p3 = PointND(1.0, 3.2)

        with self.subTest(key="normalOperation"):

            self.assertTrue(p1 == p2)

        with self.subTest(key="Identity"):

            self.assertTrue(p1 is not p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x == y, p1, p3)

    def test_inequality(self):

        p1 = Point3D(1.0, 3.4, 4.5)
        p2 = Point3D(1.0, 3.4, 4.5)
        p3 = PointND(1.0, 3.2)

        with self.subTest(key="normalOperation"):

            self.assertFalse(p1 != p2)

        with self.subTest(key="Identity"):

            self.assertTrue(p1 is not p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x != y, p1, p3)

    def test_greaterThan(self):

        p1 = Point3D(1.0, 2.1, 9.2)
        p2 = Point3D(1.0, 2.1, 3.2)
        p3 = PointND(1.0, 2.1, 3.2, 5.5)

        with self.subTest(key="normalOperation"):

            self.assertTrue(p1 > p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x > y, p1, p3)

    def test_greaterThanOrEqual(self):

        p1 = Point3D(1.0, 2.1, 3.2)
        p2 = Point3D(1.0, 2.1, 3.2)
        p3 = PointND(1.0, 2.1, 3.2, 5.5)

        with self.subTest(key="normalOperation"):

            self.assertTrue(p1 >= p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x > y, p1, p3)

    def test_lessThan(self):

        p1 = Point3D(1.0, 3.4, 4.5)
        p2 = Point3D(1.0, 3.4, 4.5)
        p3 = PointND(1.0, 2.1, 3.2, 5.5)

        with self.subTest(key="normalOperation"):

            self.assertFalse(p1 < p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x < y, p1, p3)

    def test_lessThanOrEqual(self):

        p1 = Point3D(1.0, 3.4, 4.5)
        p2 = Point3D(1.0, 3.4, 4.5)
        p3 = PointND(1.0, 2.1, 3.2, 5.5)

        with self.subTest(key="normalOperation"):

            self.assertTrue(p1 <= p2)

        with self.subTest(key="wrongCardinality"):

            self.assertRaises(ValueError, lambda x, y: x <= y, p1, p3)


class PointSetTestSuite(unittest.TestCase):

    def test_setExists(self):

        p = PointND(1.2, 5.6, 7.8)
        q = PointND(0.9, -45.3, 12.11)
        w = PointND(0.0, 0.0, 0.0)

        pointList = [p, q, w, p, q]
        ps = PointSet(pointList=pointList)
        s = {p, q, w}

        expectedValue = s
        actualValue = ps.points

        self.assertEqual(expectedValue, actualValue)

    def test_cardinalityExists(self):

        p = PointND(1.2, 5.6, 7.8)
        pointList = [p, p]
        ps = PointSet(pointList=pointList)

        expectedValue = 3
        actualValue = ps.n

        self.assertEqual(expectedValue, actualValue)

    def test_initializer(self):

        with self.subTest(key="correct input"):

            p = PointND(1.2, 5.6, 7.8)
            q = PointND(0.9, -45.3, 12.11)
            w = PointND(0.0, 0.0, 0.0)

            pointList = [p, q, w, p, q]
            ps = PointSet(pointList=pointList)

            self.assertIsNotNone(ps)

        with self.subTest(key="wrongCardinality"):

            p = PointND(1.2, 5.6, 7.8)
            q = PointND(0.9, -45.3, 12.11)
            w = PointND(0.0, 0.0, 0.0, 0.0)

            pointList = [p, q, w, p, q]

            self.assertRaises(ValueError, PointSet, pointList=pointList)

        with self.subTest(key="emptyList"):

            self.assertRaises(ValueError, PointSet, pointList=[])

        with self.subTest(key="wrongKey"):

            self.assertRaises(KeyError, PointSet, wrongKey=[])

    def test_addPoint(self):

        p = PointND(9.0, 10.1, 3.21, 6.54, -8.1, 9.4)
        q = PointND(6.54, -8.1, 9.4, 9.0, 10.1, 3.21)
        pointList = [p, q]
        ps = PointSet(pointList=pointList)

        with self.subTest(key="normalOperation"):

            w = PointND(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
            ps.addPoint(w)

            self.assertTrue(w in ps.points)

        with self.subTest(key="wrongCardinality"):

            e = PointND(1.0, 2.0, 3.0, 4.0, 5.0)
            self.assertRaises(ValueError, ps.addPoint, e)

    def test_count(self):

        p = PointND(9.0, 10.1, 3.21, 6.54, -8.1, 9.4)
        q = PointND(6.54, -8.1, 9.4, 9.0, 10.1, 3.21)
        w = PointND(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        e = PointND(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)

        pointList = [p, q, w, e, p, q, w, e]
        ps = PointSet(pointList=pointList)

        expectedValue = 4
        actualValue = ps.count()

        self.assertEqual(expectedValue, actualValue)

    def test_computeBoundingHyperCube(self):

        p01 = PointND(5.3767, -13.4989, 6.7150, 8.8840, -1.0224)
        p02 = PointND(18.3389, 30.3492, -12.0749, -11.4707, -2.4145)
        p03 = PointND(-22.5885, 7.2540, 7.1724, -10.6887, 3.1921)
        p04 = PointND(8.6217, -0.6305, 16.3024, -8.0950, 3.1286)
        p05 = PointND(3.1877, 7.1474, 4.8889, -29.4428, -8.6488)
        p06 = PointND(-13.0769, -2.0497, 10.3469, 14.3838, -0.3005)
        p07 = PointND(-4.3359, -1.2414, 7.2689, 3.2519, -1.6488)
        p08 = PointND(3.4262, 14.8970, -3.0344, -7.5493, 6.2771)
        p09 = PointND(35.7840, 14.0903, 2.9387, 13.7030, 10.9327)
        p10 = PointND(27.6944, 14.1719, -7.8728, -17.1152, 11.0927)
        pointList = [p01, p02, p03, p04, p05, p06, p07, p08, p09, p10]
        ps = PointSet(pointList=pointList)

        minPoint = PointND(-22.5885, -13.4989, -12.0749, -29.4428, -8.6488)
        maxPoint = PointND(35.7840, 30.3492, 16.3024, 14.3838, 11.0927)

        expectedValue = minPoint, maxPoint
        actualValue = ps.computeBoundingHyperCube()

        self.assertEqual(expectedValue, actualValue)

    def test_computeNearestNeighbors(self):

        p01 = PointND(9.0, 8.0, 3.0)
        p02 = PointND(5.0, 2.0, 1.0)
        p03 = PointND(1.0, 8.0, 2.0)
        p04 = PointND(1.0, 2.0, 6.0)
        p05 = PointND(2.0, 9.0, 4.0)
        pointList1 = [p01, p02, p03, p04, p05]
        ps1 = PointSet(pointList=pointList1)

        q01 = PointND(3.0, 2.0, 0.0)
        q02 = PointND(8.0, 7.0, 0.0)
        q03 = PointND(5.0, 7.0, 5.0)
        q04 = PointND(5.0, 3.0, 7.0)
        q05 = PointND(9.0, 5.0, 9.0)
        pointList2 = [q01, q02, q03, q04, q05]
        ps2 = PointSet(pointList=pointList2)

        nearestNeighbors = [(p01, q02), (p02, q01), (p03, q03), (p04, q04), (p05, q03)]
        nearestNeighbors.sort()

        expectedValue = nearestNeighbors
        actualValue = ps1.computeNearestNeighbors(ps2)

        # self.assertEqual(expectedValue, actualValue)
        self.assertSetEqual(set(expectedValue), set(actualValue))

    def test_pointAddition(self):

        p01 = PointND(-3.6235, -1.4058, -6.1554, 0.8460)
        p02 = PointND(8.7240, -0.8174, -1.0615, 0.1004)
        p03 = PointND(2.4757, 3.2953, -2.4708, -4.0010)
        p04 = PointND(4.1369, -0.8336, -4.7312, 3.3825)

        pointList1 = [p01, p02, p03, p04]
        ps1 = PointSet(pointList=pointList1)

        with self.subTest(key="normalOperation"):

            p05 = PointND(-3.1745, 2.1046, 1.5239, 1.0505)
            ps1 = ps1 + p05

            expectedValue = {p01, p02, p03, p04, p05}
            actualValue = ps1.points

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="wrongCardinality"):

            p06 = PointND(-3.1745, 2.1046, 1.5239)
            self.assertRaises(ValueError, lambda x, y: x + y, ps1, p06)

    def test_pointSubtraction(self):

        p01 = PointND(-0.8972, -2.4941, 2.8927, 3.0561)
        p02 = PointND(0.0687, -2.9376, 1.5602, -0.3997)
        p03 = PointND(-0.7860, -3.4692, -0.0601, -2.1436)
        p04 = PointND(-5.2506, -1.6007, -0.1043, 4.0542)
        p05 = PointND(-0.8570, -6.0079, -2.3945, -0.6743)

        pointList1 = [p01, p02, p03, p04, p05]
        ps1 = PointSet(pointList=pointList1)

        with self.subTest(key="normalOperation"):

            p06 = PointND(-0.8570, -6.0079, -2.3945, -0.6743)
            ps1 = ps1 - p06

            expectedValue = {p01, p02, p03, p04}
            actualValue = ps1.points

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="missingPoint"):

            p06 = PointND(8.7240, -0.8174, -1.0615, 0.1004)
            ps1 = ps1 - p06

            expectedValue = {p01, p02, p03, p04}
            actualValue = ps1.points

            self.assertEqual(expectedValue, actualValue)

    def test_membership(self):

        p01 = PointND(-3.6235, -1.4058, -6.1554, 0.8460)
        p02 = PointND(8.7240, -0.8174, -1.0615, 0.1004)
        p03 = PointND(2.4757, 3.2953, -2.4708, -4.0010)
        p04 = PointND(4.1369, -0.8336, -4.7312, 3.3825)
        p05 = PointND(-0.8570, -6.0079, -2.3945, -0.6743)

        pointList1 = [p01, p02, p03, p04]
        ps1 = PointSet(pointList=pointList1)

        self.assertFalse(p05 in ps1)


if __name__ == '__main__':
    unittest.main()
