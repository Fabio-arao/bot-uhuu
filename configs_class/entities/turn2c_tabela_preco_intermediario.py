from configs_class.base import Base
from sqlalchemy import Column, String, DateTime,  BIGINT, Float, Text, Integer, Date



class TabelaPreco(Base):
    __tablename__ = 'turn2c_tabela_preco_intermediario'

    tpr_id = Column(BIGINT, primary_key=True, autoincrement=True) 
    tpr_assembleia_restantes_default = Column(String)
    tpr_codigo = Column(String)
    tpr_data_alt = Column(DateTime)
    tpr_data_fim = Column(DateTime)
    tpr_data_ini = Column(DateTime)
    tpr_dia_vencimento_default = Column(String)
    tpr_fundo_reserva_tot_default = Column(String)
    tpr_grupo_default = Column(String)
    tpr_habilitado = Column(String)
    tpr_id_administradora = Column(String)
    tpr_instancia = Column(String)
    tpr_nome_administradora = Column(String)
    tpr_referencia = Column(String)
    tpr_seguro_vida_grupo_default = Column(Float)
    tpr_status = Column(String)
    tpr_taxa_adm_plano_tot_default = Column(String)
    tpr_user_id = Column(BIGINT)
    tpr_valor_max_bem_default = Column(Float)
    tpr_valor_min_bem_default = Column(Float)
    tpr_adesao  = Column(Float)
    tpr_parcelamento_adesao = Column(Float)
    tpr_redutor = Column(Float)
    tpr_indexador = Column(String)
    tpr_administradora_plano_codigo = Column(String)
    tpr_segmento = Column(String)
    
    
    def __repr__(self):
        return (f"TabelaPreco(tpr_id={self.tpr_id},"
                f"tpr_assembleia_restantes_default={self.tpr_assembleia_restantes_default},"
                f"tpr_codigo={self.tpr_codigo},"
                f"tpr_data_alt={self.tpr_data_alt},"
                f"tpr_data_fim={self.tpr_data_fim},"
                f"tpr_data_ini={self.tpr_data_ini},"
                f"tpr_dia_vencimento_default={self.tpr_dia_vencimento_default},"
                f"tpr_fundo_reserva_tot_default={self.tpr_fundo_reserva_tot_default},"
                f"tpr_grupo_default={self.tpr_grupo_default},"
                f"tpr_habilitado={self.tpr_habilitado},"
                f"tpr_id_administradora={self.tpr_id_administradora},"
                f"tpr_instancia={self.tpr_instancia},"
                f"tpr_nome_administradora={self.tpr_nome_administradora},"
                f"tpr_referencia={self.tpr_referencia},"
                f"tpr_seguro_vida_grupo_default={self.tpr_seguro_vida_grupo_default},"
                f"tpr_status={self.tpr_status},"
                f"tpr_taxa_adm_plano_tot_default={self.tpr_taxa_adm_plano_tot_default},"
                f"tpr_user_id={self.tpr_user_id},"
                f"tpr_valor_max_bem_default={self.tpr_valor_max_bem_default},"
                f"tpr_valor_min_bem_default={self.tpr_valor_min_bem_default},"
                f"tpr_adesao={self.tpr_adesao},"
                f"tpr_parcelamento_adesao={self.tpr_parcelamento_adesao},"
                f"tpr_redutor={self.tpr_redutor},"
                f"tpr_indexador={self.tpr_indexador},"
                f"tpr_administradora_plano_codigo={self.tpr_administradora_plano_codigo},"
                f"tpr_segmento={self.tpr_segmento}"
               )