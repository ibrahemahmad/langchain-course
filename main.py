"""Main CLI entry point for the FastAPI application."""

import argparse
import sys

import uvicorn


def run_server(host: str = "127.0.0.1", port: int = 8000, reload: bool = False):
    """Run the FastAPI server."""
    print(f"🚀 Starting FastAPI server at http://{host}:{port}")
    print(f"📚 API documentation available at http://{host}:{port}/docs")
    print(f"📖 Alternative docs at http://{host}:{port}/redoc")
    
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="FastAPI CRUD Application",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Start server on default port 8000
  python main.py --port 3000        # Start server on port 3000
  python main.py --reload           # Start server with auto-reload
  python main.py --host 0.0.0.0     # Start server accessible from network
        """
    )
    
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host to bind the server to (default: 127.0.0.1)"
    )
    
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind the server to (default: 8000)"
    )
    
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload for development"
    )
    
    args = parser.parse_args()
    
    try:
        run_server(host=args.host, port=args.port, reload=args.reload)
    except KeyboardInterrupt:
        print("\n👋 Shutting down server...")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
