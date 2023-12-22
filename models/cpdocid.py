from typing import Optional
from sqlmodel import Field, SQLModel


class Cpdocid(SQLModel, table=True): # type: ignore
	cpdocid:int= Field(default=None, primary_key=True)
	tipo:Optional[int]= Field(default=None, foreign_key="tipo_propositura.id")
	data_hora_criacao:Optional[dt]
	usuario_criacao:Optional[int]= Field(default=None, foreign_key="usuario.id")
	data_hora_atualizacao:Optional[dt]
	usuario_atualizacao:Optional[int]= Field(default=None, foreign_key="usuario.id")