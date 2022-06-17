class Resistor:
    def __init__(self, types, par, power, precision):
        self.types = types
        self.par = par
        self.power = power
        self.precision = precision

    def __str__(self):
        return f"Type: {self.types}, par: {self.par}, power: {self.power}, precision: {self.precision}"


class Node:
    def __init__(self, resistor: Resistor):
        self.left = None
        self.right = None
        self.resistor = resistor

    def insert(self, resistor: Resistor):
        if self.resistor:
            if resistor.par < self.resistor.par:
                if self.left is None:
                    self.left = Node(resistor)
                else:
                    self.left.insert(resistor)
            elif resistor.par > self.resistor.par:
                if self.right is None:
                    self.right = Node(resistor)
                else:
                    self.right.insert(resistor)
        else:
            self.resistor.par = resistor.par
        return self

    def find(self, par):
        if self.left:
            self.left.find(par)
        if self.resistor.par > par:
            print(self.resistor)
        if self.right:
            self.right.find(par)

    def delete_by_precision(self, value):
        if value < self.resistor.precision:
            if self.left is None:
                return " not found"
            self.left.delete_by_precision(value)
        elif value > self.resistor.precision:
            if self.right is None:
                return " not found"
            self.right.delete_by_precision(value)
        else:
            self.resistor = self.right
            if self.left is not None:
                self.left.delete_by_precision(value)
            if self.right is not None:
                self.right.delete_by_precision(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.resistor),
        if self.right:
            self.right.print_tree()

    def traverse_preorder(self):
        print(self.resistor, end=' ')
        if self.left:
            self.left.traverse_preorder()
        if self.right:
            self.right.traverse_preorder()

    def __str__(self):
        return "_"


def main():
    res1 = Resistor("type1", 3, 10, 99)
    res2 = Resistor("type2", 5, 30, 50)
    res3 = Resistor("type3", 1, 20, 20)
    res4 = Resistor("type4", 2, 5, 88)

    root = Node(res1)
    root.insert(res2)
    root.insert(res3)
    root.insert(res4)
    root.print_tree()
    print("\n")
    root.find(70)
    root.delete_by_precision(20)
    print("\n")
    root.print_tree()


if __name__ == '__main__':
    main()
