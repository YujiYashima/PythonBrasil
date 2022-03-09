from datetime import datetime

class Hoje:
    """Classe referente ao Padrão de Data Nacional do Dia Atual."""

    def __init__(self):
        self.today = datetime.today()
        
    def __str__(self):
        return self.__format()
        
    def month(self):
        months_of_year = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        current_month = self.today.month
        return months_of_year[current_month - 1]
    
    def weekday(self):
        days_of_week = [
            "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Domingo"
        ]
        current_day = self.today.weekday()
        return days_of_week[current_day]
    
    def today_date(self):
        formated_date = self.today.strftime("%d/%m/%Y")
        return formated_date
    
    def now_hour(self):
        formated_hour = self.today.strftime("%H:%M")
        return formated_hour
    
    def __format(self):
        date = self.today_date()
        hour = self.now_hour()
        return date + " " + hour