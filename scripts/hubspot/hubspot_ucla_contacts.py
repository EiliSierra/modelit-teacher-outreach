"""
Create UCLA Education Department contacts in HubSpot
"""
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv("D:/ClaudeEili/.env")

HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")
HUBSPOT_BASE_URL = "https://api.hubapi.com"

# UCLA Education Department Chairs data
UCLA_CONTACTS = [
    {
        "email": "rios-aguilar@gseis.ucla.edu",
        "firstname": "Cecilia",
        "lastname": "Rios-Aguilar",
        "jobtitle": "Chair, Department of Education",
        "company": "UCLA School of Education & Information Studies",
        "phone": "(310) 794-7914",
        "address": "Moore Hall 2339, 405 Hilgard Avenue",
        "city": "Los Angeles",
        "state": "California",
        "zip": "90095-1521",
        "website": "https://seis.ucla.edu/faculty/cecilia-rios-aguilar/"
    },
    {
        "email": "webb@ucla.edu",
        "firstname": "Noreen",
        "lastname": "Webb",
        "jobtitle": "Vice Chair (Academic Personnel), Distinguished Professor",
        "company": "UCLA School of Education & Information Studies",
        "phone": "(310) 825-1897",
        "address": "Moore Hall 2019A, 405 Hilgard Avenue",
        "city": "Los Angeles",
        "state": "California",
        "zip": "90095-1521",
        "website": "https://seis.ucla.edu/faculty/"
    },
    {
        "email": "jfmtz@g.ucla.edu",
        "firstname": "Jose Felipe",
        "lastname": "Martinez Fernandez",
        "jobtitle": "Vice Chair (Undergraduate Education), Professor",
        "company": "UCLA School of Education & Information Studies",
        "phone": "",
        "address": "Moore Hall 2011, 405 Hilgard Avenue",
        "city": "Los Angeles",
        "state": "California",
        "zip": "90095-1521",
        "website": "https://seis.ucla.edu/faculty/jose-felipe-martinez/"
    },
    {
        "email": "marin@gseis.ucla.edu",
        "firstname": "Ananda",
        "lastname": "Marin",
        "jobtitle": "Vice Chair (Graduate Education), Associate Professor",
        "company": "UCLA School of Education & Information Studies",
        "phone": "",
        "address": "Moore Hall 3341, 405 Hilgard Avenue",
        "city": "Los Angeles",
        "state": "California",
        "zip": "90095-1521",
        "website": "https://gseis.ucla.edu/directory/ananda-marin/"
    }
]

def create_contact(contact_data):
    """Create a single contact in HubSpot"""
    url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/contacts"

    headers = {
        "Authorization": f"Bearer {HUBSPOT_API_KEY}",
        "Content-Type": "application/json"
    }

    # Build properties payload
    properties = {
        "email": contact_data["email"],
        "firstname": contact_data["firstname"],
        "lastname": contact_data["lastname"],
        "jobtitle": contact_data["jobtitle"],
        "company": contact_data["company"],
        "address": contact_data["address"],
        "city": contact_data["city"],
        "state": contact_data["state"],
        "zip": contact_data["zip"],
        "website": contact_data["website"]
    }

    # Add phone if available
    if contact_data.get("phone"):
        properties["phone"] = contact_data["phone"]

    payload = {"properties": properties}

    print(f"\n[CREATING] {contact_data['firstname']} {contact_data['lastname']}")
    print(f"  Email: {contact_data['email']}")

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        result = response.json()
        print(f"  [OK] Contact created successfully! ID: {result.get('id')}")
        return result
    elif response.status_code == 409:
        print(f"  [EXISTS] Contact already exists in HubSpot")
        # Try to get existing contact
        return {"status": "exists", "email": contact_data["email"]}
    else:
        print(f"  [ERROR] Status: {response.status_code}")
        print(f"  Response: {response.text[:300]}")
        return None

def list_contacts():
    """List all contacts in HubSpot"""
    url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/contacts"

    headers = {
        "Authorization": f"Bearer {HUBSPOT_API_KEY}",
        "Content-Type": "application/json"
    }

    params = {
        "limit": 10,
        "properties": "email,firstname,lastname,jobtitle,company"
    }

    print("\n[LISTING] Current contacts in HubSpot...")
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        result = response.json()
        contacts = result.get("results", [])
        print(f"  Found {len(contacts)} contacts")
        for contact in contacts:
            props = contact.get("properties", {})
            print(f"  - {props.get('firstname', '')} {props.get('lastname', '')} ({props.get('email', 'N/A')})")
        return result
    else:
        print(f"  [ERROR] Status: {response.status_code}")
        print(f"  Response: {response.text[:300]}")
        return None

def main():
    print("=" * 60)
    print("HubSpot - UCLA Education Department Contacts")
    print("=" * 60)

    if not HUBSPOT_API_KEY:
        print("[ERROR] HUBSPOT_API_KEY not found in .env file")
        return

    print(f"\n[INFO] API Key loaded (first 20 chars): {HUBSPOT_API_KEY[:20]}...")

    # Create contacts
    created = []
    errors = []

    for contact in UCLA_CONTACTS:
        result = create_contact(contact)
        if result:
            created.append(contact["email"])
        else:
            errors.append(contact["email"])

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Created/Existing: {len(created)}")
    print(f"  Errors: {len(errors)}")

    if errors:
        print("\n  Failed contacts:")
        for email in errors:
            print(f"    - {email}")

    # List contacts to verify
    print("\n" + "=" * 60)
    list_contacts()

if __name__ == "__main__":
    main()
