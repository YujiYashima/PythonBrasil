from validate_docbr import CPF

class Cpf:
    """Classe referente ao Cadastro de Pessoas Físicas (CPF)."""
    
    # Inicialização do Objeto
    def __init__(self, cpf_number):
        cpf_number = str(cpf_number)
        if self.cpf_validate(cpf_number):
            self.cpf = cpf_number
        else:
            raise ValueError("CPF Inválido!!")
    
    # Representação da String
    def __str__(self):
        return self.cpf_format()
    
    # Validar Tamanho do CPF
    def cpf_validate(self, cpf_number):
        if len(cpf_number) == 11:
            validator = CPF()
            return validator.validate(cpf_number)
        else:
            raise ValueError("Quantidade de Dígitos Inválido!!")
    
    # Formatar CPF 
    def cpf_format(self):
        masked = CPF()
        return masked.mask(self.cpf)