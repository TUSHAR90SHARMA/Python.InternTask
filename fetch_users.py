import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for 4xx/5xx

        users = response.json()

        if not users:
            print("No users found.")
            return

        # Optional Bonus: filter users whose city starts with 'S'
        filtered_users = [user for user in users if user['address']['city'].startswith('S')]

        for index, user in enumerate(filtered_users, start=1):
            print(f"User {index}:")
            print(f"Name: {user['name']}")
            print(f"Username: {user['username']}")
            print(f"Email: {user['email']}")
            print(f"City: {user['address']['city']}")
            print("-" * 30)

    except requests.exceptions.RequestException as e:
        print("Error fetching data from API:", e)


if __name__ == "__main__":
    fetch_users()
