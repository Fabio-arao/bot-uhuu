from configs_class.connection import DBConnectionHandler
from configs_class.entities.sistema_log_banco import SistemaLogBanco

class LogBancoRepository:

    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(SistemaLogBanco).all()
            return data
        
    def insert(self,slb_id, slb_acao, slb_codigo, slb_data_ini, slb_data_alt, slb_data_fim, slb_habilitado,
               slb_identificador, slb_instancia, slb_ip, slb_query, slb_status, slb_tabela, slb_user_id
               ):
        with DBConnectionHandler() as db:
            
            data_insert = SistemaLogBanco(slb_id = slb_id,
                                          slb_acao = slb_acao,
                                          slb_codigo = slb_codigo,
                                          slb_data_ini = slb_data_ini,
                                          slb_data_alt = slb_data_alt,
                                          slb_data_fim = slb_data_fim,
                                          slb_habilitado = slb_habilitado,
                                          slb_identificador = slb_identificador,
                                          slb_instancia = slb_instancia,
                                          slb_ip = slb_ip,
                                          slb_query = slb_query,
                                          slb_status = slb_status,
                                          slb_tabela = slb_tabela,
                                          slb_user_id = slb_user_id
                                          )
            db.session.add(data_insert)
            db.session.commit()
        
    
  