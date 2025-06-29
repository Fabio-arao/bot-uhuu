from configs_class.base import Base
from sqlalchemy import Column, String, DateTime,  BIGINT, Float, Text, Integer, Date



class TabelaResultadoAgo(Base):
    __tablename__ = 'turn2c_tabela_resultado_ago_intermediario'
    tra_id = Column(BIGINT, primary_key=True, autoincrement=True) 
    tra_categoria_lance = Column(String)
    tra_codigo = Column(String)
    tra_condicao = Column(String)
    tra_contemplacoes = Column(String)
    tra_data_assembleia = Column(String)
    tra_data_alt = Column(DateTime)
    tra_data_fim = Column(DateTime)
    tra_data_ini = Column(DateTime)
    tra_grupo_default = Column(String)
    tra_habilitado = Column(String)
    tra_id_administradora = Column(String)
    tra_instancia = Column(String)
    tra_lance_contemplados_grupo_projetado = Column(String)
    tra_lances_contemplados =  Column(String)
    tra_nome_administradora = Column(String)
    tra_percentual_lance_maximo = Column(Float)
    tra_percentual_lance_minimo = Column(Float)
    tra_qtd_assembleia = Column(String)
    tra_referencia = Column(String)
    tra_referencia_unica  =  Column(String)
    tra_status = Column(String)
    tra_user_id = Column(BIGINT)
    tra_conversao_lance_minimo = Column(Float)
    tra_conversao_lance_quartil = Column(Float)
    tra_ordem_ago = Column(Integer)
    tra_lance_contemplados_max_contemplado_grupo = Column(Float)
    tra_lance_contemplados_min_contemplado_grupo = Column(Float)
    tra_coeficiente_angular = Column(Float)
    
    
    def __repr__(self):
        return (f"TabelaResultadoAgo(tra_id={self.tra_id},"
                f"tra_categoria_lance={self.tra_categoria_lance},"
                f"tra_codigo={self.tra_codigo},"
                f"tra_condicao={self.tra_condicao},"
                f"tra_contemplacoes={self.tra_contemplacoes},"
                f"tra_data_assembleia={self.tra_data_assembleia},"
                f"tra_data_alt={self.tra_data_alt},"
                f"tra_data_fim={self.tra_data_fim},"
                f"tra_data_ini={self.tra_data_ini},"
                f"tra_grupo_default={self.tra_grupo_default},"
                f"tra_habilitado={self.tra_habilitado},"
                f"tra_id_administradora={self.tra_id_administradora},"
                f"tra_instancia={self.tra_instancia},"
                f"tra_lance_contemplados_grupo_projetado={self.tra_lance_contemplados_grupo_projetado},"
                f"tra_lances_contemplados={self.tra_lances_contemplados},"
                f"tra_nome_administradora={self.tra_nome_administradora},"
                f"tra_percentual_lance_maximo={self.tra_percentual_lance_maximo},"
                f"tra_percentual_lance_minimo={self.tra_percentual_lance_minimo},"
                f"tra_qtd_assembleia={self.tra_qtd_assembleia},"
                f"tra_referencia={self.tra_referencia},"
                f"tra_referencia_unica={self.tra_referencia_unica},"
                f"tra_status={self.tra_status},"
                f"tra_user_id={self.tra_user_id},"
                f"tra_conversao_lance_minimo={self.tra_conversao_lance_minimo},"
                f"tra_conversao_lance_quartil={self.tra_conversao_lance_quartil},"
                f"tra_ordem_ago={self.tra_ordem_ago},"
                f"tra_lance_contemplados_max_contemplado_grupo={self.tra_lance_contemplados_max_contemplado_grupo},"
                f"tra_lance_contemplados_min_contemplado_grupo={self.tra_lance_contemplados_min_contemplado_grupo},"
                f"tra_coeficiente_angular={self.tra_coeficiente_angular},"
               )