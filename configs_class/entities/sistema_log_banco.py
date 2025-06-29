from configs_class.base import Base
from sqlalchemy import Column, String, DateTime,  BIGINT, Float, Text, Integer, Date



class SistemaLogBanco(Base):
    __tablename__ = 'sistema_log_banco'

    slb_id = Column(BIGINT, primary_key=True, autoincrement=True) 
    slb_acao = Column(String) 
    slb_codigo = Column(String)
    slb_data_ini = Column(DateTime)
    slb_data_alt = Column(DateTime) 
    slb_data_fim = Column(DateTime)
    slb_habilitado = Column(String)
    slb_identificador = Column(String)
    slb_instancia = Column(String)
    slb_ip = Column(String)
    slb_query = Column(Text(length="long"))
    slb_status = Column(String)
    slb_tabela = Column(String)
    slb_user_id = Column(Integer)

    
    def __repr__(self):
        return (f"SistemaLogBanco(slb_id={self.slb_id},"
                f"slb_acao={self.slb_acao},"
                f"slb_codigo={self.slb_codigo},"
                f"slb_data_ini={self.slb_data_ini},"
                f"slb_data_alt={self.slb_data_alt},"
                f"slb_data_fim={self.slb_data_fim},"
                f"slb_habilitado={self.slb_habilitado},"
                f"slb_identificador={self.slb_identificador},"
                f"slb_instancia={self.slb_instancia},"
                f"slb_ip={self.slb_ip},"
                f"slb_query={self.slb_query},"
                f"slb_status={self.slb_status},"
                f"slb_tabela={self.slb_tabela},"
                f"slb_user_id={self.slb_user_id},"
               )