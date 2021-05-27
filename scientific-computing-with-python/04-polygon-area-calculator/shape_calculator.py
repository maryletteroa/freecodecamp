class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shape = ""
    
    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
        self.height = height
        return self.height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = (self.width + self.height) * 2
        return self.perimeter

    def get_diagonal(self):
        width = self.width
        height = self.height
        self.diagonal = (width ** 2 + height ** 2) ** 0.5
        return self.diagonal

    def get_picture(self):
        if self.width < 50 and self.height < 50:
            height = self.height
            width = self.width
            self.shape = ""
            for h in range(height):
                for w in range(width):
                    self.shape += "*"
                self.shape += "\n"
            return self.shape
        else:
            return "Too big for picture."

    def get_amount_inside(self, object):
        inside_area = object.get_area()
        container_area = self.get_area()
        n_fit = container_area // inside_area
        return n_fit


    def __str__(self):
        width = self.width
        height = self.height
        rep = f"Rectangle(width={width}, height={height})"
        return rep


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side        

    def set_width(self, side):
        self.width = side
        return self.width

    def set_height(self, side):
        self.height = side
        return self.height

    def __str__(self):
        side = self.width
        rep = f"Square(side={side})"
        return rep