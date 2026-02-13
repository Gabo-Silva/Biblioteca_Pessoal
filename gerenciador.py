# Principais bibliotecas que serão usadas.
import customtkinter as ctk
import sqlite3
# Criando a janela.
janela = ctk.CTk()
# Criando o banco de dados ou se conectandor a ele.
conexao = sqlite3.connect('biblioteca.db')
# Criando o cursor que irá executar os códigos
cursor = conexao.cursor()
# Criando as scrollbars
scroollbar = ctk.CTkScrollableFrame(
    janela, width=300, height=200, fg_color='#1A1A1D', corner_radius=0)
scroollbar_excluir = ctk.CTkScrollableFrame(
    janela, width=300, height=200, fg_color='#1A1A1D', corner_radius=0)
scroollbar_atualizar = ctk.CTkScrollableFrame(
    janela, width=300, height=200, fg_color='#1A1A1D', corner_radius=0)
# Editando a janela
ctk.set_appearance_mode('dark')
janela.config(bg='#1A1A1D')
janela.title('Biblioteca Pessoal')
janela.resizable(False, False)


def criarTabela():
    # Caso a tabela não existe ela será criada.
    cursor.execute('''
    create table if not exists livros (
                   id integer primary key not null,
                   titulo varchar(150) not null,
                   autor varchar(60) not null, 
                   genero varchar(50) not null,
                   status varchar(9) not null
                   );
''')


def destruirJanelaPrincipal():
    # Apaga a janela principal.
    frase_biblioteca_virtual.destroy()
    btn_cadastrar_livro.destroy()
    btn_listar_livros.destroy()
    btn_atualizar_livro.destroy()
    btn_remover_livro.destroy()


def janelaPrincipal():
    # Criando a tabela.
    criarTabela()
    # Variáveis globais que serão utilizadas no futuro.
    global btn_cadastrar_livro, btn_listar_livros, btn_atualizar_livro, btn_remover_livro, frase_biblioteca_virtual
    # Título
    frase_biblioteca_virtual = ctk.CTkLabel(
        master=janela, text='Sua Biblioteca Pessoal', font=('Times New Roman', 20))
    frase_biblioteca_virtual.pack(side='top', fill='x', pady=(20, 0))
    # Definindo o tamanho da janela.
    largura_janela_principal = 600
    altura_janela_principal = 500
    # Pegando o tamanho do monitor do usuário.
    largura_tela_usuario = janela.winfo_screenwidth()
    altura_tela_usuario = janela.winfo_screenheight()
    # Definindo a posição da janela.
    x = (largura_tela_usuario - largura_janela_principal) // 2
    y = (altura_tela_usuario - altura_janela_principal) // 2
    # Configurando a janela.
    janela.geometry(
        f'{largura_janela_principal}x{altura_janela_principal}+{x}+{y}')
    # Botões que levam pra outra página.
    btn_cadastrar_livro = ctk.CTkButton(
        janela, text='Cadastrar Livro', command=lambda: cadastrarLivro('Cadastramento de Livros'), width=300, height=50, border_color='#C3073F', border_width=1, fg_color='#1A1A1D', hover_color='#C3073F', text_color='white')
    btn_cadastrar_livro.pack(expand=False, side='top', pady=(30, 0))
    btn_listar_livros = ctk.CTkButton(
        janela, text='Listar Todos os Livros', command=listarLivros, width=300, height=50, border_color='#C3073F', border_width=1, fg_color='#1A1A1D', hover_color='#C3073F', text_color='white')
    btn_listar_livros.pack(expand=False, side='top', pady=(30, 0))
    btn_atualizar_livro = ctk.CTkButton(
        janela, text='Atualizar Informações dos Livros', command=atualizarLivro, width=300, height=50, border_color='#C3073F', border_width=1, fg_color='#1A1A1D', hover_color='#C3073F', text_color='white')
    btn_atualizar_livro.pack(expand=False, side='top', pady=(30, 0))
    btn_remover_livro = ctk.CTkButton(
        janela, text='Remover Livro', width=300, command=excluirLivro, height=50, border_color='#C3073F', border_width=1, fg_color='#1A1A1D', hover_color='#C3073F', text_color='white')
    btn_remover_livro.pack(expand=False, side='top', pady=(30, 0))
    janela.mainloop()


def cadastrarLivro(texto, id_para_atualizar=0, atualizar=False):
    # Variáveis globais que serão utilizadas no futuro.
    global caixa_texto_nome_do_livro, caixa_texto_nome_do_autor, caixa_texto_genero_do_livro, cb_status, mensagem_de_erro
    # Mensagem de erro que está vazia por enquanto, simbolizado que nada ocorreu.
    mensagem_de_erro = ctk.CTkLabel(janela, text='')
    # Lista que será utilizada no combobox.
    status_de_leitura = ['Não lido', 'Lendo', 'Concluído']
    # Chamando função que apaga a página principal.
    destruirJanelaPrincipal()
    # Título.
    titulo = ctk.CTkLabel(
        master=janela, text=f'{texto}', font=('Times New Roman', 20))
    titulo.pack(side='top', fill='x', pady=(20, 0))
    # Informações que devem ser preenchidas.
    nome_do_livro = ctk.CTkLabel(
        master=janela, text='Nome do Livro: ', text_color='white', font=('Arial', 12), fg_color='#1A1A1D')
    nome_do_livro.place(x=100, y=65)
    caixa_texto_nome_do_livro = ctk.CTkEntry(
        master=janela, width=300, height=10, border_color='#C3073F', border_width=1, corner_radius=0, placeholder_text='Digite Algo...')
    caixa_texto_nome_do_livro.place(x=200, y=69)

    nome_do_autor = ctk.CTkLabel(
        master=janela, text='Nome do Autor: ', text_color='white', font=('Arial', 12), fg_color='#1A1A1D', corner_radius=0)
    nome_do_autor.place(x=100, y=100)
    caixa_texto_nome_do_autor = ctk.CTkEntry(
        master=janela, width=300, height=10, border_color='#C3073F', border_width=1, corner_radius=0, placeholder_text='Digite Algo...')
    caixa_texto_nome_do_autor.place(x=200, y=105)

    genero_do_livro = ctk.CTkLabel(
        master=janela, text='Gênero do Livro:', text_color='white', font=('Arial', 12), fg_color='#1A1A1D')
    genero_do_livro.place(x=98, y=135)
    caixa_texto_genero_do_livro = ctk.CTkEntry(
        master=janela, width=300, height=10, border_color='#C3073F', border_width=1, corner_radius=0, placeholder_text='Digite Algo...')
    caixa_texto_genero_do_livro.place(x=200, y=140)

    status_do_livro = ctk.CTkLabel(
        master=janela, text='Status de leitura:', text_color='white', font=('Arial', 12), fg_color='#1A1A1D')
    status_do_livro.place(x=98, y=180)
    cb_status = ctk.CTkComboBox(janela, values=status_de_leitura, border_color='#C3073F',
                                button_color='#C3073F', border_width=2, button_hover_color='#950740', dropdown_fg_color='#4E4E50', state='readonly')
    cb_status.set('')
    cb_status.place(x=200, y=180)
    # Botão que confirma o cadastra do livro.
    btn_confirmar = ctk.CTkButton(janela, text='Confirmar', command=lambda: confirmar(atualizar, id_para_atualizar), border_color='#C3073F',
                                  border_width=1, fg_color='#1A1A1D', hover_color='#C3073F', text_color='white')
    btn_confirmar.place(x=140, y=300)
    # Botão que retorna a página principal.
    btn_sair = ctk.CTkButton(janela, text='Sair', command=lambda: sair(btn=1, atualizar=atualizar), border_color='#C3073F', border_width=1,
                             fg_color='#1A1A1D', hover_color='#C3073F', text_color='white')
    btn_sair.place(x=330, y=300)
    cursor.execute('select * from livros')
    # Caso seja pra atualizar um determinado um livro, essa parte do código será ativada.
    if texto == 'Atualização do Livro':
        # Apagar o widgets da função atualizar.
        for widgets in scroollbar_atualizar.winfo_children():
            widgets.destroy()
        scroollbar_atualizar.pack_forget()
        # Pega as informações.
        cursor.execute(f'select * from livros where id = {id_para_atualizar}')
        # Adiciona as informações nas caixas de texto.
        for informacoes in cursor.fetchall():
            caixa_texto_nome_do_livro.insert(0, f'{informacoes[1]}')
            caixa_texto_nome_do_autor.insert(0, f'{informacoes[2]}')
            caixa_texto_genero_do_livro.insert(0, f'{informacoes[3]}')
            cb_status.set(f'{informacoes[4]}')


def confirmar(atualizar, id_para_atualizar):
    from tkinter import messagebox
    # Pegando as informações das caixas de texto.
    conteudo_nome_do_livro = caixa_texto_nome_do_livro.get().strip()
    conteudo_nome_do_autor = caixa_texto_nome_do_autor.get().strip()
    conteudo_genero = caixa_texto_genero_do_livro.get().strip()
    conteudo_status = cb_status.get()
    # Vendo se há alguma vazia.
    if len(conteudo_nome_do_livro) == 0 or len(conteudo_nome_do_autor) == 0 or len(conteudo_genero) == 0 or len(conteudo_status) == 0:
        # Se houve uma vazia, uma mensagem de erro será exibida.
        mensagem_de_erro.configure(
            text='Por favor, preencha todos os campos.', text_color='#FF0000', fg_color='#1A1A1D')
        mensagem_de_erro.place(x=200, y=350)
    else:
        # Se o parâmetro atualizar for verdadeiro, esse bloco de comando será ativado.
        if atualizar:
            # Atualizador as informações no banco de dados.
            cursor.execute(
                f'update livros set titulo = "{conteudo_nome_do_livro}", autor = "{conteudo_nome_do_autor}", genero = "{conteudo_genero}", status = "{conteudo_status}" where id = {id_para_atualizar}')
            conexao.commit()
            # Exibindo mensagem que tudo deu certo.
            messagebox.showinfo('Biblioteca Pessoal',
                                'Livro Atualizado com Sucesso ')
            # Chamando a função que volta pra página de atualizar.
            atualizarLivro()
        else:
            # Mensagem dizendo que tudo deu certo.
            mensagem_de_erro.configure(
                text='Livro Cadastrado com Sucesso', text_color="#15FF00", fg_color='#1A1A1D')
            mensagem_de_erro.place(x=215, y=350)
            # Inserindo as informações no banco de dados.
            cursor.execute(
                f'insert into livros (titulo, autor, genero, status) values ("{conteudo_nome_do_livro}", "{conteudo_nome_do_autor}", "{conteudo_genero}", "{conteudo_status}")')
            conexao.commit()
            # Apagando o conteúdo da caixa de texto.
            caixa_texto_nome_do_livro.delete(0, ctk.END)
            caixa_texto_nome_do_autor.delete(0, ctk.END)
            caixa_texto_genero_do_livro.delete(0, ctk.END)
            cb_status.set('')


def listarLivros():
    # Chamando função que apaga a página principal.
    destruirJanelaPrincipal()
    # Pegando as informações na tabela.
    cursor.execute('select * from livros')
    # Colocando a scrollbar.
    scroollbar.pack(pady=20, padx=20, fill="both", expand=True)
    # Botão que se apertado voltar pra página original.
    setinha_pra_sair = ctk.CTkButton(scroollbar, command=lambda: sair(btn=2), text='←', font=(
        'Arial', 30), width=10, height=45, fg_color='#1A1A1D', anchor='nw', hover_color="#464646", border_width=1)
    setinha_pra_sair.pack(side='top', anchor='nw', pady=0)
    # Título
    frase_bem_vindo = ctk.CTkLabel(
        master=scroollbar, text='Seus Livros', font=('Times New Roman', 20))
    frase_bem_vindo.pack(side='top', fill='x', pady=(0, 0))
    # Exibindo as informações.
    for indice, l in enumerate(cursor.fetchall()):
        livro = ctk.CTkFrame(master=scroollbar, fg_color='#1A1A1D',
                             border_color='#C3073F', border_width=1, corner_radius=10)
        livro.pack(pady=10)
        id_livro = ctk.CTkLabel(master=livro, text=f'{indice + 1}', width=370)
        id_livro.pack(padx=10, pady=10)

        info_livro = ctk.CTkFrame(master=livro, fg_color='#1A1A1D',
                                  border_color='#C3073F', border_width=1, corner_radius=0)
        info_livro.pack(pady=0)
        informacoes = ctk.CTkLabel(
            master=info_livro, text=f'Título: {l[1]}\n\nAutor: {l[2]}\n\nGênero: {l[3]}\n\nStatus: {l[4]}', width=370, height=110)
        informacoes.pack(padx=10, pady=10)


def atualizarLivro():
    # Chamando função que apaga a página principal.
    destruirJanelaPrincipal()
    for widgets in janela.winfo_children():
        if str(widgets) in '.!ctkframe' or str(widgets) in '.!ctkframe2' or str(widgets) in '.!ctkframe3':
            scroollbar.pack_forget()
            scroollbar_excluir.pack_forget()
            scroollbar_atualizar.pack_forget()
        else:
            widgets.destroy()
    # Pegando as informações da tabela.
    cursor.execute('select * from livros')
    # Colocando a scrollbar.
    scroollbar_atualizar.pack(pady=20, padx=20, fill="both", expand=True)
    # Botão que se apertado voltar pra página original.
    seta_pra_sair_do_atualizar = ctk.CTkButton(scroollbar_atualizar, command=lambda: sair(btn=4), text='←', font=(
        'Arial', 30), width=10, height=45, fg_color='#1A1A1D', anchor='nw', hover_color="#464646", border_width=1)
    seta_pra_sair_do_atualizar.pack(side='top', anchor='nw', pady=0)
    # Título.
    frase_iniciacao_do_atualizar = ctk.CTkLabel(
        master=scroollbar_atualizar, text='Seus Livros', font=('Times New Roman', 20))
    frase_iniciacao_do_atualizar.pack(side='top', fill='x', pady=(0, 0))
    # Exibindo as informações.
    for indice, l in enumerate(cursor.fetchall()):
        frame_indice_do_atualizar = ctk.CTkFrame(master=scroollbar_atualizar, fg_color='#1A1A1D',
                                                 border_color='#C3073F', border_width=1, corner_radius=10, width=390, height=50)
        frame_indice_do_atualizar.pack(pady=10)
        # Caso esse botão seja apertado, o usuário poderá modificar alguma informação do livro salvo.
        btn_atualizar_livro = ctk.CTkButton(frame_indice_do_atualizar, text='📝', command=lambda id=l[0]: cadastrarLivro(
            texto='Atualização do Livro', id_para_atualizar=id, atualizar=True), width=10, fg_color='#1A1A1D', hover_color="#464646")
        btn_atualizar_livro.place(x=357, y=10)
        id_livro_atualizar = ctk.CTkLabel(
            master=frame_indice_do_atualizar, text=f'{indice + 1}')
        id_livro_atualizar.pack(padx=10, pady=10, anchor="n")
        info_livro_atualizar = ctk.CTkFrame(master=frame_indice_do_atualizar, fg_color='#1A1A1D',
                                            border_color='#C3073F', border_width=1, corner_radius=0)
        info_livro_atualizar.pack(pady=0)
        informacoes_do_atualizar = ctk.CTkLabel(
            master=info_livro_atualizar, text=f'Título: {l[1]}\n\nAutor: {l[2]}\n\nGênero: {l[3]}\n\nStatus: {l[4]}', width=370, height=110)
        informacoes_do_atualizar.pack(padx=10, pady=10)


def excluirLivro():
    # Chamando função que apaga a página principal.
    destruirJanelaPrincipal()
    # Pegando as informações da tabela.
    cursor.execute('select * from livros')
    # Colocando a scrollbar.
    scroollbar_excluir.pack(pady=20, padx=20, fill="both", expand=True)
    # Botão que se apertado voltar pra página original.
    seta_pra_sair = ctk.CTkButton(scroollbar_excluir, command=lambda: sair(btn=3), text='←', font=(
        'Arial', 30), width=10, height=45, fg_color='#1A1A1D', anchor='nw', hover_color="#464646", border_width=1)
    seta_pra_sair.pack(side='top', anchor='nw', pady=0)
    # Título.
    frase_iniciacao = ctk.CTkLabel(
        master=scroollbar_excluir, text='Seus Livros', font=('Times New Roman', 20))
    frase_iniciacao.pack(side='top', fill='x', pady=(0, 0))
    # Exibindo as informações.
    for indice, l in enumerate(cursor.fetchall()):
        frame_indice = ctk.CTkFrame(master=scroollbar_excluir, fg_color='#1A1A1D',
                                    border_color='#C3073F', border_width=1, corner_radius=10, width=390, height=50)
        frame_indice.pack(pady=10)
        # Botão que se apertado, chama a funcão responsável por apagar o item selecionado.
        btn_excluir = ctk.CTkButton(frame_indice, text='X', command=lambda id=l[0]: excluir(
            id), width=10, fg_color='#1A1A1D', hover_color="#464646")
        btn_excluir.place(x=357, y=10)
        id_livro_excluir = ctk.CTkLabel(
            master=frame_indice, text=f'{indice + 1}')
        id_livro_excluir.pack(padx=10, pady=10, anchor="n")
        info_livro_excluir = ctk.CTkFrame(master=frame_indice, fg_color='#1A1A1D',
                                          border_color='#C3073F', border_width=1, corner_radius=0)
        info_livro_excluir.pack(pady=0)
        informacoes_do_excluir = ctk.CTkLabel(
            master=info_livro_excluir, text=f'Título: {l[1]}\n\nAutor: {l[2]}\n\nGênero: {l[3]}\n\nStatus: {l[4]}', width=370, height=110)
        informacoes_do_excluir.pack(padx=10, pady=10)


def excluir(id_para_excluir):
    from tkinter import messagebox
    # Caixa de messagem que pergunta se o usuário deseja realmente apagar o item.
    resposta = messagebox.askokcancel(
        'Biblioteca Pessoal', 'Deseja realmente apagar o livro da sua biblioteca?')
    # Se sim, esse bloco de comando acontece.
    if resposta:
        # Apaga o item da tabela.
        cursor.execute(f'delete from livros where id = {id_para_excluir}')
        conexao.commit()
        # Apaga todos os widgets da função excluir.
        for widgets in scroollbar_excluir.winfo_children():
            widgets.destroy()
        scroollbar_excluir.pack_forget()
        # Chama a função excluir novamente.
        excluirLivro()


def sair(btn, atualizar=False):
    # Dependendo do parâmetro btn, algum bloco de comando será ativado.
    if btn == 1:
        # Apaga todos os widgets da página cadastrar tirando os scrollbar.
        for widgets in janela.winfo_children():
            if str(widgets) in '.!ctkframe' or str(widgets) in '.!ctkframe2' or str(widgets) in '.!ctkframe3':
                scroollbar.pack_forget()
                scroollbar_excluir.pack_forget()
                scroollbar_atualizar.pack_forget()
            else:
                widgets.destroy()
    elif btn == 2:
        # Apaga todos os widgets da página de listagem dos livros.
        for widgets in scroollbar.winfo_children():
            widgets.destroy()
        scroollbar.pack_forget()
    elif btn == 3:
        # Apaga todos os widgets da página de deletar dos livros.
        for widgets in scroollbar_excluir.winfo_children():
            widgets.destroy()
        scroollbar_excluir.pack_forget()
    elif btn == 4:
        # Apaga todos os widgets da página de atualização os livros.
        for widgets in scroollbar_atualizar.winfo_children():
            widgets.destroy()
        scroollbar_atualizar.pack_forget()
    # Se o parâmetro atualizar for verdadeiro, chama a função atualizarLivro.
    if atualizar:
        atualizarLivro()
    # Se não chama a função janelaPrincipal.
    else:
        janelaPrincipal()
