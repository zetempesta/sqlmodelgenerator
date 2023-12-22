from typing import Optional
from sqlmodel import Field, SQLModel


class Propositurasessaoplenaria(SQLModel, table=True): # type: ignore
	propositura_cpdocid:int= Field(default=None, foreign_key="propositura.cpdocid")
	sessao_plenaria_id:int= Field(default=None, foreign_key="sessao_plenaria.id")
	data_hora_criacao:Optional[dt]
	usuario_criacao:Optional[int]= Field(default=None, foreign_key="usuario.id")
	data_hora_atualizacao:Optional[dt]
	usuario_atualizacao:Optional[int]= Field(default=None, foreign_key="usuario.id")