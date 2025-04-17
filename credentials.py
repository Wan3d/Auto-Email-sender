import os
from dotenv import load_dotenv

load_dotenv()

gmailUser = os.getenv("gmailUser")
gmailPassword = os.getenv("gmailPassword")
gmailReceiver = os.getenv("gmailReceiver")