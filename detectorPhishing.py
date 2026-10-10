import re

def isPhishing(url):
    risk = 0
    reason = []

    if re.match(r"https?://\d+\.\d+\.\d+\.\d+", url):
        risk += 2
        reason.append("URL contains IP address")

    if "@" in url:
        risk += 1
        reason.append("URL contains @ symbol")

    if len(url) > 75:
        risk += 1
        reason.append("URL is too long")

    suspicious = ["login", "verify", "secure", "account", "update"]
    for word in suspicious:
        if word in url.lower():
            risk += 1
            reason.append(f"contains suspicious word: {word}")

    if risk == 0:
        reason.append("Looks safe")
        return False, risk, reason
    else:
        return True, risk, reason

#Testing
url = input("Enter URL to check: ")
result, risk, reasons = isPhishing(url)
print(f"\nRisk Score:{risk}")
print(f"isPhishing?:{result}")
print(f"Reasons:{reasons}")
