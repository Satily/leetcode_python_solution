class Complex(object):
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.image * other.image,
            self.real * other.image + self.image * other.real
        )

    def __str__(self):
        return '%d+%di' % (self.real, self.image)

    @staticmethod
    def parse(s):
        real, image = s.split('+')
        image = image[:-1]
        return Complex(int(real), int(image))


class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(Complex.parse(a) * Complex.parse(b))


if __name__ == "__main__":
    print(Solution().complexNumberMultiply("1+1i", "1+1i"))
    print(Solution().complexNumberMultiply("1+-1i", "1+-1i"))
