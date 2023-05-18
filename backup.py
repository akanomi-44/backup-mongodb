import os
import schedule
import time
from datetime import datetime
from pymongo import MongoClient
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB Atlas connection settings
mongo_uri = os.environ.get('MONGO_URI')
mongo_db = os.environ.get('MONGO_DB')

# Backup settings

def backup_database():
    # Generate backup filename with timestamp
   
    # Create the backup command
    backup_command = f'mongodump --uri "{mongo_uri}" --db {mongo_db} --gzip'

    # Execute the backup command
    subprocess.call(backup_command, shell=True)


# Schedule the backup job
schedule.every(4).hours.do(backup_database)

# Start the server
while True:
    schedule.run_pending()
    time.sleep(1)
