# generated by datamodel-codegen:
#   filename:  moderate.json

from __future__ import annotations

from pydantic import BaseModel, Extra


class ModerateParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    address: str
    state: str