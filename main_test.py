# Import pytest and the functions to be tested
import pytest
from main import area_base_height, area_three_sides, area_points

# Test for area_base_height
def test_area_base_height():
    assert area_base_height(10, 5) == 25
    assert area_base_height(7, 3) == pytest.approx(10.5)

# Test for area_three_sides
def test_area_three_sides():
    assert area_three_sides(3, 4, 5) == 6  # Perfect triangle
    assert area_three_sides(10, 10, 10) == pytest.approx(43.301, 0.001)  # Equilateral triangle

# Test for area_points
def test_area_points():
    assert area_points(0, 0, 4, 0, 4, 3) == 6  # Right-angled triangle
    assert area_points(0, 0, 0, 3, 4, 3) == 6  # Same right-angled triangle, different order

# Test function circumference
def test_circumference():
    from main import circumference
    assert circumference(3, 4, 5) == 6  # Half of the perimeter of a perfect triangle
    assert circumference(10, 10, 10) == 15  # Half of the perimeter of an equilateral triangle