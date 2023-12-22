from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import date


class Tramitacao(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	ordem:int
	cpdocid:int= Field(default=None, foreign_key="propositura.cpdocid")
	data_tramitacao:date
	tipo_tramitacao:Optional[int]= Field(default=None, foreign_key="tipotramitacao.id")
	texto_tramitacao:str
	data_hora_criacao:Optional[dt]
	usuario_criacao:Optional[int]= Field(default=None, foreign_key="usuario.id")
	data_hora_atualizacao:Optional[dt]
	usuario_atualizacao:Optional[int]= Field(default=None, foreign_key="usuario.id")