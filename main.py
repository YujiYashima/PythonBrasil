from sqlite3 import Date
from modules.cep import Cep
from modules.cnpj import Cnpj
from modules.cpf import Cpf
from modules.telefonesBR import Celular, Telefone
from modules.dataHoje import Hoje

#--------------------------------------------------#
myCEP = "01311000"
CEP = Cep(myCEP)
print(CEP) 
print(CEP.informations())
#--------------------------------------------------#

#--------------------------------------------------#
myCNPJ = "00573184000189"
CNPJ = Cnpj(myCNPJ)
print(CNPJ)
print(CNPJ.informations())
#--------------------------------------------------#

#--------------------------------------------------#
myCPF = "59530216076"
CPF = Cpf(myCPF)
print(CPF)
#--------------------------------------------------#

#--------------------------------------------------#
myCelular = "17997435399"
myTelefone = "1320295743"
CELULAR = Celular(myCelular)
TELEFONE = Telefone(myTelefone)
print(CELULAR)
print(TELEFONE)
#--------------------------------------------------#

#--------------------------------------------------#
hoje = Hoje()
print(hoje)
print(hoje.today_date())
print(hoje.now_hour())
print(hoje.month())
print(hoje.weekday())
#--------------------------------------------------#
