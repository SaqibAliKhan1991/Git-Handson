________________________________________
1. Introduction to Git
What Git is:
•	A distributed version control system
•	Tracks changes in your code
•	Lets multiple people work on the same project safely
Key Concepts:
•	Repository (repo) → Your project tracked by Git
•	Commit → Snapshot of your code
•	Branch → Parallel version of your code
•	Merge → Combine changes from different branches
•	Remote → GitHub, GitLab, or Bitbucket repository
Commands to know:
git --version             # Check Git version
git help                  # Get help
git init                  # Initialize a Git repo
git status                # Show current status
git log                   # View commit history
________________________________________
2. Setting Up Git
Global configuration:
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"  # Use VS Code as editor
Check config:
git config --list
________________________________________
3. Creating and Cloning Repositories
Create a new local repo:
mkdir my-project
cd my-project
git init
Clone an existing repo:
git clone https://github.com/username/repo.git
________________________________________
4. Basic Git Workflow
1. Stage files:
git add file.txt          # Stage a single file
git add .                 # Stage all files
2. Commit changes:
git commit -m "Add initial code"
3. Push to remote:
git remote add origin https://github.com/username/repo.git
git branch -M main        # Rename default branch
git push -u origin main
4. Pull changes:
git pull origin main
________________________________________
5. Branching and Merging
Create a branch:
git branch feature-login
git checkout feature-login
# or shortcut
git switch -c feature-login
Merge branch into main:
git checkout main
git merge feature-login
Delete branch:
git branch -d feature-login
________________________________________
6. Handling Conflicts
•	Git will warn if two branches modify the same line
•	Open the conflicted file, fix manually, then:
git add file.txt
git commit
________________________________________
7. Undoing Changes
Unstaged changes:
git restore file.txt
Staged changes:
git restore --staged file.txt
Undo last commit (keep changes):
git reset --soft HEAD~1
Undo last commit (discard changes):
git reset --hard HEAD~1
________________________________________
8. Viewing History
git log                       # Full history
git log --oneline --graph      # Compact, visual
git diff                       # Differences not staged
git diff --staged               # Differences staged
________________________________________
9. Working with Remotes
Check remotes:
git remote -v
Add new remote:
git remote add origin URL
Fetch changes:
git fetch origin
Push branch:
git push -u origin branch-name
________________________________________
10. .gitignore
•	Prevent files from being tracked:
__pycache__/
*.log
.env
________________________________________
11. Advanced Git
Rebasing:
git rebase main
Stashing:
git stash           # Save uncommitted changes
git stash pop       # Apply stash
Cherry-pick commits:
git cherry-pick <commit-hash>
Tagging releases:
git tag v1.0
git push origin v1.0
________________________________________
12. Git Best Practices
•	Commit often, with meaningful messages
•	Use branches for features/bug fixes
•	Pull before pushing
•	Don’t commit secrets
•	Keep .gitignore up to date
•	Write clean commit messages (imperative tense)
________________________________________
13. Mini Projects to Practice Git
1.	Create a Python project and push it to GitHub
2.	Work with a friend: clone the repo, create a branch, merge changes
3.	Track log files or notes using Git

