class Account(object): 
    
    ID_COUNT = 1

    def __init__(self, name, **kwargs): 
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT 
        Account.ID_COUNT += 1 
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    
    def transfer(self, amount):
        self.value += amount

    def __str__(self):
        return f"Name: {self.name}, value: {self.value}"

    def __repr__(self):
        return f"Name: {self.name}, value: {self.value}"
    

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return   True if success, False if an error occured
        """
            # test if new_account is an Account() instance and if
            # it can be appended to the attribute accounts
            # ... Your code ...
        try:
            if isinstance(new_account, Account) == False:
                raise AttributeError("Invalid new_account.")
            dct = new_account.__dict__
            for acc in self.accounts:
                if dct['name'] == acc.__dict__['name']:
                    raise AttributeError("an account with this name already exists.")
            self.accounts.append(new_account)
            return True
        except AttributeError as e:
            print("Error:",e)
            return False

    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
            # test if new_account is an Account() instance and if
            # it can be appended to the attribute accounts
            # ... Your code ...
        try:
            coincidences = 0
            for acc in self.accounts:
                if origin == acc.__dict__['name']:
                    giver = acc
                    coincidences += 1
                if dest == acc.__dict__['name']:
                    taker = acc
                    coincidences += 1
            if coincidences != 2:
                raise AttributeError("Invalid accounts")
            self._check_account(giver)
            if ((giver.__dict__['value'] - amount) < 0 or amount < 0): 
                raise AttributeError("Invalid amount")
            self._check_account(taker)
            for acc in self.accounts:
                if origin == acc.__dict__['name']:
                    acc.__dict__['value'] -= amount
                if dest == acc.__dict__['name']:
                    acc.__dict__['value'] += amount
            return True
        except Exception as e:
            print(e)
            return False

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        for acc in self.accounts:
            if name == acc.__dict__['name']:
                try:
                    self._check_account(acc)
                except AttributeError as e:
                    if len(e.args) == 1:
                        if e.args[0] == 'Odd atributes.':
                            acc.__setattr__('odd_fix', 0)
                            return True
                    if len(e.args) == 2:
                        if e.args[1] == 'atribute starting with b.':
                            fixed_name = e.args[0][1::]
                            fixed_value = acc.__dict__.pop(e.args[0])
                            acc.__setattr__(fixed_name, fixed_value)
                            return True
        return False

    def _check_account(self, new_account):
        dct = new_account.__dict__
        if ('id' or 'name' or 'value') not in dct:
            raise AttributeError("Missing atributes.")
        if isinstance(dct['name'],str) == False:
            raise AttributeError("name is not an str.")
        if isinstance(dct['id'],(int)) == False:
            raise AttributeError("id is not a valid number.")
        if isinstance(dct['value'],(int, float)) == False:
            raise AttributeError("value is not a valid number.")
        if len(dct) % 2 == 0:
            raise AttributeError("Odd atributes.")
        for item in dct:
            if item.startswith('b'):
                raise AttributeError(item,"atribute starting with b.")

    def __str__(self):
        return f"{self.accounts}"

    def __repr__(self):
        return f"{self.accounts}"