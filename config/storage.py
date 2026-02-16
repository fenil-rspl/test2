import os
from config.constants import UPLOAD_DIRECTORY

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)