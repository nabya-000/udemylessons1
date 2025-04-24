
import re
log_entry = "ERROR [2024-01-02 15:20:18] connection timeout in data"
print("our log entry:", log_entry)
pattern = r'ERROR \[(.*?)\] (.*)'
match = re.search(pattern,log_entry)
print("timestamp: ", match.group(1))
print("error_message: ", match.group(2))