class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        squared_sum = self.x ** 2 + self.y ** 2 + self.z ** 2
        return squared_sum

# Example usage
point = Point(1, 3, 5)
result = point.sqSum()
print("Sum of squared values:", result)