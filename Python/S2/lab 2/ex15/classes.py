class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height
    
    def __str__(self):
        return f"{self.length} x {self.width} x {self.height}"
    
    def is_cubic(self):
        if self.length == self.width == self.height:
            return True
        else:
            return False
        
    def __eq__(self, other):
        if self.length == other.length and self.width == other.width and self.height == other.height:
            return True
        else:
            return False
        
Small_box = Box(5, 10, 4)
Big_box = Box(20, 20, 20)

print(f"Small Box: {Small_box.__str__()}")
print(f"Big Box: {Big_box.__str__()}")
print(f"Volume Small: {Small_box.volume()}\nVolume Big: {Big_box.volume()} ")
print(f"Cube Small: {Small_box.is_cubic()}\nCube Big: {Big_box.is_cubic()}")
print(f"Are the boxes the same Size? {Small_box.__eq__(Big_box)}")