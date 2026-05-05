import unittest
from math import isclose, sqrt
from shadow.polyedr import Polyedr


class TestGoodEdges(unittest.TestCase):

    # Куб со стороной 1 и центром в начале координат.
    # Коэффициент гомотетии 200.0, все вершины далеко за пределами полосы.
    # Ожидаемая сумма = 0.0.
    def test_cube(self):
        poly = Polyedr("data/cube.geom")
        self.assertTrue(isclose(poly.good_edges_sum(), 0.0))

    # Специальный полиэдр: три треугольные грани.
    # Первая грань — все три ребра хорошие:
    #   (0,0,0)-(2,0,0) длина 2.0,
    #   (2,0,0)-(1,1,0) длина √2,
    #   (1,1,0)-(0,0,0) длина √2.
    # Вторая и третья грани не дают хороших рёбер.
    # Сумма = 2.0 + 2√2.
    def test_mixed(self):
        poly = Polyedr("data/test_good.geom")
        expected = 2.0 + 2.0 * sqrt(2.0)
        self.assertTrue(isclose(poly.good_edges_sum(), expected))

    # Все точки имеют x = 42 и 43 — далеко за пределами полосы.
    # Ожидаемая сумма = 0.0.
    def test_none_good(self):
        poly = Polyedr("data/test_bad.geom")
        self.assertTrue(isclose(poly.good_edges_sum(), 0.0))
