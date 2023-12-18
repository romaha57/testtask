from sqlalchemy import Column, Integer, String

from app.connect_db import Base


class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    main_category = Column(String)
    category = Column(String)
    type = Column(String)
    ceo = Column(String)

    def __repr__(self):
        return f'{self.main_category} - {self.category} - {self.type} - {self.ceo}'
