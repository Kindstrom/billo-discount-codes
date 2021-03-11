from sqlalchemy.orm import Session
from . import models, schemas


def get_discount_code(
    db: Session,
    brand_id: int
):
    return db.query(models.DiscountCode).filter(
        models.DiscountCode.brand_id==brand_id
    ).first()

def create_discount_code(
    db: Session,
    code: str,
    brand_id: int
):
    db_discount_code = models.DiscountCode(
        code=code,
        is_active=True,
        brand_id=brand_id
    )
    db.add(db_discount_code)
    db.commit()
    db.refresh(db_discount_code)
    return db_discount_code