import unittest

import code

class TestMethods(unittest.TestCase):
    def test_mag(self):
        self.assertEqual(code.magnitude(100.,0.),5.)

    def test_flux(self):
        self.assertEqual(code.flux(5.),100.)

if __name__=="__main__":
    unittest.main()
