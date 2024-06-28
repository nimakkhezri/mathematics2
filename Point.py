class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.multi = []

    def show(self) -> str:
        return f"({self.x} , {self.y} , {self.z})"

    def show_multi(self) -> str:
        point = self.multi

    def set_multi(self, parameters: list):
        for parameter in parameters:
            self.multi.append(parameter)