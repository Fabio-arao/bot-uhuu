from configs_class.connection import DBConnectionHandler
from configs_class.entities.sistema_bot_log import TabelaBotLog


class BotLogRepository:
        
    def insert(self, sbl_id, sbl_administradora, sbl_codigo, sbl_data_alt, sbl_data_fim,
                sbl_data_ini, sbl_habilitado, sbl_qtd_credito, sbl_qtd_grupos_ago, sbl_qtd_preco,
                sbl_status, sbl_tempo_execussao, sbl_tentativas, sbl_user_id
               ):
        with DBConnectionHandler() as db:
            
            data_insert = TabelaBotLog(sbl_id = sbl_id,
                                          sbl_administradora = sbl_administradora,
                                          sbl_codigo = sbl_codigo,
                                          sbl_data_alt = sbl_data_alt,
                                          sbl_data_fim = sbl_data_fim,
                                          sbl_data_ini = sbl_data_ini,
                                          sbl_habilitado = sbl_habilitado,
                                          sbl_qtd_credito = sbl_qtd_credito,
                                          sbl_qtd_grupos_ago = sbl_qtd_grupos_ago,
                                          sbl_qtd_preco = sbl_qtd_preco,
                                          sbl_status = sbl_status,
                                          sbl_tempo_execussao = sbl_tempo_execussao,
                                          sbl_tentativas = sbl_tentativas,
                                          sbl_user_id = sbl_user_id
                                          )
            db.session.add(data_insert)
            db.session.commit()