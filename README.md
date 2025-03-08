# repoCleaner
# 🚀 GitHub Stale Branch Cleaner

## 📌 Overview
The **GitHub Stale Branch Cleaner** helps clean up repositories by detecting and removing stale branches (older than 1 year). This script automates the process of identifying and deleting outdated branches, making repository maintenance easier.

---

## 📂 Steps to Follow

### **1️⃣ Fork the Repositories**
- Go to the GitHub repositories that need stale branch cleanup.
- Click **Fork** to create copies in your GitHub account.

### **2️⃣ Clone the Forked Repositories**
- Download the repositories to your local system for processing.

### **3️⃣ Set Up the Cleaning Script**
- Configure the script to check for stale branches.
- **Created the following files:**
  - `repoCleaner.py` → Main script to detect and delete stale branches.
  - `.env` → Stores credentials securely.
  - `.gitignore` → Prevents accidental leaks of sensitive files.
  - `masterRepoList.txt` → Contains a list of repositories to scan.

### **4️⃣ Install Dependencies**
  Run the following command to install required dependencies:
  $ pip install PyGithub python-dotenv

### 5️⃣ Run the Script
  Execute the script to scan for stale branches:
  $  python3 repoCleaner.py
  The script will list branches that haven’t been updated in over a year.

6️⃣ Select Branches for Deletion -
********************************
  Choose to delete all stale branches or select specific ones.
  The script will remove only the selected branches.
  Note: Ensure you only delete branches you no longer need.

7️⃣ Verify the Cleanup -
***********************
  Go to GitHub and check if the branches have been deleted.
  Ensure no necessary branches were removed.

8️⃣ Test with a Sample Stale Branch (Optional) -
***********************************************
  To test, create a test branch with an old commit date and run the script to confirm that it detects and deletes the branch.
  Test with a Sample Stale Branch (Optional)
  Create a Stale Test Branch
  
  $  git checkout -b test-stale-branch
  $  echo "Testing stale branch" > stale_branch.txt
  $  git add stale_branch.txt
  $  git commit -m "Adding test file for stale branch"
  $  GIT_COMMITTER_DATE="2022-01-01T12:00:00" git commit --amend --no-edit --date "2022-01-01T12:00:00"
  $  git push origin test-stale-branch

9️⃣ Maintain Repository Cleanliness -
*************************************
  Run the script periodically to keep repositories clean.
  Automate the process if necessary.
