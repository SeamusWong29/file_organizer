# main.py
print("Hello, file sorting world!")

def scan_folder():
    print("Scanning folder...")

def log(message):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

print("testing branch")
scan_folder()
