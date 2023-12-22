from typing import Optional
from sqlmodel import Field, SQLModel


class Documentoparlamentar(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	sessao_plenaria:int
	autor:str
	documento:str
	Ementa:str
	data_hora_criacao:Optional[dt]
	usuario_criacao:Optional[int]= Field(default=None, foreign_key="usuario.id")
	data_hora_atualizacao:Optional[dt]
	usuario_atualizacao:Optional[int]= Field(default=None, foreign_key="usuario.id")