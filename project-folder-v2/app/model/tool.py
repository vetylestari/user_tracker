from pydantic import BaseModel

class ToolHashPasswordGenerator(BaseModel):
    password: str