import requests

response = requests.get("https://api.github.com")

if response.status_code == 200:
    print("✅ GitHub API ist erreichbar!")
else:
    print(f"❌ Fehler: {response.status_code}")
