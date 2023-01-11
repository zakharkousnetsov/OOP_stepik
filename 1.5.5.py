# https://stepik.org/lesson/701975/step/6?unit=702076

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        for edge in [self.a, self.b, self.c]:
            if not (isinstance(edge, float) or isinstance(edge, int) ) or isinstance(edge, bool) or (edge<=0):
                return 1

        if (self.a+self.b)<self.c or (self.a+self.c)<self.b or (self.b+self.c)<self.a:
            return 2

        else:
            return 3

a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

a, b, c = map(int, input().split())

# еще коммент
# еще