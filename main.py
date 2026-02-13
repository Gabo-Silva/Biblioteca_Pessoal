# Importador minhas funções.
import gerenciador
# Importador a biblioteca sqlite3.
import sqlite3
# Criar ou conecta ao nosso banco de dados.
conexao = sqlite3.connect('biblioteca.db')
# Chama função que exibe a janela principal.
gerenciador.janelaPrincipal()
# No final de tudo, o banco de dados será fechado.
conexao.close()
