# main.py
from shapes import Rectangle, Circle, Triangle
from area_calculator import AreaCalculator

def main():
    """Основная функция для демонстрации работы системы."""
    # Создаём разные фигуры
    rect = Rectangle(5.0, 10.0)
    circle = Circle(3.0)
    triangle = Triangle(8.0, 4.0)

    # Выводим площадь каждой фигуры
    print(f"Площадь прямоугольника: {rect.area():.2f}")
    print(f"Площадь круга: {circle.area():.2f}")
    print(f"Площадь треугольника: {triangle.area():.2f}")

    # Считаем общую площадь всех фигур
    shapes = [rect, circle, triangle]
    total = AreaCalculator.total_area(shapes)
    print(f"\nОбщая площадь всех фигур: {total:.2f}")

if __name__ == '__main__':
    main()  # Запускаем основную функцию, если файл запущен напрямую
