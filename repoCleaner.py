import os
import requests
from github import Github
from datetime import datetime, timedelta
from dotenv import load_dotenv  # Securely load environment variables

# Load environment variables from .env file
load_dotenv()

# Get credentials securely
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")  # Changeable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Changeable

# Ensure credentials are available
if not GITHUB_TOKEN or not GITHUB_USERNAME:
    raise ValueError("GitHub credentials are missing. Please set them in a .env file.")

# Connect to GitHub
g = Github(GITHUB_TOKEN)

# Define time window (1 year) for stale branches
TIME_WINDOW = datetime.now() - timedelta(days=365)

def get_repositories():
    """Read repository names from masterRepoList.txt"""
    if not os.path.exists("masterRepoList.txt"):
        raise FileNotFoundError("masterRepoList.txt is missing! Please create the file and add your repositories.")
    
    with open("masterRepoList.txt", "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def get_stale_branches(repo_name):
    """Identify stale branches older than 1 year"""
    try:
        repo = g.get_repo(f"{GITHUB_USERNAME}/{repo_name}")
        branches = repo.get_branches()
        stale_branches = []
        
        for branch in branches:
            commit = repo.get_branch(branch.name).commit
            commit_date = commit.commit.author.date

            # Convert commit_date to naive datetime for comparison
            commit_date = commit_date.replace(tzinfo=None)

            if commit_date < TIME_WINDOW:
                stale_branches.append((branch.name, commit_date))
        
        return stale_branches
    
    except Exception as e:
        print(f"Error processing repository {repo_name}: {e}")
        return []

def delete_branches(repo_name, branches):
    """Delete user-selected stale branches"""
    repo = g.get_repo(f"{GITHUB_USERNAME}/{repo_name}")
    
    for branch in branches:
        ref = f"heads/{branch}"
        try:
            repo.get_git_ref(ref).delete()
            print(f"✅ Deleted branch: {branch}")
        except Exception as e:
            print(f"⚠️ Failed to delete {branch}: {e}")

def main():
    """Main execution function"""
    repos = get_repositories()
    
    for repo in repos:
        print(f"\n🔍 Checking repository: {repo}")
        stale_branches = get_stale_branches(repo)
        
        if stale_branches:
            print(f"🛑 Found {len(stale_branches)} stale branches in {repo}:")
            for i, (branch, date) in enumerate(stale_branches, 1):
                print(f"{i}. {branch} (Last commit: {date})")
            
            # Ask user for deletion consent
            choices = input("Enter branch numbers to delete (comma-separated) or 'all': ").strip()
            if choices.lower() == "all":
                selected_branches = [branch for branch, _ in stale_branches]
            else:
                try:
                    selected_indices = [int(i)-1 for i in choices.split(",")]
                    selected_branches = [stale_branches[i][0] for i in selected_indices]
                except:
                    print("⚠️ Invalid input! No branches deleted.")
                    continue

            delete_branches(repo, selected_branches)

        else:
            print(f"✅ No stale branches found in {repo}.")

if __name__ == "__main__":
    main()

