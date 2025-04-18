import os

class Config:
    JSONIFY_PRETTYPRINT_REGULAR = True
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # Limit upload size (100 MB)
    DEBUG = True

    # Load cookies from environment variable
    COOKIES = os.getenv("COOKIES")
