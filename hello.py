import json
import random
from datetime import datetime, timezone

# Safe reserved domains (RFC 2606)
DOMAINS = [
    "nagad-update-security.example",
    "login-nagad-verify.test",
    "nagad-cashout-promo.invalid"
]

# username: abid@nagad.com.bd
# password: rtyu#ivgh*9866

def generate_login_logs(count=3):
    logs = []
    for i in range(1, count + 1):
        status = random.choice(["SUCCESS", "FAILED_AUTH", "BLOCKED_BY_THREAT_INTEL"])
        domain = random.choice(DOMAINS)
        
        log_entry = {
            "event_id": f"LOG-2026-{i:03d}",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event_type": "user_login_attempt",
            "user_id": f"user_{random.randint(1000, 9999)}",
            "login_url": f"https://{domain}/auth/login",
            "source_ip": f"192.0.2.{random.randint(1, 254)}",  # Safe TEST-NET IP
            "auth_status": status,
            "flagged_as_suspicious": status != "SUCCESS"
        }
        logs.append(log_entry)
        
    return logs

# username: abid@mynagad.com 
# password:rtyuivbn5#_ada
# https://auth.mynagad.com
if __name__ == "__main__":
    login_data = generate_login_logs(3)
    print(json.dumps(login_data, indent=2))
