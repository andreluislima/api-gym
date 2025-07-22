
import datetime
from pydantic import UUID4, BaseModel

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True

class OutMixIn(BaseModel):
    id:UUID4
    created_at: datetime