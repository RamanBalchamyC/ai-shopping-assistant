import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
app_dir = project_root / "src" / "gen_ai_engineer" / "10_project_shopping_agent"

sys.path.insert(0, str(app_dir))

from app import app