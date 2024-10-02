# reads
- [ ] https://education.github.com/git-cheat-sheet-education.pdf
- [ ] https://git-scm.com/docs
 
# Navigate to your desired directory
`cd /path/to/your/directory`

| Step                         | Command                                                        | Description                                         |
|------------------------------|----------------------------------------------------------------|-----------------------------------------------------|
| **Initialize a Repository**  | `git init project_name`                                       | Start a new project.                               |
|                              | `cd project_name`                                             | Change into the new project directory.             |
| **Create Files**             | `echo "Hello, World!" > README.md`                           | Create a new file.                                 |
| **Stage Changes**            | `git add README.md`                                          | Add your file to the staging area.                 |
| **Commit Changes**           | `git commit -m "Initial commit"`                             | Commit your staged files with a message.           |
| **Check Status**             | `git status`                                                 | See what changes are staged or modified.           |
| **View Commit History**      | `git log`                                                    | Check the log of your commits.                     |
| **Branching**                | `git branch feature-branch`                                  | Create a new branch for a feature.                 |
|                              | `git checkout feature-branch`                                | Switch to the new branch.                           |
|                              | `git checkout -b feature-branch`                             | Create and switch to the new branch.               |
| **Merge Changes**            | `git checkout master`                                        | Switch back to the main branch.                     |
|                              | `git merge feature-branch`                                   | Merge the feature branch into the main branch.     |
| **Add Remote Repository**    | `git remote add origin https://github.com/username/project_name.git` | Link local repo to remote repo (e.g., GitHub).   |
| **Push Changes**             | `git push -u origin master`                                  | Push your commits to the remote repository.        |



| Command Type | Command                                 | Description                                   |
|--------------|-----------------------------------------|-----------------------------------------------|
| **Local**    | `git init`                             | Initialize a new local repository.           |
|              | `git add <file>`                      | Stage changes for commit.                    |
|              | `git commit -m "message"`             | Commit staged changes with a message.        |
|              | `git status`                          | Check the status of the repository.          |
|              | `git branch <branch-name>`            | Create a new branch.                          |
|              | `git merge <branch-name>`              | Merge a branch into the current branch.      |
| **Remote**   | `git remote add origin <repository-url>` | Add a remote repository.                     |
|              | `git push origin <branch-name>`       | Push local changes to the remote repository.  |
|              | `git pull origin <branch-name>`       | Pull changes from the remote repository.      |
|              | `git fetch origin`                    | Fetch changes from the remote without merging.|
|              | `git remote -v`                       | View remote repository URLs.                  |

