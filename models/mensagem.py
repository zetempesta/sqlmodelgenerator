from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import date


class Mensagem(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	numero:int
	ano:int
	tipo:int= Field(default=None, primary_key=True, foreign_key="tipo_propositura.id")
	data_protocolo:Optional[date]
	resumo:str
	do_edicao:Optional[int]
	do_data:Optional[date]
	extra_do:Optional[int]
	norma_gerada:Optional[str]
	data_leitura:Optional[date]
	propositura:Optional[int]= Field(default=None, foreign_key="propositura.cpdocid")
	data_hora_criacao:Optional[dt]
	usuario_criacao:Optional[int]= Field(default=None, foreign_key="usuario.id")
	data_hora_atualizacao:Optional[dt]
	usuario_atualizacao:Optional[int]= Field(default=None, foreign_key="usuario.id")