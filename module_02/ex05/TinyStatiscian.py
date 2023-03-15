from math import sqrt

class TinyStatistician:
    def mean(self, x):
        if not x:
            return None
        elem_nb = 0
        total = 0
        for i in range(len(x)):
            if isinstance(x[i], list):
                for j in range(len(x[i])):
                    total += x[i][j]
                    elem_nb += 1
            else:
                total += x[i]
                elem_nb += 1
        return total / elem_nb

    def median(self, x):
        if not x:
            return None
        vector = []
        num = 0
        for i in range(len(x)):
            if isinstance(x[i], list):
                for j in range(len(x[i])):
                    vector.append(x[i][j])
            else:
                vector = x
        vector.sort()
        if len(vector) % 2:
            num = vector[int(len(vector) / 2)] 
        else:
            num = (vector[int(len(vector) / 2)] + vector[(int(len(vector) / 2)) - 1]) / 2
        return num
    
    def quartiles(self, x):
        if not x:
            return None
        vector = []
        nums = []
        for i in range(len(x)):
            if isinstance(x[i], list):
                for j in range(len(x[i])):
                    vector.append(x[i][j])
            else:
                vector = x
        vector.sort()
        if len(vector) % 4:
            nums.append(vector[int(len(vector) / 4)])
            nums.append(vector[int(len(vector) * 3 / 4)])
        else:
            nums.append((vector[int(len(vector) / 4)] + vector[(int(len(vector) / 4)) - 1]) / 2)
            nums.append((vector[int(len(vector) * 3 / 4)] + vector[(int(len(vector) * 3 / 4)) - 1]) / 2)
        return nums

    def var(self, x):
        if not x:
            return None
        mean = self.mean(x)
        elem_nb = 0
        total = 0
        for i in range(len(x)):
            if isinstance(x[i], list):
                for j in range(len(x[i])):
                    total += (x[i][j] - mean) ** 2
                    elem_nb += 1
            else:
                total += (x[i] - mean) ** 2
                elem_nb += 1
        return total / elem_nb
    
    def std(self, x):
        if not x:
            return None
        return sqrt(self.var(x))

if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    b = [[100, 20, 3, 5], [40, 500, 6, 2], [70, 8, 900, 1535], [12, 34534, 64, 765]]
    c = [1, 42, 300, 10, 59, 88]

    print("===mean===")
    print(tstat.mean(a))        # Output: 82.4
    print(tstat.mean(b))        # Output: 5.0

    print("===median===")
    print(tstat.median(a))      # Expected result: 42.0
    print(tstat.median(b))
    print(tstat.median(c))

    print("===quartiles===")
    print(tstat.quartiles(a))   # Expected result: [10.0, 59.0]
    print(tstat.quartiles(b))
    print(tstat.quartiles(c))

    print("===var===")
    print(tstat.var(a))         # Expected result: 12279.439999999999
    print(tstat.var(b))
    print(tstat.var(c))

    print("===std===")
    print(tstat.std(a))         # Expected result: 110.81263465868862
    print(tstat.std(b))
    print(tstat.std(c))
