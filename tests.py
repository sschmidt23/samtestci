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

if __name__ == "__main__":
    unittest.main()
