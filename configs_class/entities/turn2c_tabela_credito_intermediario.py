from configs_class.base import Base
from sqlalchemy import Column, String, DateTime,  BIGINT, Float, Text, Integer, Date



class TabelaCredito(Base):
    __tablename__ = 'turn2c_tabela_credito_intermediario'

    cre_id = Column(BIGINT, primary_key=True, autoincrement=True)
    cre_codigo = Column(String)
    cre_codigo_bem = Column(String)
    cre_credito = Column(String)
    cre_data_alt = Column(DateTime)
    cre_data_fim = Column(DateTime)
    cre_data_ini = Column(DateTime)
    cre_descricao_bem = Column(String)
    cre_grupo = Column(String)
    cre_habilitado = Column(String)
    cre_id_administradora = Column(String)
    cre_instancia = Column(String)
    cre_nome_administradora = Column(String)
    cre_referencia = Column(String)
    cre_status = Column(String)
    cre_user_id = Column(BIGINT)
    cre_valor_credito = Column(Float) 
    cre_valor_parcela = Column(String)
    cre_valor_parcela_maxima = Column(Float) 
    cre_valor_parcela_minima = Column(Float)
    cre_referencia_unica = Column(String)
   


    def __repr__(self):
        return (f"TabelaCredito(cre_id={self.cre_id},"
                f"cre_codigo={self.cre_codigo},"
                f"cre_codigo_bem={self.cre_codigo_bem},"
                f"cre_credito={self.cre_credito},"
                f"cre_data_alt={self.cre_data_alt},"
                f"cre_data_fim={self.cre_data_fim},"
                f"cre_data_ini={self.cre_data_ini},"
                f"cre_descricao_bem={self.cre_descricao_bem},"
                f"cre_grupo={self.cre_grupo},"
                f"cre_habilitado={self.cre_habilitado},"
                f"cre_id_administradora={self.cre_id_administradora},"
                f"cre_referencia={self.cre_referencia},"
                f"cre_status={self.cre_status},"
                f"cre_user_id={self.cre_user_id},"
                f"cre_valor_credito={self.cre_valor_credito},"
                f"cre_valor_parcela={self.cre_valor_parcela},"
                f"cre_valor_parcela_maxima={self.cre_valor_parcela_maxima},"
                f"cre_valor_parcela_minima={self.cre_valor_parcela_minima},"
                f"cre_referencia_unica={self.cre_referencia_unica},"
               )
 
  
     