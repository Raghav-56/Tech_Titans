from pydantic import BaseModel, constr


class Query(BaseModel):
    text: constr(min_length=1, max_length=1000)
