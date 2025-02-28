from pydantic import BaseModel


class SearchSchema(BaseModel):
    search_by: str
    q: str
