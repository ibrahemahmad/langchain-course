"""JSON file storage for items."""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from app.models import Item, ItemCreate, ItemUpdate


class JSONStore:
    """Simple JSON file storage for items."""
    
    def __init__(self, file_path: str = "data/data.json"):
        """Initialize the store with a file path."""
        self.file_path = Path(file_path)
        self._ensure_file_exists()
    
    def _ensure_file_exists(self) -> None:
        """Create the data file if it doesn't exist."""
        if not self.file_path.exists():
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            self.file_path.write_text(json.dumps({"items": {}}, indent=2))
    
    def _read_data(self) -> Dict:
        """Read data from the JSON file."""
        try:
            return json.loads(self.file_path.read_text())
        except json.JSONDecodeError:
            # If file is corrupted, reset it
            self._ensure_file_exists()
            return {"items": {}}
    
    def _write_data(self, data: Dict) -> None:
        """Write data to the JSON file."""
        self.file_path.write_text(json.dumps(data, indent=2, default=str))
    
    def create_item(self, item_data: ItemCreate) -> Item:
        """Create a new item."""
        data = self._read_data()
        
        # Generate unique ID
        item_id = str(uuid.uuid4())
        now = datetime.now()
        
        # Create item
        item = Item(
            id=item_id,
            name=item_data.name,
            description=item_data.description,
            price=item_data.price,
            quantity=item_data.quantity,
            created_at=now,
            updated_at=now
        )
        
        # Store item
        data["items"][item_id] = item.model_dump(mode="json")
        self._write_data(data)
        
        return item
    
    def get_item(self, item_id: str) -> Optional[Item]:
        """Get an item by ID."""
        data = self._read_data()
        item_data = data["items"].get(item_id)
        
        if item_data:
            return Item(**item_data)
        return None
    
    def get_all_items(self) -> List[Item]:
        """Get all items."""
        data = self._read_data()
        return [Item(**item_data) for item_data in data["items"].values()]
    
    def update_item(self, item_id: str, item_update: ItemUpdate) -> Optional[Item]:
        """Update an item."""
        data = self._read_data()
        
        if item_id not in data["items"]:
            return None
        
        # Get existing item
        item_data = data["items"][item_id]
        
        # Update only provided fields
        update_data = item_update.model_dump(exclude_unset=True)
        item_data.update(update_data)
        item_data["updated_at"] = datetime.now().isoformat()
        
        # Save updated item
        data["items"][item_id] = item_data
        self._write_data(data)
        
        return Item(**item_data)
    
    def delete_item(self, item_id: str) -> bool:
        """Delete an item."""
        data = self._read_data()
        
        if item_id in data["items"]:
            del data["items"][item_id]
            self._write_data(data)
            return True
        return False
    
    def clear_all(self) -> None:
        """Clear all items."""
        self._write_data({"items": {}})


# Global store instance
store = JSONStore()
