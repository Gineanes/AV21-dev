from ConexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def atualizarCadastro(cod,tpmf, desc, val, ctg, dmov):
    conexao, cursor = conectar()
    try:
        sql =f"""UPDATE tb_dado
            SET TipoMovimentaçãoFinanceira='{tpmf}', descricao='{desc}', valor='{val}', categoria='{ctg}', dataMovimentacao='{dmov}' WHERE codigo='{cod}'
        """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Atualizar", "Cadastro atualizado!")
        return True
    
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha", "Falha ao atualizar"+str(falha))

        return False
    finally:
        conexao.close()
        cursor.close()