failed_attempts = 0

with open("sample_logs.txt", "r") as file:
  logs = file.readlines()

for log in logs:
  if "Failed" in log:
    failed_attempts += 1
    print ("Suspicious Detected:", log.strip())

print("\nTotal failed attempts:", failed_attempts)

if failed_attempts >= 3:
  print("Brute force is used!)
        else:
  print("The System is secured")
