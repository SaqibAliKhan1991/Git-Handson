import shutil
import datetime
import os

source = "app.log"
backup_dir = "backup"

# Create backup folder if it doesn't exist
os.makedirs(backup_dir, exist_ok=True)

# Get current date
date = datetime.datetime.now().strftime("%Y-%m-%d")

# Backup file name
backup_file = f"{backup_dir}/app_{date}.log"

# Copy file
shutil.copy(source, backup_file)
print(f"Backup saved as {backup_file}")

