import unittest
import lsystem

class TestLSystem(unittest.TestCase):

    def test_simple_grammar_iteration(self):
        ls = lsystem.LSystem("F", {"F": "FF"})
        
        self.assertEqual(ls.current_grammar, "F")
        ls._IterateGrammar()
        self.assertEqual(ls.current_grammar, "FF")
        ls._IterateGrammar()
        self.assertEqual(ls.current_grammar, "FFFF")

        # Case with variable with no rule
        ls = lsystem.LSystem("F", {"F": "FX"})
        self.assertEqual(ls.current_grammar, "F")
        ls._IterateGrammar()
        self.assertEqual(ls.current_grammar, "FX")
        ls._IterateGrammar()
        self.assertEqual(ls.current_grammar, "FXX")

    def test_generate_points(self):
        ls = lsystem.LSystem("F", {"F": "FF"})
        ls._IterateGrammar()

        points = [x for x in ls.GeneratePoints(30, 10)]
        expected_points = [[0, 0, 0], [10,  0,  0], [20,  0,  0]]
        self.assertEqual(points, expected_points)
        
    def test_generate_points_rotation(self):
        ls = lsystem.LSystem("F>F>F>F", {})

        points = [x for x in ls.GeneratePoints(90, 10)]
        expected_points = [[0, 0, 0], [10,  0,  0], [10,  10,  0], [0, 10, 0], [0, 0, 0]]
        self.assertEqual(points, expected_points)

        ls = lsystem.LSystem(">F<<F+F--F^F&&F", {})

        points = [x for x in ls.GeneratePoints(90, 10)]
        expected_points = [[0, 0, 0],
                           [0,  10,  0],
                           [0,  0,  0],
                           [10,  0,  0],
                           [0,  0,  0],
                           [0,  0,  10],
                           [0,  0,  0]]
        self.assertEqual(points, expected_points)


if __name__ == '__main__':
    unittest.main()
