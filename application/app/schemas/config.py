from pydantic import BaseModel


class UpdateSchema(BaseModel):
    port: str
    baudrate: int
    bytesize:int
    parity:str
    stopbits:float | int
    timeout:float | int
    xonxoff:bool
    rtscts: bool
    dsrdtr: bool