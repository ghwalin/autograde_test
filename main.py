def area_base_height(s, hs):
    """
    Calculate the area of a triangle given its base and height.

    :param s: The length of the base of the triangle.
    :param hs: The height of the triangle perpendicular to the base.
    :return: The area of the triangle.
    """
    return s * hs / 2

def circumference(a, b, c):
    """
    Calculate the semi-perimeter (half the circumference) of a triangle.

    :param a: The length of the first side of the triangle.
    :param b: The length of the second side of the triangle.
    :param c: The length of the third side of the triangle.
    :return: The semi-perimeter of the triangle.
    """
    return (a + b + c) / 2

def area_three_sides(a, b, c):
    """
    Calculate the area of a triangle using Heron's formula, given the lengths of its three sides.

    :param a: The length of the first side of the triangle.
    :param b: The length of the second side of the triangle.
    :param c: The length of the third side of the triangle.
    :return: The area of the triangle.
    """
    s = circumference(a, b, c)
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def area_points(ax, ay, bx, by, cx, cy):
    """
    Calculate the area of a triangle given the coordinates of its three vertices.

    :param ax: The x-coordinate of the first vertex of the triangle.
    :param ay: The y-coordinate of the first vertex of the triangle.
    :param bx: The x-coordinate of the second vertex of the triangle.
    :param by: The y-coordinate of the second vertex of the triangle.
    :param cx: The x-coordinate of the third vertex of the triangle.
    :param cy: The y-coordinate of the third vertex of the triangle.
    :return: The area of the triangle.
    """
    a = ((bx - cx)**2 + (by - cy)**2) ** 0.5
    b = ((cx - ax)**2 + (cy - ay)**2) ** 0.5
    c = ((ax - bx)**2 + (ay - by)**2) ** 0.5
    return area_three_sides(a, b, c)

def main():
    # Beispielaufruf der Funktionen
    print(area_base_height(3, 4))
    print(area_three_sides(3, 4, 5))
    print(area_points(0, 0, 3, 0, 3, 4))

if __name__ == '__main__':
    main()