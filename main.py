import uvicorn
from fastapi import FastAPI

from format_answers import format_items_data
from services import DBManager

app = FastAPI(
    title='Тестовое задание'
)


@app.get('/get-items-data')
async def get_items_data(
        search: str = None
):
    records = DBManager.get_items_data()
    result = format_items_data(records)

    return result


if __name__ == '__main__':
    DBManager.create_tables()
    DBManager.insert_mock_data()
    uvicorn.run('main:app', reload=True)
