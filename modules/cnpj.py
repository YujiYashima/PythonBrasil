from validate_docbr import CNPJ
import requests

class Cnpj:
    """Classe referente ao Cadastro Nacional da Pessoa Jurídica (CNPJ)."""
    
    # Inicialização do Objeto
    def __init__(self, cnpj):
        cnpj = str(cnpj)
        if self.__validate(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ Inválido!!")
    
    # Representação da String
    def __str__(self):
        return self.__format()
    
    # Validar Tamanho do CNPJ
    def __validate(self, cnpj):
        if len(cnpj) == 14:
            validator = CNPJ()
            return validator.validate(cnpj)
        else:
            raise ValueError("Quantidade de Dígitos Inválido!!")
    
    # Formatar CNPJ
    def __format(self):
        masked = CNPJ()
        return masked.mask(self.cnpj)
    
    def informations(self):
        url = "https://brasilapi.com.br/api/cnpj/v1/{}".format(self.cnpj)
        res = requests.get(url)
        datas = res.json()
        return {
            "CNPJ": self.__format(),
            "Razão Social": datas['razao_social'],
            "Nome Fantasia": datas['nome_fantasia'],
            "UF": datas['uf'],
            "Cidade": datas['municipio'],
            "Natureza Jurídica": datas['natureza_juridica'],
            "Data de Início": datas['data_inicio_atividade'],
            "Descrição": datas['cnae_fiscal_descricao']
        }