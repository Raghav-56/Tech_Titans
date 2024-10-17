import os

G_API_KEY = os.environ.get("G_API_KEY", "your_default_key_here")
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
ALLOWED_EXTENSIONS = {".pdf", ".html", ".csv", ".xlsx"}
BATCH_SIZE = 1000
