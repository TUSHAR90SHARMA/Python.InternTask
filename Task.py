import requests


def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx/5xx)

        users = response.json()

        if not users:
            print("No users found.")
            return

        # Optional Bonus: filter only users whose city starts with 'S'
        filtered_users = [user for user in users if user['address']['city'].startswith('S')]

        for i, user in enumerate(filtered_users, start=1):
            print(f"User {i}:")
            print(f"Name: {user['name']}")
            print(f"Username: {user['username']}")
            print(f"Email: {user['email']}")
            print(f"City: {user['address']['city']}")
            print("-" * 30)

    except requests.exceptions.RequestException as e:
        print("Error fetching users:", e)


if __name__ == "__main__":
    fetch_users()
