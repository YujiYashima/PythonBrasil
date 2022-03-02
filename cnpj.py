from validate_docbr import CNPJ

class Cnpj:
    """Classe referente ao Cadastro Nacional da Pessoa Jurídica (CNPJ)."""
    
    # Inicialização do Objeto
    def __init__(self, cnpj_number):
        cnpj_number = str(cnpj_number)
        if self.cnpj_validate(cnpj_number):
            self.cnpj = cnpj_number
        else:
            raise ValueError("CNPJ Inválido!!")
    
    # Representação da String
    def __str__(self):
        return self.cnpj_format()
    
    # Validar Tamanho do CNPJ
    def cnpj_validate(self, cnpj_number):
        if len(cnpj_number) == 14:
            validator = CNPJ()
            return validator.validate(cnpj_number)
        else:
            raise ValueError("Quantidade de Dígitos Inválido!!")
    
    # Formatar CNPJ
    def cnpj_format(self):
        masked = CNPJ()
        return masked.mask(self.cnpj)