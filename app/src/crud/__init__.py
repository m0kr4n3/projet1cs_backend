from .crud_item import item
from .crud_user import user
from .crud_lieu import lieu
from .crud_categorie import categorie
from .crud_theme import theme
from .crud_rating import rating


# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)