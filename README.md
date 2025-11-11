# Fetch Users from Public API

This Python script fetches user data from a public API using the **GET** method and displays specific user details.  
It demonstrates how to make HTTP requests, handle JSON responses, and manage errors in Python.

---

## 🚀 Features

- Uses the `requests` library to call the public API endpoint:  
  **https://jsonplaceholder.typicode.com/users**
- Displays:
  - Name  
  - Username  
  - Email  
  - City (from `address.city`)
- Handles:
  - API errors (e.g., failed responses)
  - Empty user lists
- **Optional Bonus:** Prints only users whose city names start with the letter **‘S’**.

---

## 🧰 Requirements

- Python 3.7 or later
- The `requests` library

You can install the required dependency using:

```bash
pip install requests

# How to run the Script

python fetch_users.py

# Example Output

User 1:
Name: Clementine Bauch
Username: Samantha
Email: Nathan@yesenia.net
City: South Elvis
------------------------------
User 2:
Name: Nicholas Runolfsdottir V
Username: Maxime_Nienow
Email: Sherwood@rosamond.me
City: San Antonio
------------------------------
