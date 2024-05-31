from dotenv import load_dotenv
import os

load_dotenv()

FTP_HOST = os.getenv('FTP_HOST', '87.120.179.246')
FTP_PORT = int(os.getenv('FTP_PORT', 31222))
FTP_USER = os.getenv('FTP_USER', 'wwwpremier2024')
FTP_PASS = os.getenv('FTP_PASS', 'wwwprem!er2@24')
DIRECTORY_PATH = os.getenv('DIRECTORY_PATH', r"C:\Users\Stan\PycharmProjects\PremierFort")
