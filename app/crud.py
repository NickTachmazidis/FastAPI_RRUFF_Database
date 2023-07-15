from sqlalchemy.orm import Session

from . import models, schemas

def get_mineral(db: Session, mineral_id: int):
    return db.query(models.Minerals).filter(models.Minerals.id == mineral_id).first()

def get_mineral_by_name(db: Session, name: str):
    return db.query(models.Minerals).filter(models.Minerals.name == name).first()

def get_minerals(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Minerals).offset(skip).limit(limit).all()

def get_mineral_csv_path(db: Session, mineral_id: int):
    return db.query(models.Minerals).filter(models.Minerals.id == mineral_id).first()

def create_mineral(db: Session, mineral: schemas.MineralCreate):
    db_mineral = models.Minerals(name = mineral.name,
                                 description = mineral.description,
                                 r_id = mineral.r_id, 
                                 locality = mineral.locality, 
                                 source = mineral.source,  
                                 owner = mineral.owner, 
                                 status = mineral.status, 
                                 url = mineral.url, 
                                 ideal_chemistry = mineral.ideal_chemistry, 
                                 measured_chemistry = mineral.measured_chemistry)
    db.add(db_mineral)
    db.commit()
    db.refresh(db_mineral)
    return db_mineral