"""Items CRUD routes."""

from typing import List

from fastapi import APIRouter, HTTPException, Query, status

from app.models import Item, ItemCreate, ItemUpdate
from app.services import store

router = APIRouter(prefix="/items", tags=["Items"])


@router.post("", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """Create a new item."""
    try:
        new_item = store.create_item(item)
        return new_item
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create item: {str(e)}"
        )


@router.get("", response_model=List[Item])
async def get_all_items():
    """Get all items."""
    try:
        items = store.get_all_items()
        return items
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve items: {str(e)}"
        )


@router.get("/paginated", response_model=List[Item])
async def get_paginated_items(
    from_index: int = Query(1, ge=1, alias="from", description="Start index (1-based)"),
    to_index: int = Query(20, ge=1, alias="to", description="End index (inclusive)")
):
    """Get paginated items based on query parameters."""
    try:
        # Validate range
        if from_index > to_index:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"'from' ({from_index}) cannot be greater than 'to' ({to_index})"
            )
        
        # Get all items
        all_items = store.get_all_items()
        
        # Convert to 0-based index for slicing
        start_idx = from_index - 1
        end_idx = to_index
        
        # Return paginated subset
        paginated_items = all_items[start_idx:end_idx]
        
        return paginated_items
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve paginated items: {str(e)}"
        )


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: str):
    """Get a specific item by ID."""
    item = store.get_item(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    return item


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: str, item_update: ItemUpdate):
    """Update an item."""
    updated_item = store.update_item(item_id, item_update)
    if not updated_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    return updated_item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str):
    """Delete an item."""
    success = store.delete_item(item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    return None


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_items():
    """Delete all items."""
    try:
        store.clear_all()
        return None
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete all items: {str(e)}"
        )
