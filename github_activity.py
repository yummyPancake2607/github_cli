import sys
import urllib.request
import urllib.error  # 🆕 For catching HTTP errors
import json

# Step 1: Get the GitHub username from the command line
if len(sys.argv) < 2:
    print("Usage: python github_activity.py <github_username>")
    sys.exit(1)

username = sys.argv[1]
print(f"Fetching activity for GitHub user: {username}")

# Step 2: Build the GitHub API URL
url = f"https://api.github.com/users/{username}/events"

# Step 3: Make the API request and parse JSON data
try:
    with urllib.request.urlopen(url) as response:
        data = response.read()
        events = json.loads(data)

        # Handle API rate limit error
        if isinstance(events, dict) and events.get("message") == "API rate limit exceeded":
            print("🚫 GitHub API rate limit exceeded. Try again later.")
            sys.exit(1)

        # Step 5: Handle no activity
        if not events:
            print("ℹ️ No recent public activity found.")
            sys.exit(0)

except urllib.error.HTTPError as e:
    if e.code == 404:
        print("❌ User not found. Please check the GitHub username.")
    else:
        print(f"❌ GitHub returned an HTTP error: {e.code}")
    sys.exit(1)

except urllib.error.URLError:
    print("❌ Failed to connect to GitHub. Check your internet connection.")
    sys.exit(1)

except json.JSONDecodeError:
    print("❌ Failed to parse GitHub response.")
    sys.exit(1)

# ✅ Step 4: Display the events
print("\nRecent Public Activity:\n")

for event in events:
    event_type = event["type"]
    repo = event["repo"]["name"]

    if event_type == "PushEvent":
        commit_count = len(event["payload"].get("commits", []))
        print(f"- Pushed {commit_count} commits to {repo}")

    elif event_type == "WatchEvent":
        print(f"- Starred {repo}")

    elif event_type == "IssuesEvent":
        action = event["payload"]["action"]
        print(f"- {action.capitalize()} an issue in {repo}")

    elif event_type == "CreateEvent":
        ref_type = event["payload"]["ref_type"]
        print(f"- Created a new {ref_type} in {repo}")

    else:
        print(f"- {event_type} in {repo}")
