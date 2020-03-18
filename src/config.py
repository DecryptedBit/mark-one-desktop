import os

# Menu bar configuration settings
# - Action configuration settings
from pathlib import Path

DEFAULT_SAVE_DIR            = os.getcwd()

# UI configuration settings
UI_RESOLUTION               = (1280, 720)

# Terminal configuration settings
CONSOLE_PREFIX              = f'> '
CONSOLE_HISTORY_LEN         = 5
CONSOLE_LOGGING             = True
CONSOLE_RESPONSE_LOGGING    = True
CONSOLE_LOG_FILE_PATH       = Path(os.getcwd() + "/Logs") / "console_logs.txt"
