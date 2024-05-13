#titulo:Hashzap
# botao de iniciar chat
    # popup para entrar no chat(janelinha na tela)
    #titulo: bem vindo ao chat
    #campo para escrever seu nome
    #botão entrar no chat
    # quando entrar no chat: (aparece para todo mundo)
        # a mensagem que você entrou no chat
        # o campo e o botão de enviar mensagem
        # a cada mensagem que você envia (aparece para todo mundo)
        # Nome: Texto da Mensagem

#flet é o faz a função do back and e front and e tem 3 etapas
#1-importar
import flet as ft 

#2-criar a função principal do app 
def main(pagina):
    #3- criar todas as funcionalidades

    #criar o elemento
    titulo = ft.Text("HashZap")

    titulo_janela = ft.Text("Bem vindo ao Hashzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    

    def enviar_mensagem(evento):  
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value 
        mensagem =f"{nome_usuario}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        pagina.update()
    


    campo_mensagem =ft.TextField(label="DIgite a mensagem",on_submit=enviar_mensagem)
    botao_enviar_mensagem =ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_mensagem =ft.Row([campo_mensagem, botao_enviar_mensagem]) #pega row pega os dois elementos e coloca em uma linha 

# def é a função que o codigo vai fazer
    def entrar_chat (evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(campo_mensagem)
        pagina.add(botao_enviar_mensagem)
        pagina.add(linha_mensagem)
        mensagem = f"{campo_nome_usuario.value} Entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()


    botao_entar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entar])

    #funcionalidade do botão
    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    #botão 
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click= iniciar_chat)

    #adicionar o elemento na pagina
    pagina.add(titulo )
    pagina.add(botao_iniciar)
    
#rodar o app   
ft.app(main, view=ft.WEB_BROWSER)