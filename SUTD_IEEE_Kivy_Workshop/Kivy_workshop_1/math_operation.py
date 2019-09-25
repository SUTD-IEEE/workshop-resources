class math_operation:

    def __init__(self,input_x,input_y):
        self.x = input_x
        self.y = input_y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplicaiton(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y

    def output(self):
        return '''
        Addition: {0}
        Subtraction: {1}
        Multiplication: {2}
        Division: {3}
        '''.format(self.addition(),self.subtraction(),
                   self.multiplicaiton(),self.division())
