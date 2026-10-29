import subprocess
import os

def run(cmd):
    print(f"--> {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.stdout.strip():
        print("STDOUT:", res.stdout.strip()[:1000])
    if res.stderr.strip():
        print("STDERR:", res.stderr.strip()[:1000])
    return res.returncode

# 1. Initialize and set branch
run("git init")
run("git branch -M main")

# 2. Add all files (respecting .gitignore which excludes Old/)
run("git add .")

# 3. Check status
res = subprocess.run("git status --short", shell=True, capture_output=True, text=True)
lines = [l for l in res.stdout.splitlines() if l.strip()]
print(f"Total staged files: {len(lines)}")
has_old = any("old" in l.lower() for l in lines)
print(f"Does staged files contain 'Old'? {has_old}")

# 4. Commit
commit_msg = "Initial commit: GymOptix system architecture, documentation, and research benchmarks"
run(f'git commit -m "{commit_msg}"')

# 5. Remote setup
run("git remote remove origin")
run("git remote add origin https://github.com/M-a-z-e-n/Gym-Optix.git")
run("git remote -v")

# 6. Push to GitHub
print("Pushing to GitHub...")
code = run("git push -u origin main")
if code == 0:
    print("\nSUCCESSFULLY PUSHED TO GITHUB!")
else:
    print(f"\nPush returned exit code: {code}")
