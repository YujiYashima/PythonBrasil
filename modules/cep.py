import requests

class Cep:
    def __init__(self, cep):
        cep = str(cep)
        if self.__validate(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido!!")
        
    def __str__(self):
        return self.__format()
        
    def __validate(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def __format(self):
        return "{}-{}".format(
            self.cep[:5],
            self.cep[5:]
        )
        
    def informations(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        res = requests.get(url)
        datas = res.json()
        return {
            "CEP": datas['cep'],
            "UF": datas['uf'],
            "Cidade": datas['localidade'],
            "DDD": datas['ddd']
        }