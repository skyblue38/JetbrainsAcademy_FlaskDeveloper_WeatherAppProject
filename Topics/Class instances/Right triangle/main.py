class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = float(0.5 * self.a * self.b)


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

if input_a * input_a + input_b * input_b == input_c * input_c:
    triangle = RightTriangle(input_c, input_a, input_b)
    print("%.1f" % triangle.area)
else:
    print("Not right")
