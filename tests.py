import unittest
import code

class TestMethods(unittest.TestCase):
    """quick unit tests
    Paramters
    ---------
    None
    """
    
    def test_mag(self):
        """test magnitude
        Parameters
        ----------
        None
        """
        self.assertAlmostEqual(code.magnitude(100., 0.), -5.)

    def test_flux(self):
        """test flux function
        Parameters
        ----------
        None
        """
        self.assertAlmostEqual(code.flux(-5.), 100.)

    def test_fibonacci(self):
        """test the fibonacci function for 9, should yield
           should yield 34
        Parameters:
        -----------
        None
        """
        self.assertEqual(code.fibonacci(9),34)

    def test_fibonacci_zero(self):
        """test the zero case of fibonacci 
           should return 0
        Parameters:
        -----------
        None
        """
        self.assertEqual(code.fibonacci(0),0)

if __name__ == "__main__":
    unittest.main()
