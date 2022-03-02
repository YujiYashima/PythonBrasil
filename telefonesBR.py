import re

class TelefonesBR:
    def __init__(self, tel):
        if self.validate_tel(tel):
            self.number = tel
        else:
            raise ValueError("Número Incorreto!!")
    
    def validate_tel(self, tel):
        pattern = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        response = re.findall(pattern, tel)
        if response:
            return True
        else:
            return False