import re

class Telefone:
    """Classe referente ao Padrão Nacional de Número de Telefone Fixo."""
    
    def __init__(self, tel_number):
        if self.tel_validate(tel_number):
            self.number = tel_number
        else:
            raise ValueError("Número Incorreto!!")
        
    def __str__(self):
        return self.tel_format()
    
    def tel_validate(self, tel_number):
        pattern = "(\d{2})(\d{4})(\d{4})"
        response = re.findall(pattern, tel_number)
        if response:
            return True
        else:
            return False
        
    def tel_format(self):
        pattern = "(\d{2})(\d{4})(\d{4})"
        response = re.search(pattern, self.number)
        formated_tel = "({}) {}-{}".format(
            response.group(1),
            response.group(2),
            response.group(3),
        )
        return formated_tel
    
class Celular:
    """Classe referente ao Padrão Nacional de Número de Celular."""
    
    def __init__(self, cel_number):
        if self.cel_validate(cel_number):
            self.number = cel_number
        else:
            raise ValueError("Número Incorreto!!")
        
    def __str__(self):
        return self.cel_format()
    
    def cel_validate(self, cel_number):
        pattern = "(\d{2})(\d{5})(\d{4})"
        response = re.findall(pattern, cel_number)
        if response:
            return True
        else:
            return False
        
    def cel_format(self):
        pattern = "(\d{2})(\d{5})(\d{4})"
        response = re.search(pattern, self.number)
        formated_cel = "({}) {}-{}".format(
            response.group(1),
            response.group(2),
            response.group(3)
        )
        return formated_cel