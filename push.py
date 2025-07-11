import os
os.system("git add .")
print("Staged all changes.")
text = str(input("What is the commit msg? \n").strip())
os.system(f"git commit -m \"{text}\"")
print("Committed changes with message:", text)
os.system("git push origin main")
print("Pushed changes to origin/main branch.")