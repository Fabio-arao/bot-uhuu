from configs_class.base import Base
from sqlalchemy import Column, String, DateTime,  BIGINT, Float, Text, Integer, Date, Integer, Time



class TabelaBotLog(Base):
    __tablename__ = 'sistema_bot_log'

    sbl_id = Column(BIGINT, primary_key=True, autoincrement=True)
    sbl_administradora = Column(String)
    sbl_codigo = Column(String)
    sbl_data_alt = Column(DateTime)
    sbl_data_fim = Column(DateTime)
    sbl_data_ini = Column(DateTime)
    sbl_habilitado = Column(String)
    sbl_qtd_credito = Column(Integer)
    sbl_qtd_grupos_ago = Column(Integer)
    sbl_qtd_preco = Column(Integer)
    sbl_status = Column(String)
    sbl_tempo_execussao = Column(Time)
    sbl_tentativas = Column(Integer)
    sbl_user_id = Column(String)
    

    def __repr__(self):
        return (f"TabelaBotLog(sbl_id={self.sbl_id},"
                f"sbl_administradora={self.sbl_administradora},"
                f"sbl_codigo={self.sbl_codigo},"
                f"sbl_data_alt={self.sbl_data_alt},"
                f"sbl_data_fim={self.sbl_data_fim},"
                f"sbl_data_ini={self.sbl_data_ini},"
                f"sbl_habilitado={self.sbl_habilitado},"
                f"sbl_qtd_credito={self.sbl_qtd_credito},"
                f"sbl_qtd_grupos_ago={self.sbl_qtd_grupos_ago},"
                f"sbl_qtd_preco={self.sbl_qtd_preco},"
                f"sbl_status={self.sbl_status},"
                f"sbl_tempo_execussao={self.sbl_tempo_execussao},"
                f"sbl_tentativas={self.sbl_tentativas},"
                f"sbl_user_id={self.sbl_user_id},"
               )
 
  
     