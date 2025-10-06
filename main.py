from github import Github
print("Starting Automated Github-Repository-Sync")

from dotenv import load_dotenv
import os

# Pfad zur .env Datei laden
load_dotenv(dotenv_path=".env/.env")

# Token aus der Umgebungsvariable auslesen
token = os.getenv("github_key")

git = Github(token)

print(token)
print(git)