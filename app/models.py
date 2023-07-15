from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

class Minerals(Base):
    __tablename__ = 'mineral_data'

    id: Mapped[int] = mapped_column(primary_key=True)   # ID
    r_id: Mapped[Optional[str]]                         # RRUFFID
    name: Mapped[str]                                   # NAMES
    locality: Mapped[Optional[str]]                     # LOCALITY
    source: Mapped[Optional[str]]                       # SOURCE
    description: Mapped[Optional[str]]                  # DESCRIPTION
    owner: Mapped[Optional[str]]                        # OWNER
    status: Mapped[Optional[str]]                       # STATUS 
    url: Mapped[Optional[str]]                          # URL
    csv_path: Mapped[Optional[str]]                     # CSV_PATH
    ideal_chemistry: Mapped[Optional[str]]              # IDEAL CHEMISTRY
    measured_chemistry: Mapped[Optional[str]]           # MEASURED CHEMISTRY