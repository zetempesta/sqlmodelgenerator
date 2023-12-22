from typing import Optional
from sqlmodel import Field, SQLModel


class Parametro(SQLModel, table=True): # type: ignore
	nome:str= Field(default=None, primary_key=True)
	valor:str
	data_hora_criacao:Optional[dt]
	usuario_criacao:Optional[int]= Field(default=None, foreign_key="usuario.id")
	data_hora_atualizacao:Optional[dt]
	usuario_atualizacao:Optional[int]= Field(default=None, foreign_key="usuario.id")