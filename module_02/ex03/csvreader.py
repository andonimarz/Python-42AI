class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.error = 0
        try:
            self.file = open(filename, 'r')
            self.data = [row.strip().split(self.sep) for row in self.file.readlines()]
            for row in self.data:
                if len(row) != len(self.data[0]):
                    raise Exception("Bad format")
        except FileNotFoundError as e:
            #print("Error:", e)
            self.error = 1
        except Exception as e:
            print("Error:", e)
            self.error = 1

    def __enter__(self):
        if self.error:
            return None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return True

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom. 
            Return:
                nested list (list(list, list, ...)) representing the data.
        """
        data = self.data[self.skip_top + 1 if self.header else self.skip_top:\
        len(self.data) - self.skip_bottom]
        if self.header:
            header = self.getheader()
            data.insert(0,header)
        return data

    def getheader(self):
        """ Retrieves the header from csv file. 
            Returns:
                list: representing the data (when self.header is True). 
                None: (when self.header is False).
        """
        if self.header == False:
            return None 
        return self.data[0]
    
    def __str__(self):
        if self.error == 1:
            return None
        txt = ("filename: ", self.filename, ", sep: '", self.sep, \
        "', header: ", self.header, ", skip top: ", self.skip_top, ", skip bottom: ", self.skip_bottom)
        return "".join(str(element) for element in txt)

if __name__ == "__main__":
    with CsvReader('good.csv', ',', False, 0, 0) as file:
        data = file.getdata()
        print(file)
        print("data:")
        print(data)
        print("Header:")
        header = file.getheader()
        print(header)

""" if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted") """

""" if __name__ == "__main__":
    with CsvReader('good.csv') as file: 
        data = file.getdata()
    header = file.getheader() """