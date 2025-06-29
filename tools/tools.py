from bot.settings import *
from bot.locators import *
import os, time
from abc import ABC
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from fake_useragent import UserAgent
from dotenv import load_dotenv
load_dotenv()


class Email_sender():
  
    def __init__(self, user, password):
        self.host = "imap.gmail.com"
        self.port = 587
        self.user = user
        self.password = password

    def send_email(self, send_to, msg, *file_name_list, cc_list=None):
        server = smtplib.SMTP(self.host, self.port)        
        server.ehlo()
        server.starttls()
        server.login(self.user, self.password)        
        message = msg    
        email_msg = MIMEMultipart()
        email_msg['From'] = self.user
        email_msg['To'] = send_to
        email_msg['Subject'] =  'BOT - TICKET_UHUU.COM'    

        all_recipients = [send_to]

        if cc_list:
            if isinstance(cc_list, list):
                email_msg['Cc'] = ', '.join(cc_list)
                all_recipients += cc_list
            else:
                email_msg['Cc'] = cc_list
                all_recipients.append(cc_list)

        email_msg.attach(MIMEText(message, 'plain'))

        try:
            for file_name in file_name_list:
                df = pd.read_excel(os.getcwd() + f'\\sheets\\tmp\\{file_name}.xlsx')
                if len(df) > 0:
                    attachment = open(os.getcwd() + f'\\sheets\\tmp\\{file_name}.xlsx', 'rb')
                    part = MIMEBase('application', 'vnd.ms-excel')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment', filename=f'{file_name}.xlsx')           
                    email_msg.attach(part)
                    attachment.close()
        except:
            pass

        server.sendmail(email_msg['From'], all_recipients, email_msg.as_string())      
        server.quit()

class Tools(ABC):
    """
    Classe abstrata onde contém 
    todos os elementos, métodos e funções necessários para
    iteragir com webelements.
    """ 
    def __init__(self, webdriver, path, url,login_done=False, group_done=True):
        """
        Método construtor para iniciar o webdriver

        Args:
            webdriver: webdriver que será executado
            url (str, optional): url para acesso à adm. Defaults to ''.
        """
        self.webdriver = webdriver
        self.path = path
        self.webdriver.maximize_window()        
        self.url = url 
        self.login_done = login_done
        self.group_done = group_done
        try:
            os.mkdir(self.path + '\\tmp')
        except:
            pass
        self.open_url()     
        self.check_and_create_sheets() 
             
    ### GERAL ###
    
    def wait_(self, t=60):
        return WebDriverWait(self.webdriver, t)
        
    def wait_element(self, locator, t=60, el_type='presence'):        
        if el_type == 'presence':
            return self.wait_(t).until(EC.presence_of_element_located(locator))
        elif el_type == 'clickable':
            return self.wait_(t).until(EC.element_to_be_clickable(locator))
        elif el_type == 'visibility':
            return self.wait_(t).until(EC.visibility_of_element_located(locator))
    
    def find(self, locator, t=60, el_type='presence'):
        """
        Encontra o WebElement de acordo com seu locator

        Args:
            locator (tuple): tupla com as informações do WebElement

        Returns:
            WebElement: Elemento do DOM
        """
        self.wait_element(locator, t, el_type)
        return self.webdriver.find_element(*locator)
    
    def finds(self, locator, t=60, el_type='presence'):
        """
        Encontra os WebElements de acordo com seu locator

        Args:
            locator (tuple): tupla com as informações do WebElement

        Returns:
            WebElement (list): lista com os elementos encontrados.
        """
        self.wait_element(locator, t, el_type)
        return self.webdriver.find_elements(*locator)    
        
    def open_url(self):
        """
        Abre a url no navegador
        """
        self.webdriver.get(self.url)

    def click_in_element(self, locator, t=60, el_type='presence'):
        """
        Aguarda a presença do elemento por 30 segundos e clica no mesmo

        Args:
            locator (tuple): tupla com as informações do WebElement
        """
        self.find(locator, t, el_type).click()    
    
    def click_in_elements(self, locator, i, t=60, el_type='presence'):
        """
        Aguarda a presença dos elementos por 30 segundos e clica no elemento de índice i

        Args:
            locator (tuple): tupla com as informações do WebElement
            i (integer): índice da lista gerada, do elemento à ser clicado
        """
        elements = self.finds(locator, t, el_type)
        elements[i].click()

    def send_keys_to_element(self, locator, keys, t=60, el_type='presence'):
        """
        Aguarda a presença do elemento por 30 segundos e envia à ele a infomação de Keys

        Args:
            locator (tuple): tupla com as informações do WebElement
            keys (string): informação a ser enviada
        """
        self.find(locator, t, el_type).send_keys(keys)

    def send_keys_to_elements(self, locator, i, keys, t=60, el_type='presence'):
        """
        Aguarda a presença dos elementos, e envia ao elemento de índice i a infomação de Keys

        Args:
            locator (tuple): tupla com as informações do WebElement
            i (integer): índice da lista 
            keys (string): informação a ser enviada
        """
        elements = self.finds(locator, t, el_type)
        elements[i].send_keys(keys)
     
    def switch_to_frame(self, to):
        """
        Muda para o frame passado por parâmetro (to)

        Args:
            to (string): nome do frame que quer alterar
        """
        return self.webdriver.switch_to.frame(to)
    
    def switch_to_default_content(self):
        """
        Retorna para o conteúdo principal(padrao) do navegador
        """
        return self.webdriver.switch_to.default_content()

    def switch_to_parent_frame(self):
        """
        Retorna para o frame pai.
        ex:
            frame_a {
                frame_b{
                    frame_c{
                        ....
                    }
                }
            } 
            Estando em frame_c, switch_to_parent_frame, retornaria para o frame_b
        """
        return self.webdriver.switch_to.parent_frame()
                
    def check_and_create_sheets(self):
        """
        Percorre o arquivo e se nao encontrar o dataframe(tabela),
        cria um novo.
        
        Args:
            bot (modulo): modulo bot onde contem a classe PortoSeguroBot com o 
            método invocado create_sheets()
        """
        path_base = '\\'.join(self.path.split('\\')[:-1])
        try:
            os.mkdir(path_base + '\\sheets')
        except:
            pass
        try:
            if len(pd.read_excel(self.path + '\\Tickets_Uhuu.xlsx')) == 0:
                self.create_sheets() 
            else:
                pass
        except:
            self.create_sheets()  

    def create_sheets(self):
        """
        Cria os dataframes(tabelas) vazio,  apenas com as colunas. 
        """       
        df1 = pd.DataFrame(columns=COLS.get('event'))
        df1.to_excel(self.path + '\\Tickets_Uhuu.xlsx', index=False)
        

    def split_list(self, list, num):
        """
        Recebe uma lista e a divide em partes de acordo com num

        Args:
            list (list): lista a ser dividida
            num (integer): numero com quantidade de partes a ser dividida

        Returns:
            list: lista 
        """
        splited_list = []
        a = int(len(list) / num)
        len_l = len(list)
        for i in range(a):
            start = int(i*len_l/a)
            end = int((i+1)*len_l/a)
            splited_list.append(list[start:end])
        return splited_list
    
    def split_list2(self, list, num):
        """
        Recebe uma lista e a divide em partes de acordo com num.
        Se a divisao da lista pela qtd de elementos(num) nao for exata,
        se for maior em 1 elemento, entao esse elemento é retirado,
        se for mais do que 1, sera acrecentado zeros ate dar a qtd de elementos
        para uma divisao exata.

        Args:
            list (list): lista a ser dividida
            num (integer): numero com quantidade de partes a ser dividida

        Returns:
            list: lista
        """
        splited_list = []
        a = int(len(list) / num)
        b = int(len(list) % num)
        if b == 1:
            len_l = len(list[:-1])
        else:
            while b != 0:
                list.append('0')
                b = int(len(list) % num)
                len_l = len(list)
                a = int(len(list) / num)
            len_l = len(list)
        for i in range(a):
            start = int(i * len_l / a)
            #print("start ", start)
            end = int((i+1) * len_l/a)
            #print(end)
            splited_list.append(list[start:end])
            #print(len(splited_list))
        return splited_list

    
    def delete_sheets(self, end): 

        for file in os.listdir(self.path):
            try:
                if str(file).endswith(end):
                    os.remove(self.path + f'\\{file}')
                    time.sleep(1)
            except:
                pass
        path_gru = self.path + f'\\tmp\\grupos.xlsx'
        if os.path.exists(path_gru):
            os.remove(self.path + f'\\tmp\\grupos.xlsx')
       
    
    def send_email(self, worked, err=''):
        print_log('Enviando e-mails ...')        
        email = Email_sender(os.getenv('EMAIL_NEW'), os.getenv('PASSWORD_NEW')) 
        email.send_email('marcosmguedes1@gmail.com', 'Segue em anexo a coleta do Bot-Tickets_Uhuu', 'Tickets_Uhuu', cc_list=['fabinhoarao@gmail.com', 'cjaniel@gmail.com', 'contatoisavalentim@gmail.com'])    

    def exceptions(self, start, end, err):
        # time.sleep(60*2)
         
        if start <= end:
            print_log(f"ERRO - Tentando novamente")
            self.login_done = False
        else:
            print_log(f"ERRO GERAL") 
            self.send_email(False, err)
    
class Setup():
    def __init__(self, path) -> None:  
        
        self.s = Service(ChromeDriverManager().install())  #version="114.0.5735.90"
        self.opt = uc.ChromeOptions()

        prefs = {
            "download.default_directory" : path + '\\tmp',         
            "profile.content_settings.exceptions.automatic_downloads.*.setting": 1, 
            "safebrowsing.disable_download_protection": True,
            }      
        
        self.ua = UserAgent()
        self.ua_agent = self.ua.random
        print_log(self.ua_agent)
        self.opt.add_argument(f'--user-agent={self.ua_agent}')
        self.opt.add_experimental_option("prefs", prefs)
        self.opt.add_argument('--kiosk-printing')
        
