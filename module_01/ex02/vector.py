class Vector:
    def __init__(self, values):
        self.values = values
        self.shape = (len(values), len(values[0]))

    def dot(self, v):
        print("dot()")
        if self.shape != v.shape:
            raise ValueError("Error: Different shapes!")
        result = 0
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                result += self.values[i][j] * v.values[i][j]
        return (result)
    
    def T(self):
        aux = []
        for j in range(len(self.values[0])):
            new_row = []
            for i in range(len(self.values)):
                new_row.append(self.values[i][j])
            aux.append(new_row)
        return (Vector(aux))
    
    def __add__(self, v):
        print("__add__")
        if self.shape != v.shape:
            raise ValueError("Error: Different shapes!")
        aux = []
        for i in range(len(self.values)):
            new_row = []
            for j in range(len(self.values[i])):
                new_row.append(self.values[i][j] + v.values[i][j])
            aux.append(new_row)
        return (aux)
    
     def __radd__(self, v):
        print("__add__")
        if self.shape != v.shape:
            raise ValueError("Error: Different shapes!")
        aux = []
        for i in range(len(self.values)):
            new_row = []
            for j in range(len(self.values[i])):
                new_row.append(self.values[i][j] + v.values[i][j])
            aux.append(new_row)
        return (aux)
    
    def __sub__(self, v):
        print("__sub__")
        if self.shape != v.shape:
            raise ValueError("Error: Different shapes!")
        aux = []
        for i in range(len(self.values)):
            new_row = []
            for j in range(len(self.values[i])):
                new_row.append(self.values[i][j] - v.values[i][j])
            aux.append(new_row)
        return (aux)
    
    def __rsub__(self, v):
        print("__sub__")
        if self.shape != v.shape:
            raise ValueError("Error: Different shapes!")
        aux = []
        for i in range(len(self.values)):
            new_row = []
            for j in range(len(self.values[i])):
                new_row.append(self.values[i][j] - v.values[i][j])
            aux.append(new_row)
        return (aux)

    def __truediv__(self, num):
        print("__div__")
        aux = []
        try:
            for row in self.values:
                new_row = [elem / num for elem in row]
                aux.append(new_row)
            return (aux)
        except Exception as e:
            print("ZeroDivisionError:",e)
    
    def __rtruediv__(self, num):
        print("__rdiv__")
        print("NotImplementedError: Division of a scalar by a Vector is not defined here.")

    def __mul__(self, num):
        print("__mul__")
        aux = []
        for row in self.values:
            new_row = [elem * num for elem in row]
            aux.append(new_row)
        return (aux)
    
    def __rmul__(self, num):
        print("__rmul__")
        aux = []
        for row in self.values:
            new_row = [elem * num for elem in row]
            aux.append(new_row)
        return (aux)
        
    def __str__(self):
        return f"{self.values}"

    def __repr__(self):
        return f"{self.values}"