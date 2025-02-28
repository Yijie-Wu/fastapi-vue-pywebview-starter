from pydantic import BaseModel


class CarouselsBase(BaseModel):
    store_name: str
    desc: str
    show: bool


class CreateCarousels(CarouselsBase):
    pass


class UpdateCarousels(CarouselsBase):
    pass
