from bot.locators import L_IMOVEL, L_AUTO, L_CAMINHAO, L_MOTO
import logging, sys, os
from sqlalchemy import event, create_engine
from dotenv import load_dotenv
load_dotenv()



def print_log(msg):
    print(msg)
    logging.info(msg)  

def setup_log(path):
    logging.basicConfig(
    filename =  path + "\\" + f"{INFOS_BOT.get('bot_name')}.log", 
    level = logging.INFO, 
    # filemode='w', 
    encoding='utf8',
    format = "%(asctime)s :: %(message)s",
    datefmt = '%d-%m-%Y %H:%M:%S')

def gen_steps():
    try:
        if sys.argv[1] == 'pre_cre':
            return {
                1: False
            }     
        else:
            return {
                2: False
            }     
    except:
        return {
                1: False
            }     

TRYS = {
    'start': 1,
    'max': 10
}

INFOS_BOT = {
    'ticket': 'ticket_Uhuu',
    'ticket_full_name': 'ticket_Uhuu',
    'bot_name':'bot-ticket_Uhuu',
    'url': 'https://uhuu.com/busca?termo=S%C3%A3o+Paulo&page='
}

EMAILS = {
    'fabio_arao':'fabio.arao@turn2c.com'
}

EVENT_COLS = [
        "Id_evento",
        "Titulo",
        "Descricao",
        "Data_hora",
        "Local",
        "Valor_do_ingresso",
        "Link",
        "Imagem",
        "Faixa_etaria"
    ]


COLS = {
    'event': EVENT_COLS
}
# links = self.finds((By.CSS_SELECTOR, 'a[class*="btn link"]'), t=2)
# hrefs = [link.get_attribute("href") for link in links]

URLS = {
        "Tickets_Uhuu": "https://uhuu.com/busca?termo=S%C3%A3o+Paulo&page=",
        
        }