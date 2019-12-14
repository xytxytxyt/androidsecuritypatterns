import unittest
import naiveGeometry as ng


class naiveGeometryTest(unittest.TestCase):
    def testGetSlope(self):
        self.assertEqual(ng.getSlope((1, 1), (2, 2)), 1)
        self.assertEqual(ng.getSlope((2, 2), (1, 1)), 1)

        self.assertEqual(ng.getSlope((1, 1), (2, 1)), 0)
        self.assertEqual(ng.getSlope((2, 1), (1, 1)), 0)

        self.assertEqual(ng.getSlope((2, 1), (1, 2)), -1)
        self.assertEqual(ng.getSlope((1, 2), (2, 1)), -1)

        self.assertEqual(ng.getSlope((2, 1), (2, 2)), float('inf'))
        self.assertEqual(ng.getSlope((2, 2), (2, 1)), float('inf'))

    def testPointIsBetweenOnLine(self):
        self.assertTrue(ng.pointIsBetweenOnLine((2, 3), (3, 3), (1, 3)))
        self.assertTrue(ng.pointIsBetweenOnLine((2, 3), (1, 3), (3, 3)))

        self.assertTrue(ng.pointIsBetweenOnLine((1, 2), (1, 1), (1, 3)))
        self.assertTrue(ng.pointIsBetweenOnLine((1, 2), (1, 3), (1, 1)))

        self.assertTrue(ng.pointIsBetweenOnLine((2, 2), (1, 1), (3, 3)))
        self.assertTrue(ng.pointIsBetweenOnLine((2, 2), (3, 3), (1, 1)))

        self.assertFalse(ng.pointIsBetweenOnLine((1, 1), (2, 2), (3, 3)))
        self.assertFalse(ng.pointIsBetweenOnLine((1, 1), (3, 3), (2, 2)))

        self.assertFalse(ng.pointIsBetweenOnLine((1, 1), (1, 2), (1, 3)))
        self.assertFalse(ng.pointIsBetweenOnLine((1, 1), (1, 3), (1, 2)))

        self.assertFalse(ng.pointIsBetweenOnLine((1, 3), (2, 3), (3, 3)))
        self.assertFalse(ng.pointIsBetweenOnLine((1, 3), (3, 3), (2, 3)))

        self.assertFalse(ng.pointIsBetweenOnLine((1, 3), (3, 2), (3, 3)))
        self.assertFalse(ng.pointIsBetweenOnLine((1, 3), (3, 3), (3, 2)))


if __name__ == '__main__':
    unittest.main()
