class GotCharacter:
    
    def __init__(self, first_name):
        self.first_name = first_name
        self.is_alive = True
    
class Stark(GotCharacter):
    '''
    A class representing the Stark family. Or when bad things happen to good people.
    '''
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    
    def print_house_words(self):
        print(self.house_words)
        return None
    
    def die(self):
        self.is_alive = False
        return None

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Error: invalid arg number.") 
    else:
        text_analyzer(args[0])
