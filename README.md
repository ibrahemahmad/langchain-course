# FastAPI CRUD Application

A well-structured FastAPI application with CRUD operations using JSON file storage.

## 🏗️ Project Structure

```
langchain-course/
├── app/                    # Main application package
│   ├── __init__.py
│   ├── main.py            # FastAPI app instance
│   ├── api/               # API routes
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── items.py   # Items CRUD endpoints
│   ├── models/            # Pydantic models
│   │   ├── __init__.py
│   │   └── item.py        # Item data models
│   ├── services/          # Business logic
│   │   ├── __init__.py
│   │   └── store.py       # JSON storage service
│   └── core/              # Core configuration
│       ├── __init__.py
│       └── config.py      # App settings
├── data/                  # Data storage
│   └── data.json         # JSON database file
├── tests/                 # Test files
│   └── __init__.py
├── main.py               # CLI entry point
├── pyproject.toml        # Project dependencies
└── README.md            # This file
```

## 🚀 Features

- ✅ **Structured Architecture** - Clean separation of concerns
- ✅ **RESTful API** with FastAPI
- ✅ **CRUD Operations** (Create, Read, Update, Delete)
- ✅ **JSON File Storage** - No database required
- ✅ **Data Validation** with Pydantic
- ✅ **Configuration Management** - Centralized settings
- ✅ **Interactive API Docs** (Swagger UI & ReDoc)
- ✅ **CLI Interface** for easy server management

## 🛠️ Installation

Install dependencies using uv (or pip):

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

## 🏃 Running the Server

### Basic Usage

```bash
# Start server on default port (8000)
python main.py

# Start server on custom port
python main.py --port 3000

# Start server with auto-reload (for development)
python main.py --reload

# Make server accessible from network
python main.py --host 0.0.0.0 --port 8000
```

### CLI Options

- `--host` - Host to bind the server to (default: 127.0.0.1)
- `--port` - Port to bind the server to (default: 8000)
- `--reload` - Enable auto-reload for development

## 📚 API Documentation

Once the server is running, access the interactive documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔌 API Endpoints

### Root & Health

- `GET /` - Welcome message
- `GET /health` - Health check

### Items CRUD

- `POST /items` - Create a new item
- `GET /items` - Get all items
- `GET /items/{item_id}` - Get a specific item
- `PUT /items/{item_id}` - Update an item
- `DELETE /items/{item_id}` - Delete a specific item
- `DELETE /items` - Delete all items

## 📝 API Usage Examples

### Create an Item

```bash
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop",
    "description": "MacBook Pro 16-inch",
    "price": 2499.99,
    "quantity": 5
  }'
```

### Get All Items

```bash
curl "http://localhost:8000/items"
```

### Get a Specific Item

```bash
curl "http://localhost:8000/items/{item_id}"
```

### Update an Item

```bash
curl -X PUT "http://localhost:8000/items/{item_id}" \
  -H "Content-Type: application/json" \
  -d '{
    "price": 2299.99,
    "quantity": 3
  }'
```

### Delete an Item

```bash
curl -X DELETE "http://localhost:8000/items/{item_id}"
```

### Delete All Items

```bash
curl -X DELETE "http://localhost:8000/items"
```

## 🗂️ Data Models

### ItemCreate

```json
{
  "name": "string",
  "description": "string (optional)",
  "price": 0.0,
  "quantity": 0
}
```

### ItemUpdate

All fields are optional:

```json
{
  "name": "string",
  "description": "string",
  "price": 0.0,
  "quantity": 0
}
```

### Item (Response)

```json
{
  "id": "uuid",
  "name": "string",
  "description": "string",
  "price": 0.0,
  "quantity": 0,
  "created_at": "2026-02-09T12:00:00",
  "updated_at": "2026-02-09T12:00:00"
}
```

## 🏛️ Architecture

### Layers

1. **API Layer** (`app/api/`) - HTTP endpoints and request/response handling
2. **Service Layer** (`app/services/`) - Business logic and data operations
3. **Model Layer** (`app/models/`) - Data validation and serialization
4. **Core Layer** (`app/core/`) - Configuration and shared utilities

### Design Principles

- **Separation of Concerns** - Each module has a single responsibility
- **Dependency Injection** - Services are injected where needed
- **Type Safety** - Pydantic models ensure data validation
- **Modularity** - Easy to extend with new features

## 💾 Data Storage

All data is stored in [data/data.json](data/data.json) in the following format:

```json
{
  "items": {
    "uuid-1": { /* item data */ },
    "uuid-2": { /* item data */ }
  }
}
```

## 🔧 Development

### Adding New Models

1. Create model in `app/models/`
2. Export from `app/models/__init__.py`

### Adding New Routes

1. Create route file in `app/api/routes/`
2. Define router with endpoints
3. Include router in `app/main.py`

### Adding New Services

1. Create service in `app/services/`
2. Export from `app/services/__init__.py`
3. Import in routes as needed

## 🧪 Testing

```bash
# Run tests (when implemented)
pytest

# Run with coverage
pytest --cov=app
```

## 🎯 Next Steps

- [ ] Add unit tests
- [ ] Add authentication and authorization
- [ ] Implement search and filtering
- [ ] Add pagination for large datasets
- [ ] Add data export/import functionality
- [ ] Implement caching
- [ ] Add logging and monitoring
- [ ] Add Docker support

## 📄 License

This project is part of the langchain-course repository.
