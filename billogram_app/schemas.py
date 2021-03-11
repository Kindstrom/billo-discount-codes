from typing import List, Optional

from pydantic import BaseModel


class DiscountCodeBase(BaseModel):
    code: str
    is_active: Optional[bool] = None
    brand_id: int

    class Config:
        orm_mode = True


class DiscountCode(DiscountCodeBase):
    id: int
