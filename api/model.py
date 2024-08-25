from pydantic import BaseModel


class MyModel(BaseModel):
    msg: str = ""
