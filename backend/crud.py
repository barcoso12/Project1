from sqlalchemy.orm import Session
from app.models import Item

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

# Add more CRUD operations as needed
