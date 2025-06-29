import os, boto3, sqlalchemy, io, sys, uuid, math, json, requests
from types import SimpleNamespace
from bot.settings import *

class GetCode():
    def __init__(self, url):
        self.url = url
    
    def get_code(self):
        try:
            req = requests.get(self.url)
            if req.status_code == 200:
                print_log(f'STATUS POST: {req.status_code}')
            else:
                print_log(f'ERRO: Status {req.status_code} - {req.text}')
            return req.text
        except requests.exceptions.RequestException as e:
            print_log(f"ERRO: Falha na requisição POST: {str(e)}")
    
    def clear_emails(self, mode):
        try:
            data = {'tipo': mode}
            req = requests.post(self.url, json=data)
            if req.status_code == 200:
                print_log(f'STATUS POST: {req.status_code} clear emails')
            else:
                print_log(f'ERRO: Status {req.status_code} - {req.text}')
        except requests.exceptions.RequestException as e:
            print_log(f"ERRO: Falha na requisição POST: {str(e)}") 
        