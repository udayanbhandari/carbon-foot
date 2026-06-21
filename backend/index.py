import os
import sys

# Ensure backend directory is in sys.path when running from workspace root (e.g. on Vercel)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import app
