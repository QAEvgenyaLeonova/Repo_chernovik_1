# test_shapes.py
import unittest  # Импортируем модуль unittest для создания тестов
from shapes import Rectangle, Circle, Triangle  # Импортируем конкретные классы фигур
from area_calculator import AreaCalculator  # Импортируем класс для расчёта площади

class TestShapes(unittest.TestCase):
    """Класс тестов для проверки функциональности фигур и калькулятора."""

    def test_rectangle_area(self):
        """Тест расчёта площади прямоугольника."""
        rect = Rectangle(4.0, 5.0)  # Создаём прямоугольник 4×5
        self.assertAlmostEqual(rect.area(), 20.0)  # Ожидаемая площадь: 4 × 5 = 20

    def test_circle_area(self):
        """Тест расчёта площади круга."""
        circle = Circle(2.0)  # Круг с радиусом 2
        expected = 3.14159 * (2 ** 2)  # Ожидаемая площадь: π × 4 ≈ 12.56636
        self.assertAlmostEqual(circle.area(), expected, places=5)  # Сравниваем с точностью до 5 знаков


    def test_triangle_area(self):
        """Тест расчёта площади треугольника."""
        triangle = Triangle(6.0, 3.0)  # Треугольник с основанием 6 и высотой 3
        self.assertAlmostEqual(triangle.area(), 9.0)  # Ожидаемая площадь: (6 × 3) / 2 = 9

    def test_total_area_calculator(self):
        """Тест калькулятора площади для коллекции фигур."""
        shapes = [
            Rectangle(2.0, 3.0),  # Площадь: 6
            Circle(1.0),             # Площадь: ≈3.14159
            Triangle(4.0, 2.0)    # Площадь: 4
        ]
        total = AreaCalculator.total_area(shapes)  # Считаем общую площадь
        expected = 6 + 3.14159 + 4  # Ожидаемая сумма: ≈13.14159
        self.assertAlmostEqual(total, expected, places=5)  # Проверяем с точностью до 5 знаков

if __name__ == '__main__':
    unittest.main()  # Запускаем тесты, если файл запущен напрямую
