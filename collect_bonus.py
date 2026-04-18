import os #1
from rbrapi import RocketBotRoyale
from rbrapi.errors import AuthenticationError, CollectTimedBonusError

def main():
    email = os.environ.get("RBR_EMAIL")
    password = os.environ.get("RBR_PASSWORD")

    if not email or not password:
        print("Error: RBR_EMAIL and RBR_PASSWORD environment variables must be set.")
        return

    print(f"Logging in as {email}...")

    try:
        client = RocketBotRoyale(email=email, password=password)
        print("Login successful!")
    except AuthenticationError as e:
        print(f"Login failed: {e}")
        return

    try:
        success = client.collect_timed_bonus()
        if success:
            print("Timed bonus collected successfully!")
        else:
            print("Could not collect timed bonus. It may not be ready yet.")
    except CollectTimedBonusError as e:
        print(f"Failed to collect timed bonus: {e}")
    except AuthenticationError as e:
        print(f"Authentication error while collecting bonus: {e}")

if __name__ == "__main__":
    main()
