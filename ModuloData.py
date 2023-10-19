# Função para converter data para o formato de banco de dados
import datetime
def converterData(dataString): 
   minhaData = datetime.datetime.strptime(dataString, "%d/%m/%Y")
   dataFormatada = minhaData.date().isoformat()
   return dataFormatada