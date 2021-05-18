def bmi_function(height, weight):
    return height / weight ** 2 * 10000

class BmiConstructor(object):

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def get_bmiconstructor(self):
        return self.weight / self.height ** 2 *10000

if __name__ == '__main__':
    pass
    b = BmiConstructor(180,80)
    print(b.get_bmiconstructor())
    bmi_function()
