# botão de iniciar char 
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
	# a mensagem que você entrou no chat
	# o campo e o botão de enviar mensagem
# a cada mensagem que você envia: (aparece para todo mundo)
	# Nome: texto da mensagem
# Jaguarzap

import flet as ft 

def main(pagina):
	texto = ft.Text("JaguarZap")

	chat = ft.Column()

	nome_usuario = ft.TextField(label="Digite seu nome")

	def enviar_mensagem_tunel(mensagem):
		tipo = mensagem["tipo"]
		if tipo == "mensagem":			
			texto_mensagem = mensagem["texto"]
			usuario_mensagem = mensagem["usuário"]
			# adicionar a mensagem no chat
			chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
		else:
			usuario_mensagem = mensagem["usuário"]
			chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", 
				size=12, italic=True, color=ft.colors.BLUE))
		pagina.update()

	# PUBSUB
	pagina.pubsub.subscribe(enviar_mensagem_tunel)

	def enviar_mensagem(evento):
		pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuário": nome_usuario.value, "tipo" : "mensagem"})
		# limpar o campo de mensagem
		campo_mensagem.value=""
		# campo_imagem.value=""

	campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
	#campo_imagem = ft.FilePicker(label="Envie um arquivo")

	botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

	def entrar_popup(evento):
		pagina.pubsub.send_all({"usuário": nome_usuario.value , "tipo" : "entrada"})
		# adicionar o chat
		pagina.add(chat)
		# fechar o popup
		popup.open = False
		# remover o botão iniciar chat
		pagina.remove(botao_iniciar)
		pagina.remove(texto)
		# criar o campo de mansagem do usuário
		# criar botão de enviar mensagem do usuário
		pagina.add(ft.Row(
			[campo_mensagem, botao_enviar_mensagem]
				))
		pagina.update()

	popup = ft.AlertDialog(
		open=False, 
		modal=True, 
		title=ft.Text("Bem vindo ao JaguarZap"), 
		content=nome_usuario,
		actions=[ft.ElevatedButton("Emtrar", on_click=entrar_popup)],
		)


	def entrar_chat(evento):
		pagina.dialog = popup
		popup.open = True
		pagina.update()

	botao_iniciar= ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

	pagina.add(texto)
	pagina.add(botao_iniciar)




ft.app(target=main)





