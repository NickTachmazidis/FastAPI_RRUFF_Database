from pydantic import BaseModel

class MineralsBase(BaseModel):
    name: str
    description: str | None = None

class MineralCreate(MineralsBase):
    r_id: str | None = None
    locality: str | None = None
    source: str | None = None
    description: str | None = None
    owner: str | None = None
    status: str | None = None
    url: str | None = None
    ideal_chemistry: str | None = None
    measured_chemistry: str | None = None

class Mineral(MineralsBase):
    id: str
    name: str
    r_id: str | None = None
    locality: str | None = None
    source: str | None = None
    description: str | None = None
    owner: str | None = None
    status: str | None = None
    url: str | None = None
    ideal_chemistry: str | None = None
    measured_chemistry: str | None = None
    
    class Config:
        orm_mode = True