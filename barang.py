from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Stock(str, Enum):
    ada = "ada"
    tidak = "tidak"

class Kondisi(str, Enum):
    rusak = "rusak"
    lama = "lama"
    baru = "baru"

class Barang(BaseModel):
    id: Optional[UUID] = uuid4()
    nama_barang: str
    harga_barang: int
    stock: Stock
    kondisi: List[Kondisi]

class BarangUpdateRequest(BaseModel):
    nama_barang: Optional[str]
    harga_barang: Optional[str]
    kondisi: Optional[List[Kondisi]]