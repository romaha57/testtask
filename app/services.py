from typing import Type

from app.mock_data import mock_records
from app.connect_db import engine
from sqlalchemy.orm import Session
from app.connect_db import Base


from app.models import Record


class Singleton(type):
    """Синглтон для БД"""

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class DBManager(metaclass=Singleton):

    @classmethod
    def create_tables(cls):
        """Удаляем и создаем таблицы заново"""

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @classmethod
    def insert_mock_data(cls):
        """Добавляем тестовые данные(чтобы получилась такая же таблица как в задании)"""

        with Session(engine, expire_on_commit=False) as session:
            records = []
            for data in mock_records:
                r = Record(
                    main_category=data[0],
                    category=data[1],
                    type=data[2],
                    ceo=data[3],
                )

                records.append(r)

            session.add_all(records)
            session.commit()

    @classmethod
    def get_items_data(cls, search: str = None) -> list[Type[Record]]:
        """Здесь мы получаем данные как в задании"""

        with Session(engine, expire_on_commit=False) as session:
            # имитируем получение таких же данных как в задании в исходной таблице
            records = session.query(Record).all()
            return records

            # А если брать запрос из задания

            # stmt = text("""
            # with
            #     cte1 as (
            #     select cd.category_name as level1, cd2.category_name as level2,
            #     cd3.category_name as level3, cd3.category_seo as seo,
            #     if(cd3.filter_name=cd2.filter_name, cd3.filter_name, cd2.filter_name) as filter_name
            #     from categories_data cd
            #     left join categories_data cd2 on
            #     cd.category_id = cd2.parent_id  and cd2.date = today() and cd2.shop_id = 8 and (cd2.filter_name ilike :search or cd2.category_seo ilike :search or cd2.category_name ilike :search)
            #     left join categories_data cd3 on
            #     cd2.category_id = cd3.parent_id  and cd3.date = today() and cd3.shop_id = 8 and (cd3.filter_name ilike :search or cd3.category_seo ilike :search or cd3.category_name ilike :search)
            #     where cd.parent_id = '' and cd.date = today() and cd.shop_id = 8
            #     );
            #
            #     select * from cte1 where (level1 ilike :search or level2 ilike :search or level3 ilike :search or seo ilike :search or filter_name ilike :search)
            #     order by level1, level2, level3, seo, filter_name asc
            # """)

            # records = session.execute(stmt, search=search)
            # return records






