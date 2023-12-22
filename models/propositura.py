from typing import Optional
from sqlmodel import Field, SQLModel


class Propositura(SQLModel, table=True): # type: ignore
	cpdocid:int= Field(default=None, primary_key=True)
	ementa:str
	tipo:Optional[int]= Field(default=None, foreign_key="tipo_propositura.id")
	numero:int
	Ano_número:int
	protocolo:int
	ano_protocolo:int
	processo:int
	ano_processo:int
	data_insercao:Optional[dt]
	arquivo:Optional[int]= Field(default=None, foreign_key="arquivo.id")
	arquivar:Optional[bool]
	data_hora_criacao:Optional[dt]
	usuario_criacao:Optional[int]= Field(default=None, foreign_key="usuario.id")
	data_hora_atualizacao:Optional[dt]
	usuario_atualizacao:Optional[int]= Field(default=None, foreign_key="usuario.id")