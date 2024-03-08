import flet as ft
    
def main(pagina):
    texto = ft.Text('Teste')

    chat = ft.Column()

    def send_message_tunel(message):
        add_message = ft.Text(message)
        chat.controls.append(add_message)
        pagina.update()

    pagina.pubsub.subscribe(send_message_tunel) # Túnel de comunicação

    def send_message(evento):
        pagina.pubsub.send_all(f"{nomeuser.value}: {camp_message.value}")
        # Limpar campo de mensagem
        camp_message.value = ""
        pagina.update()

    def digitando(evento):
        textpopup = ft.Text(f'{nomeuser.value} está digitando...')
        pagina.add(textpopup)
        pagina.update()

    camp_message = ft.TextField(label="Digite sua mensagem", on_change=digitando, on_submit=send_message)
    button_send = ft.TextButton('Enviar', on_click=send_message)
    line_send = ft.Row([camp_message, button_send]) # Deixar camp_message e button_send na mesma linha

    def enter_chat(evento):
        popup.open = False
        # Remove botão/texto
        pagina.remove(botao_inicial)
        pagina.remove(texto)
        # Adiciona chat/mensagem/botão enviar
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nomeuser.value} entrou no chat")
        #chat.controls.append(texto_welcome)
        pagina.add(line_send)
        # Atualizar
        pagina.update()

    textpopup = ft.Text('Seja bem-vindo!')
    nomeuser = ft.TextField(label='Escreva seu nome!', on_submit=enter_chat)
    botaoenter = ft.ElevatedButton('Entrar no chat', on_click=enter_chat)

    popup = ft.AlertDialog(open=False, modal=True, title=textpopup, content=nomeuser, actions=[botaoenter])

    def open_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_inicial = ft.ElevatedButton('CLIQUE AQUI', on_click=open_popup)

    pagina.add(texto)
    pagina.add(botao_inicial)

ft.app(target=main, view=ft.WEB_BROWSER)