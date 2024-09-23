class ImageArea:
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height

    def __eq__(self,other):
        if self.get_area() == other.get_area():
            return True
        else:
            return False
    def __ne__(self, other):
        if self.get_area() != other.get_area():
            return True
        else:
            return False
    def __lt__(self, other): 
        if self.get_area() < other.get_area():
             return True
        else:
            return False
    def __gt__ (self, other):
        if self.get_area() > other.get_area():
              return True
        else:
            return False
    def __le__(self, other): 
        if self.get_area() <= other.get_area():
            return True
        else:
            return False
    def __ge__ (self, other):
        if self.get_area() >= other.get_area():
            return True
        else:
            return False

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)
False
False
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)
