from ConexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def inserir(tpmf, desc, val, ctg, dmov):
    conexao, cursor = conectar()
    try: 
        sql = f"""insert into tb_dado
                (TipoMovimentaçãoFinanceira, descricao, valor, categoria, dataMovimentacao)
                VALUES
                ('{tpmf}','{desc}','{val}','{ctg}','{dmov}')
        
        """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Cadastrado","com sucesso!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha", "Falha ao cadastrar: "+str(falha))
        return False
    
    finally:
        conexao.close()
        cursor.close()