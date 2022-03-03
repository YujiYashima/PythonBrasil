import requests

class Cep:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_validate(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido!!")
        
    def __str__(self):
        return self.cep_format()
        
    def cep_validate(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def cep_format(self):
        return "{}-{}".format(
            self.cep[:5],
            self.cep[5:]
        )
        
    def cep_datas(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        res = requests.get(url)
        datas = res.json()
        return {
            "CEP": datas['cep'],
            "UF": datas['uf'],
            "Cidade": datas['localidade'],
            "DDD": datas['ddd']
        }