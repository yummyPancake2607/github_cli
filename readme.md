
# GitHub Activity CLI

A simple command-line Python tool to fetch and display the recent public activity of any GitHub user — using only Python’s built-in libraries (no external packages).

---

## 📌 Features

- Accepts a GitHub username as a command-line argument
- Connects to the GitHub public API
- Parses and displays recent public events such as:
  - Commit pushes
  - Starred repositories
  - Created branches or repositories
  - Opened or closed issues
- Gracefully handles errors like:
  - Invalid username
  - No internet connection
  - GitHub rate limit exceeded
  - No recent activity
- Uses only built-in Python modules: `sys`, `urllib`, `json`

---

## 🚀 How to Run

### 1. Save the Script

Create a Python file named `github_activity.py` and paste the code into it.

---

### 2. Run the script from terminal

```bash
python github_activity.py <github_username>
````

#### ✅ Example:

```bash
python github_activity.py torvalds
```

---

## 🧪 Sample Output

```
Fetching activity for GitHub user: torvalds

Recent Public Activity:

- Pushed 3 commits to torvalds/linux
- Starred torvalds/test-repo
- Created a new repository in torvalds/sample
```

---

## ⚠️ Error Handling

| Problem                    | Error Message                                |
| -------------------------- | -------------------------------------------- |
| No username provided       | Usage: python github\_activity.py <username> |
| Invalid username (404)     | ❌ User not found. Please check the username. |
| No internet / DNS error    | ❌ Failed to connect to GitHub                |
| GitHub rate limit exceeded | 🚫 GitHub API rate limit exceeded            |
| No recent activity         | ℹ️ No recent public activity found.          |

---

## 📚 Built With

* Python 3
* `sys` – for command-line arguments
* `urllib.request` – for making HTTP requests
* `urllib.error` – for handling HTTP/network errors
* `json` – for parsing the API response

---

## 🌱 Author

**Lakshit Verma**
Beginner Python Developer
Learning APIs and building CLI tools through projects like this one!

---
