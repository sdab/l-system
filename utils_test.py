import unittest
import utils

class TestUtils(unittest.TestCase):

    def test_center_points(self):
        points = [[0, 0, 0],
                  [1, 1, 1],
                  [2, 2, 2]]

        np = utils.center_points(points)
        expected_points = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
        self.assertEqual(np, expected_points)
        
        points = [[1, -1, 0],
                  [1, 1, 1],
                  [2, 2, 2]]

        np = utils.center_points(points)
        expected_points = [[0, 0, 0], [0, 2, 1], [1, 3, 2]]
        self.assertEqual(np, expected_points)
        

if __name__ == '__main__':
    unittest.main()
