from bot.settings import *
from bot.locators import *
from tools.tools import Tools
from tools.decorators import track_processed_items, pages
from selenium.webdriver.common.by import By
import time, re, uuid
from sqlalchemy import text
from difflib import SequenceMatcher
import pandas as pd
from typing import Optional
from selenium.webdriver.support.ui import Select



class Ticket360(Tools):    
    
    def make_collect(self, step): 
           
        match step:
            case 1:  
                base = os.path.join(self.path + '\\tmp\\Tickets_Uhuu.xlsx')
                self.titulos_existentes = set(t.strip().lower() for t in pd.read_excel(base)['Titulo'].dropna())
                self.collect_tickts(URLS)
                self.concat_sheets()
                
    
    def clear_text(self, texto):
        if isinstance(texto, str):
            texto = texto.strip("[]")                # Remove colchetes
            texto = texto.replace("'", "")           # Remove aspas simples
            texto = re.sub(r'QTD(?:\s\d){1,10}', '', texto)  # Remove "QTD" seguido de até 6 dígitos separados por espaço
            texto = re.sub(r'\s+', ' ', texto)       # Remove espaços extras
            texto = texto.strip()                    # Remove espaços no início/fim
        return texto

    def concat_sheets(self):
        df_1 = pd.read_excel(self.path + '\\Tickets_Uhuu.xlsx')
        df_2= pd.read_excel(self.path + '\\tmp\\Tickets_Uhuu.xlsx')
       
        df_concat = pd.concat([df_1, df_2], ignore_index=True, axis=0)
        df_concat['Valor_do_ingresso'] = df_concat['Valor_do_ingresso'].apply(self.clear_text)
        df_concat = df_concat.drop_duplicates()
        df_concat.to_excel(self.path + '\\tmp\\Tickets_Uhuu.xlsx', index=False)
        os.remove(self.path + '\\Tickets_Uhuu.xlsx')
                
    def loading(self):
        while True:
            try:
                if self.find((By.XPATH, "//*[contains(text(), 'Descrição do evento')]"), t=1):
                    print("Pagina carregada!")
                    break
            except:
                print("Loading ..")
                time.sleep(1)
                try:
                    host_element = self.webdriver.find_element(By.CSS_SELECTOR, 'app-page[page="event"]')
                    shadow_root = self.webdriver.execute_script("return arguments[0].shadowRoot", host_element)
                    if shadow_root.find_element(By.CSS_SELECTOR, "iron-pages"):
                        print("Pagina carregada no 2!")
                        break
                except:
                    print("Loading 2 ..")
                    time.sleep(1)

    def click_in_cookies(self):
        host = self.webdriver.find_element(By.ID, 'cmpwrapper')
        shadow_root = self.webdriver.execute_script('return arguments[0].shadowRoot', host)
        botao_aceitar = shadow_root.find_element(By.CSS_SELECTOR, "a.cmpboxbtn.cmpboxbtnyes")
        botao_aceitar.click()
    
    def click_in_option(self):
        try:
            self.find((By.CSS_SELECTOR, 'div[id="promoComponent"] form button'), t=2).click()
        except:
            self.find((By.CSS_SELECTOR, 'i[class="icon icon-expand-more margin-left-auto"]'), t=1).click()  

    def select_events_in_events(self):
        try:
            divs = self.finds((By.CSS_SELECTOR, 'div[id="tickets"] .listing-item-wrapper-inside-card'), t=2)
        except:
            divs = self.finds((By.CSS_SELECTOR, 'article[class*="listing listing-container"]'), t=2) 
        return divs

    def alert(self):
        try:
            iframes = self.webdriver.find_elements(By.TAG_NAME, "iframe")
            self.webdriver.switch_to.frame(iframes[1])
            self.find((By.XPATH, "//button[contains(@class, 'btnClose')]"),t=1).click()
            self.switch_to_default_content()
        except:
            pass
    
    def position_line_click(self, i):
        scrollable = self.webdriver.find_element(By.CSS_SELECTOR, 'div[class="item card-evento"]')
        self.webdriver.execute_script("""
            const rect = arguments[0].getBoundingClientRect();
            const container = arguments[1];
            const offset = rect.top + container.scrollTop - (container.clientHeight / 2) + (rect.height / 2);
            container.scrollTop = offset;
        """, i, scrollable)
    
    @track_processed_items
    def collect_tickts(self, key):
        nome_categoria, url = list(key.items())[0]
        print_log(f'Coletando {nome_categoria}')
        arquivo = os.path.join(self.path, f'{nome_categoria}.xlsx')
        try:
            self.find((By.CSS_SELECTOR, 'button[id="cookie-banner-accept"]'),t=4).click()
        except:
            self.alert()
        if not os.path.exists(arquivo):
            df = pd.DataFrame(columns=COLS.get('event'))
            df.to_excel(arquivo, index=False)
            
        df_tickets = pd.read_excel(arquivo)
        self.webdriver.execute_script("window.scrollBy(0, 300)")
        time.sleep(20)
        self.webdriver.execute_script("window.scrollBy(0, 300)")
        time.sleep(10)
        self.alert()
        pagina_fin = self.find((By.CSS_SELECTOR, 'ul[class="pagination"]')).text.split("\n")[-1]

        for page in range(1, int(pagina_fin)+1):
            print(f'Estamos na pagina: {page} de {pagina_fin}')
            full_url = str(list(key.items())[0][1]) + str(page)
            self.webdriver.get(full_url)
            events = self.finds((By.CSS_SELECTOR, 'div[class="item card-evento"]'))
            time.sleep(2)
            for event in range(len(events)):
                # if event <4:
                #     continue
                title = events[event].find_element(By.CSS_SELECTOR, "div[class*='infoCardMobile ']").text.split("\n")[-1]
                evento_id = f"{full_url} / {event}"
                print(title)
                if self.evento_ja_coletado(title, self.titulos_existentes):
                    print(f"{title} Já foi coletado!!")
                    continue
                if evento_id not in pages:
                    try:
                        element = events[event]
                        self.webdriver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
                        time.sleep(0.5)  # tempo para garantir o scroll antes do clique
                        image = element.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
                        element.click()
                        # events[event].click()
                        descricao = self.find((By.CSS_SELECTOR, 'div[class*="tabs-content-item "]')).text.replace("\n", " ")
                        time.sleep(1)
                        evento_data = self._coletar_evento_one(descricao, image)
                        if evento_data:
                            df_tickets.loc[len(df_tickets)] = evento_data
                            df_tickets.to_excel(arquivo, index=False)
                        self.force_return()
                        events = self.finds((By.CSS_SELECTOR, 'div[class="item card-evento"]'))
                    except Exception as e:
                        print_log(f"Erro ao coletar os dados do Evento {event + 1}: {e}")
                    pages.add(evento_id)
                self.webdriver.get(full_url)
                time.sleep(1)
                events = self.finds((By.CSS_SELECTOR, 'div[class="item card-evento"]'))

    def normalizar_texto(self, texto):
        texto = texto.lower()
        texto = re.sub(r'[^a-z0-9\s]', '', texto)  # remove símbolos como |, -, etc
        texto = re.sub(r'\s+', ' ', texto).strip()  # normaliza espaços
        return texto

    def remover_stopwords(self, texto):
        stopwords = {'de', 'do', 'da', 'e', 'em', 'para', 'com', 'por', 'um', 'uma', 'são', 'no', 'na', 'consta', 'a', 'o'}
        return ' '.join([palavra for palavra in texto.split() if palavra not in stopwords])

    def evento_ja_coletado(self, titulo_novo, titulos_existentes):
        titulo_novo_norm = self.normalizar_texto(titulo_novo)
        titulo_novo_limpo = self.remover_stopwords(titulo_novo_norm)    

        for titulo_existente in titulos_existentes:
            titulo_existente_norm = self.normalizar_texto(titulo_existente)
            titulo_existente_limpo = self.remover_stopwords(titulo_existente_norm)

            # Comparação direta
            if titulo_existente_limpo == titulo_novo_limpo:
                return True

            # Comparação por similaridade (ajuste o threshold conforme necessário)
            similarity = SequenceMatcher(None, titulo_novo_limpo, titulo_existente_limpo).ratio()
            if similarity > 0.85:
                return True

        return False


    def force_return(self):
        while True:
            try:
                events = self.finds((By.CSS_SELECTOR, 'div[class="item card-evento"]'), t=1)
                break
            except:
                self.webdriver.execute_script("window.history.back()")
        return

    def _coletar_evento_one(self, descricao: str, image:str) -> Optional[list[str]]:
        """
        Coleta os dados de um evento aberto.
        """
        id_event = uuid.uuid4().hex
        
        try:
            cla = re.search(r'Classificação:\s*(.......)', descricao) 
            classific = cla.group(1)
        except:
            classific = ''

        descricao = descricao.split("Classificação")[0]
        try:
            details = self.finds((By.CSS_SELECTOR, 'div[class*="event-details"] p'))
            try:
                valores = self.colect_values_tickets()
            except:
                try:
                    valores = details[1].text.replace("\n", " ")
                except:
                    valores = details[1].text.replace("\n", " ")
                
            titulo = self.find((By.TAG_NAME, 'h1')).text
            data = details[0].text.replace("\n", " ")
            local = details[2].text.replace("\n", " ") 
            self._log_evento(id_event, titulo, descricao, data, local, valores, self.webdriver.current_url, image, classific)
            return [id_event, titulo, descricao, data, local, valores, self.webdriver.current_url, image, classific]

        except:
            return self._coletar_evento_two(descricao, image, id_event, classific)
        
    def colect_values_tickets(self):
        valores = list()
        cheks = self.finds((By.CSS_SELECTOR, 'label[class="m-radio"]'), t=3)
        for i in cheks:
            i.click()
            time.sleep(1)
            val = self.find((By.CSS_SELECTOR, 'div[class="col-12 col-lg-12 col-sm-12 col-md-12 col-lx-12"]'), t=5).text.replace("\n"," ").replace("+ Taxas QTD 0 1 2 3 4 0", " ").strip("ESCOLHER INGRESSO")
            valores.append(val)
        return valores
    
    def _coletar_evento_two(self, descricao: str, image:str, id_event:str, classific:str) -> Optional[list[str]]:
        """
        Coleta os dados de um evento aberto.
        """
        try:
            valores = self.find((By.CSS_SELECTOR, 'div[class="event-list-item-wrapper pc-list-item-space clearfix js-product-type"]'), t=2).text.replace("\n", " ")
            titulo = self.finds((By.CSS_SELECTOR, 'h1[class="stage-headline"]'))[0].text
            data = self.finds((By.TAG_NAME, 'time'))[0].text
            local = self.find((By.CSS_SELECTOR, 'span[data-qa="event-venue"]')).text

            self._log_evento(id_event, titulo, descricao, data, local, valores, self.webdriver.current_url, image, classific)
            return [id_event, titulo, descricao, data, local, valores, self.webdriver.current_url, image, classific]

        except:
            return self._coletar_evento_tree(descricao, image, id_event, classific)
    
    def _coletar_evento_tree(self, descricao: str, image:str, id_event:str, classific:str) -> Optional[list[str]]:
        """
        Coleta os dados de um evento aberto.
        """
        try:
            titulo = self.finds((By.CSS_SELECTOR, 'h1[class="stage-headline"]'), t=5)[0].text
            data = self.finds((By.TAG_NAME, 'time'))[0].text
            local = self.finds((By.CSS_SELECTOR, 'div[class*="stage-list-item js-scroll u-position-relative"]'))[0].text  
            ingre = self.find((By.CSS_SELECTOR, 'div[class*="card-section promotion-card js-promo-selection"]'), t=6)
            vend_geral = ingre.find_element(By.NAME, 'promo_id')
            try:
                Select(vend_geral).select_by_visible_text('1 - VENDA GERAL')
            except:
                Select(vend_geral).select_by_visible_text('VENDA GERAL')
            valores = self.find((By.CSS_SELECTOR, 'div[class="event-list-item-wrapper pc-list-item-space clearfix js-product-type"]'), t=2).text.replace("\n", " ")    
            
            self._log_evento(id_event, titulo, descricao, data, local, valores, self.webdriver.current_url, image, classific)
            return [id_event, titulo, descricao, data, local, valores, self.webdriver.current_url, image, classific]
        except:
            return self._coletar_evento_four(descricao, image, id_event, classific)


    def _coletar_evento_four(self, descricao: str, image:str, id_event:str, classific:str) -> Optional[list[str]]:
        """
        Coleta os dados de um evento aberto.
        """
        try:
            val = self.finds((By.CSS_SELECTOR, 'ul[class="styled-dropdown-list js-dd-elements"]'),t=5)
            valores = val[0].text.replace("\n", " ").replace("0 ", "0 / ")
            titulo = self.finds((By.CSS_SELECTOR, 'h1[class="stage-headline"]'))[0].text
            data = self.finds((By.TAG_NAME, 'time'))[0].text
            local = self.finds((By.CSS_SELECTOR, 'div[class*="stage-list-item js-scroll u-position-relative"]'))[0].text  
            
            self._log_evento(id_event, titulo, descricao, data, local, valores, self.webdriver.current_url, image, classific)
            return [id_event, titulo, descricao, data, local, valores, self.webdriver.current_url, image, classific]
        
        except:
            raise Exception("Erro ao coletar os dados do evento.")



    def _log_evento(self, id_event: str, titulo: str, descricao: str, data: str, local: str, preco: str, url: str, image: str, classific: str) -> None:
        """
        Prints the event data to the console.

        Args:
            titulo (str): Event title.
            descricao (str): Event description.
            data (str): Event date.
            local (str): Event location.
            preco (str): Ticket price.
        """
        print_log("*********************************************************")
        print_log(f"Title: {id_event}")
        print_log(f"Title: {titulo}")
        print_log(f"Description: {descricao}")
        print_log(f"Date: {data}")
        print_log(f"Location: {local}")
        print_log(f"Ticket price: {preco}")
        print_log(f"Link: {url}")
        print_log(f"Image: {image}")
        print_log(f"Classificação: {classific}")
        print_log("*********************************************************")