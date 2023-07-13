from fastapi import FastAPI, HTTPException
from uuid import UUID
from barang import Barang,Stock,Kondisi,BarangUpdateRequest
from typing import Optional, List

app = FastAPI()

db: List[Barang] = [
    Barang(
        id=UUID("9cc91c6f-9fe0-4099-b73a-8ff77a35e89a"),
        nama_barang="Mouse",
        harga_barang=20000,
        stock=Stock.ada,
        kondisi=[Kondisi.baru]
        ),
    Barang(
        id=UUID("6ff47efe-b54f-4e4f-980d-af294c607be5"),
        nama_barang="Keyboard",
        harga_barang=40000,
        stock=Stock.tidak,
        kondisi=[Kondisi.rusak]
        ),
]

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/api/v1/barang")
async def fetch_barang():
    return db;

@app.post("/api/v1/barang")
async def regist_barang(barang: Barang):
    db.append(barang)

@app.delete("/api/v1/barang/{barang_id}")
async def delete_barang(barang_id: UUID):
    for barang in db:
        if barang.id == barang_id:
            db.remove(barang)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id {barang_id} does not exists"
    )

@app.put("/api/v1/barang/{user_id}")
async def update_barang(barang_update: BarangUpdateRequest, barang_id: UUID ):
    for barang in db:
        if barang.id == barang_id:
            if barang_update.nama_barang is not None:
                barang.nama_barang = barang_update.nama_barang
            if barang_update.harga_barang is not None:
                barang.harga_barang = barang_update.harga_barang
            if barang_update.kondisi is not None:
                barang.kondisi = barang_update.kondisi
            return
    raise HTTPException(
        status_code=404,
        detail=f"user dengan id {barang_id} tidak ada"
    )