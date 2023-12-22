from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import date


class Sessaolegislativa(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	legislatura:int= Field(default=None, foreign_key="legislatura.numero")
	numero:int
	tipo_sessao_legislativa:int= Field(default=None, foreign_key="tipo_sessao_legislativa.id")
	data_inicio:date
	data_fim:Optional[date]
	data_hora_criacao:Optional[dt]
	usuario_criacao:Optional[int]= Field(default=None, foreign_key="usuario.id")
	data_hora_atualizacao:Optional[dt]
	usuario_atualizacao:Optional[int]= Field(default=None, foreign_key="usuario.id")