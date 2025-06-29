from configs_class.connection import DBConnectionHandler
from configs_class.entities.turn2c_tabela_resultado_ago_intermediario import TabelaResultadoAgo


class TabelaAgoRepository:
    
    def insert(self, data):
        """
        Insere uma única linha na tabela TabelaCredito com os dados fornecidos.
        """
        with DBConnectionHandler() as db:
            db.session.add(data)
            db.session.commit()
            
    def insert_bulk(self, data_list):
        """
        Insere múltiplas linhas na tabela TabelaCredito a partir de uma lista de dicionários.
        """
        with DBConnectionHandler() as db:
            try:
                for data in data_list:
                    db.session.add(TabelaResultadoAgo(**data))
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
  