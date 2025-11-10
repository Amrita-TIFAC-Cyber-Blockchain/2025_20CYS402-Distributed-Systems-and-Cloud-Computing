import requests
import csv
import time

usernames = [
    "adarshrk568", "adithyans636", "agil2004", "aish2913", "amalpromass", "darkstorm22",
    "anaswarasureshmk", "lol0lol", "cbenu4cys22009", "AadhithyaSiv", "Akshit404", "dockerthingy123",
    "sai150404", "prem011", "rishi3161", "ams7", "VyshaliChitla", "charank1904", "hansicachinni",
    "firestrom", "dharshisakthi", "ghamsini", "VettrivelGanappathi", "gunateet", "hemupc",
    "harshith1201", "jphemanthkumaar", "joserohit264", "joshua2004", "jeeshitha", "krishna12345678",
    "22034", "kaushik7251", "Logesh0107", "lalitha14", "tejas610", "sanjumarri7", "Midhru",
    "mukundkumarappan", "meera042", "namitha0710", "navarang", "varshith78", "parthivkumarnikku",
    "pillimetlavamsi", "Roopak28", "shanxm", "narenadithya", "sruthi2004", "rahulshankarv",
    "rathneshr", "RamrajS", "thanujjj", "mohanvamsi06", "chakri07", "parzimes", "sharvesh27",
    "shravankrishnan", "siddhuvajjula", "kishansai", "Saisupraj", "ParvathiS066", "amitank67",
    "mukesher4", "Anurag018", "nandanamahesh", "shajianagh", "srilakshmi2277", "vichushan",
    "vijaynishanth07", "vishalyeskay", "chandan22076"
]

OUTPUT_FILE = "dockerhub_repo_metadata.csv"
API_URL_TEMPLATE = "https://hub.docker.com/v2/repositories/{username}/?page_size=100"

def get_user_repositories(username):
    repos = []
    url = API_URL_TEMPLATE.format(username=username)
    while url:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"❌ Failed for {username} ({response.status_code})")
            break
        data = response.json()
        for repo in data.get("results", []):
            repos.append({
                "username": username,
                "repository_name": repo.get("name", ""),
                "image_link": f"https://hub.docker.com/r/{username}/{repo.get('name', '')}",
                "created_at": repo.get("created_at", "N/A"),
                "last_updated": repo.get("updated_at", "N/A"),
                "pull_count": repo.get("pull_count", "N/A"),
                "star_count": repo.get("star_count", "N/A"),
                "description": repo.get("description", "").strip() if repo.get("description") else ""
            })
        url = data.get("next")
        time.sleep(0.2)
    return repos

all_repos = []
for user in usernames:
    print(f"🔍 Fetching repositories for {user}...")
    all_repos.extend(get_user_repositories(user))

# Save to CSV
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=[
        "username", "repository_name", "image_link",
        "created_at", "last_updated", "pull_count", "star_count", "description"
    ])
    writer.writeheader()
    writer.writerows(all_repos)

print(f"\n✅ Done! {len(all_repos)} repositories saved to {OUTPUT_FILE}")

