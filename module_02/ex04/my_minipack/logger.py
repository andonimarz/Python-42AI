import time
from random import randint
import os

def log(param_func):
    def return_func(*args, **kwargs):
        username = os.getlogin()
        log_file = open("machine.log", "a")
        start_time = time.time()
        result = param_func(*args, **kwargs)
        exec_time = round((time.time() - start_time), 3)
        print(f"({username})Running: \
{param_func.__name__.capitalize().replace('_', ' '):<{20}}   \
[ exec-time = {exec_time:.3f} {'ms' if exec_time < 1 else 's'} ]", \
file=log_file)
        log_file.close()
        return result
    return return_func


class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)