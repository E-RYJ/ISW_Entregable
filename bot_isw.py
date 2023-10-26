from config import*
import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply
from functionsDB import DataBase
from functions import fuciones

bot = telebot.TeleBot(TELEGRAM_TOKEN)
usuario={}
#comandos /text
#comandos DML Y DQL:

#comandos bienbenidas
@bot.message_handler(commands=["start","ayuda","help"])
def cmd_start(message):
        bot.reply_to(message,fuciones.cmd_start(message),parse_mode="MarkdownV2",disable_web_page_preview=True)

@bot.message_handler(commands=["borrar"])
def preguntar_dlt_usr(message):
        msg = bot.send_message(message.chat.id,"¿Nombre del usuario a eliminar usuario que deas eliminar?") 
        
        bot.register_next_step_handler(msg,dlt_usr)

def dlt_usr(message):
        
        msg=message.text
        database = DataBase()
         
        user = database.delete_user(msg)
        if user != False:
                bot.reply_to(message,"<b>Usuario Eliminado con exito</b>",parse_mode="html",disable_web_page_preview=True)
                users = database.select_users()
                texto_html =""
                contador=0

                for renglon in users:
                        user = str(users[contador]).split(",")
                        user_name = str(user[1])
                        phone = str(user[2])
                        mail = str(user[3])

                        print(user_name,phone,mail)

                        texto_html += "<b>Lista</b>" + "\n"
                        texto_html += "<b>Nombre: </b> "+user_name+"\n"
                        texto_html +="<b>Telefono: </b>"+phone+ "\n"
                        texto_html +="<b>E-mail: </b>"+mail+"\n"+"\n"
                        contador+=1
                bot.reply_to(message,texto_html,parse_mode="html",disable_web_page_preview=True)
        else: 
                bot.reply_to(message,"<b>Usuario no encontrado</b>",parse_mode="html",disable_web_page_preview=True)

@bot.message_handler(commands=["buscar"])
def preguntar_srch_usr(message):
        msg = bot.send_message(message.chat.id,"¿Cual usuario que deas buscarr?") 
        
        bot.register_next_step_handler(msg,srch_usr)

def srch_usr(message):
        msg=message.text
        database = DataBase()
         
        user = database.select_user(msg)
        if user != False:
                bot.reply_to(message,"<b>Usuario encontrado con exito</b>",parse_mode="html",disable_web_page_preview=True)
                texto_html =""
                
                 
                user_name       =       user[1]
                phone           =       user[2]
                mail            =       user[3]

                print(user_name,phone,mail)

                texto_html += "<b>Sus datos son:</b>" + "\n"
                texto_html += "<b>Nombre: </b> "+user_name+"\n"
                texto_html +="<b>Telefono: </b>"+phone+ "\n"
                texto_html +="<b>E-mail: </b>"+mail+"\n"+"\n"
                
                bot.reply_to(message,texto_html,parse_mode="html",disable_web_page_preview=True)
        else: 
                bot.reply_to(message,"<b>Usuario no encontrado</b>",parse_mode="html",disable_web_page_preview=True)

@bot.message_handler(commands=["consulta"])
def preguntar_usr(message):
        bot.send_message(message.chat.id,"La Lista de usuarios es la siguiente")
        database = DataBase()
        users = database.select_users()
        
        texto_html =""
        contador=0

        for renglon in users:
                user = str(users[contador]).split(",")
                user_name = str(user[1])
                phone = str(user[2])
                mail = str(user[3])

                print(user_name,phone,mail)

                texto_html += "<b>Lista</b>" + "\n"
                texto_html += "<b>Nombre: </b> "+user_name+"\n"
                texto_html +="<b>Telefono: </b>"+phone+ "\n"
                texto_html +="<b>E-mail: </b>"+mail+"\n"+"\n"
                contador+=1

        bot.reply_to(message,texto_html,parse_mode="html",disable_web_page_preview=True)


@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
        #gestionar mensajes
        msg = message.text.split(" ")
        if message.text.startswith("/"):
                #send
                bot.send_message(message.chat.id,"Comando no disponible")
                bot.send_message(message.chat.id,"Utilice /help")
        elif msg[0]=="consultar":
                database = DataBase()
         
                user = database.select_user(msg[1])
                if user != False:
                        bot.reply_to(message,"<b>Usuario encontrado con exito</b>",parse_mode="html",disable_web_page_preview=True)
                        texto_html =""
                        
                        
                        user_name       =       user[1]
                        phone           =       user[2]
                        mail            =       user[3]

                        print(user_name,phone,mail)

                        texto_html += "<b>Sus datos son:</b>" + "\n"
                        texto_html += "<b>Nombre: </b> "+user_name+"\n"
                        texto_html +="<b>Telefono: </b>"+phone+ "\n"
                        texto_html +="<b>E-mail: </b>"+mail+"\n"+"\n"
                        
                        bot.reply_to(message,texto_html,parse_mode="html",disable_web_page_preview=True)
                else: 
                        bot.reply_to(message,"<b>Usuario no encontrado</b>",parse_mode="html",disable_web_page_preview=True)
        elif msg[0]=="borrar":
                database = DataBase()
                user = database.delete_user(msg[1])
                
                if user != False:
                        bot.reply_to(message,"<b>Usuario Eliminado con exito</b>",parse_mode="html",disable_web_page_preview=True)
                        users = database.select_users()
                        texto_html =""
                        contador=0

                        for renglon in users:
                                user = str(users[contador]).split(",")
                                user_name = str(user[1])
                                phone = str(user[2])
                                mail = str(user[3])

                                print(user_name,phone,mail)

                                texto_html += "<b>Lista</b>" + "\n"
                                texto_html += "<b>Nombre: </b> "+user_name+"\n"
                                texto_html +="<b>Telefono: </b>"+phone+ "\n"
                                texto_html +="<b>E-mail: </b>"+mail+"\n"+"\n"
                                contador+=1
                        bot.reply_to(message,texto_html,parse_mode="html",disable_web_page_preview=True)
                else: 
                        bot.reply_to(message,"<b>Usuario no encontrado</b>",parse_mode="html",disable_web_page_preview=True)
        else:
                bot.send_message(message.chat.id,"Buen dia!")

if __name__=='__main__':
        print("Bot iniciado")
        bot.infinity_polling()
        print("Fin")