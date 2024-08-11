import sys
import requests

def check_health():
    try:
        response = requests.get("http://localhost:5000/healthcheck")
        if response.status_code == 200:
            sys.exit(0)  # Success, healthy
        else:
            sys.exit(1)  # Unhealthy
    except Exception as e:
        sys.exit(1)  # Unhealthy if there's an exception

if __name__ == "__main__":
    check_health()