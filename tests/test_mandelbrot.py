import unittest
from src.models.mandelbrot_model import MandelbrotModel


class TestMandelbrotModel(unittest.TestCase):

    def test_initial_bounds(self):
        model = MandelbrotModel()
        self.assertEqual(model.xmin, -2.0)
        self.assertEqual(model.xmax, 2.0)
        self.assertEqual(model.ymin, -1.5)
        self.assertEqual(model.ymax, 1.5)

    def test_reset_zoom(self):
        model = MandelbrotModel()
        model.xmin, model.xmax = 0.0, 1.0
        model.reset_zoom()
        self.assertEqual(model.xmin, -2.0)
        self.assertEqual(model.xmax, 2.0)
