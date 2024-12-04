from datetime import datetime

print(datetime.now())
# import datetime
# datetime.datetime.now()

with open("server.log", "w", newline="\n") as file:
    file.write("""2024-12-04 10:23:45,INFO,Service started
2024-12-04 10:24:05,WARNING,High memory usage
2024-12-04 10:25:12,ERROR,Service failed
2024-12-04 10:26:30,INFO,Service restarted
""")

with open("server.log", "a", newline="\n") as file:
    file.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")},INFO,Logged from function")

log_entries = []
with open("server.log") as log_file:
    for line in log_file:
        timestamp, severity, message = line.strip().split(",")
        log_entries.append({
            "timestamp": timestamp,
            "severity": severity,
            "message": message
        })

print(log_entries)

def filter_logs_by_severity(log_entries, severity):
    return [entry for entry in log_entries if entry["severity"] == severity]

def filter_logs_by_severity(log_entries, severity):
    result = []
    for entry in log_entries:
        if entry["severity"] == severity:
            result.append(entry)
    return result

for severity in ["INFO", "WARNING", "ERROR"]:
    filtered_log = filter_logs_by_severity(log_entries, severity)
    with open(f"{severity.lower()}_logs.txt", "w", newline="\n") as severity_file:
        for entry in filtered_log:
            severity_file.write(f'{entry["timestamp"]},{entry["severity"]},{entry["message"]}\n')

print("Printed filtered logs.")

severity_count = {}
for entry in log_entries:
    severity = entry["severity"]
    # severity_count[severity]
    severity_count[severity] = severity_count.get(severity, 0) + 1

with open("log_report.txt", "w", newline="\n") as report:
    for severity, count in severity_count.items():
        report.write(f"{severity}: {count}\n")