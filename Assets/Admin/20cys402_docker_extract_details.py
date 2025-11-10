import requests
import csv
import time

usernames = [
    "adarshrk568", "adithyans636", "agil2004", "aish2913", "amalpromass", "darkstorm22",
    "anaswarasureshmk", "lol0lol", "cbenu4cys22009", "aadhithyasiv", "akshit404", "dockerthingy123",
    "sai150404", "prem011", "rishi3161", "ams7", "vyshalichitla", "charank1904", "hansicachinni",
    "firestrom", "dharshisakthi", "ghamsini", "vettrivelganappathi", "gunateet", "hemupc",
    "harshith1201", "jphemanthkumaar", "joserohit264", "joshua2004", "jeeshitha", "krishna12345678",
    "22034", "kaushik7251", "logesh0107", "lalitha14", "tejas610", "sanjumarri7", "midhru",
    "mukundkumarappan", "meera042", "namitha0710", "navarang", "varshith78", "parthivkumarnikku",
    "pillimetlavamsi", "roopak28", "shanxm", "narenadithya", "sruthi2004", "rahulshankarv",
    "rathneshr", "ramrajs", "thanujjj", "mohanvamsi06", "chakri07", "parzimes", "sharvesh27",
    "shravankrishnan", "siddhuvajjula", "kishansai", "saisupraj", "parvathis066", "amitank67",
    "mukesher4", "anurag018", "nandanamahesh", "shajianagh", "srilakshmi2277", "vichushan",
    "vijaynishanth07", "vishalyeskay", "chandan22076"
]

DETAILS_FILE = "dockerhub_repo_metadata.csv"
SUMMARY_FILE = "dockerhub_user_summary.csv"
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
                "pull_count": repo.get("pull_count", 0) or 0,
                "star_count": repo.get("star_count", 0) or 0,
                "description": repo.get("description", "").strip() if repo.get("description") else ""
            })
        url = data.get("next")
        time.sleep(0.2)
    return repos

all_repos = []
user_summary = []

for user in usernames:
    print(f"🔍 Fetching repositories for {user}...")
    repos = get_user_repositories(user)
    all_repos.extend(repos)
    total_pulls = sum(r.get("pull_count", 0) for r in repos)
    user_summary.append({
        "username": user,
        "num_repositories": len(repos),
        "total_pulls": total_pulls
    })

# Save detailed repo data
with open(DETAILS_FILE, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=[
        "username", "repository_name", "image_link",
        "created_at", "last_updated", "pull_count", "star_count", "description"
    ])
    writer.writeheader()
    writer.writerows(all_repos)

# Save summary data
with open(SUMMARY_FILE, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["username", "num_repositories", "total_pulls"])
    writer.writeheader()
    writer.writerows(user_summary)

print(f"\n✅ Done! {len(all_repos)} repositories saved to '{DETAILS_FILE}'")
print(f"📊 Summary for {len(user_summary)} users saved to '{SUMMARY_FILE}'")
