from config import*
import telebot
from functionsDB import DataBase

class fuciones:
    def cmd_start(message):
        
        texto_html = "*Lista de comandos*" + "\n"
        texto_html += "/help : _Ayuda general_"+"\n"
        texto_html +='/borrar : Elimina un usaurio' + '\n'
        texto_html +='/busacar : busca un usaurio' + '\n'
        texto_html +='/consulta : Consulta un usuario'
        return texto_html
        bot.reply_to(message,texto_html,parse_mode="MarkdownV2",disable_web_page_preview=True)


