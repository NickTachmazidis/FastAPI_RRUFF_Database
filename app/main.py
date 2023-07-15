from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import pandas as pd

from . import crud, schemas
from .database import SessionLocal

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def index():
    return {"msg":
    "Hello to this API! It contains information about minerals from RRUFF"}

@app.get("/minerals/", response_model=list[schemas.Mineral])
def read_minerals(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    minerals = crud.get_minerals(db, skip=skip, limit=limit)
    return minerals

@app.post("/minerals/", response_model=schemas.Mineral, status_code=201)
def create_mineral(mineral: schemas.MineralCreate, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral_by_name(db, name=mineral.name)
    if db_mineral:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_mineral(db=db, mineral=mineral)

@app.get("/minerals/{mineral_id}", response_model=schemas.Mineral)
def read_mineral(mineral_id: int, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral(db, mineral_id=mineral_id)
    if db_mineral is None:
        raise HTTPException(status_code=404, detail="Mineral not found")
    return db_mineral

@app.delete("/minerals/{mineral_id}", response_model=schemas.Mineral)
def delete_mineral(mineral_id: int, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral(db, mineral_id=mineral_id)
    if not db_mineral:
        raise HTTPException(status_code=404, detail="Mineral not found")
    db.delete(db_mineral)
    db.commit()
    raise HTTPException(status_code=200, detail="Mineral deleted")

@app.get("/minerals/{mineral_id}/status")
def read_mineral_status(mineral_id: int, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral(db, mineral_id=mineral_id)
    if db_mineral is None:
        return HTTPException(status_code=404, detail="Mineral not found")
    return db_mineral.status

@app.get("/minerals/{mineral_id}/locality")
def read_mineral_locality(mineral_id: int, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral(db, mineral_id=mineral_id)
    if db_mineral is None:
        return HTTPException(status_code=404, detail="Mineral not found")
    return db_mineral.locality

@app.get("/minerals/{mineral_id}/source")
def read_mineral_source(mineral_id: int, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral(db, mineral_id=mineral_id)
    if db_mineral is None:
        return HTTPException(status_code=404, detail="Mineral not found")
    return db_mineral.source

@app.get("/minerals/{mineral_id}/description")
def read_mineral_description(mineral_id: int, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral(db, mineral_id=mineral_id)
    if db_mineral is None:
        return HTTPException(status_code=404, detail="Mineral not found")
    return db_mineral.description

@app.get("/minerals/{mineral_id}/owner")
def read_mineral_owner(mineral_id: int, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral(db, mineral_id=mineral_id)
    if db_mineral is None:
        return HTTPException(status_code=404, detail="Mineral not found")
    return db_mineral.owner

@app.get("/minerals/{mineral_id}/r_id")
def read_mineral_r_id(mineral_id: int, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral(db, mineral_id=mineral_id)
    if db_mineral is None:
        return HTTPException(status_code=404, detail="Mineral not found")
    return db_mineral.r_id 

@app.get("/minerals/{mineral_id}/url", response_class=HTMLResponse)
def read_mineral_url(mineral_id: int, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral(db, mineral_id=mineral_id)
    if db_mineral is None:
        return HTTPException(status_code=404, detail="Mineral not found")
    return f"""
    <p>Click to this <a href="http://{db_mineral.url}">link</a> to redirect to rruff</p>
    """

@app.get("/minerals/{mineral_id}/path")
def read_mineral_csv_path(mineral_id: int, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral_csv_path(db, mineral_id=mineral_id)
    if db_mineral is None:
        return HTTPException(status_code=404, detail="Mineral not found")
    return db_mineral.csv_path

@app.get("/minerals/{mineral_id}/path/data")
def read_mineral_csv_path_data(mineral_id: int, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral_csv_path(db, mineral_id=mineral_id)
    if db_mineral is None:
        return HTTPException(status_code=404, detail="Mineral not found")
    df = pd.read_csv(db_mineral.csv_path)
    x = df['x'].to_list()
    y = df['y'].to_list()
    return {'x': x, 'y': y}

@app.get("/minerals/{mineral_id}/chemistry")
def read_mineral_ideal_chemistry(mineral_id: int, db: Session = Depends(get_db)):
    db_mineral = crud.get_mineral(db, mineral_id=mineral_id)
    if db_mineral is None:
        return HTTPException(status_code=404, detail="Mineral not found")
    return {"ideal_chemistry": db_mineral.ideal_chemistry, 
            "measured_chemistry": db_mineral.measured_chemistry}