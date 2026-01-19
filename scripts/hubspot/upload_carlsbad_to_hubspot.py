"""
Upload Carlsbad USD Staff Directory to HubSpot
Group: Teachers K12
"""

import sys
import csv
import requests
import os
import time
from dotenv import load_dotenv

# Fix encoding for Windows
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables
load_dotenv("D:/ClaudeEili/.env")

HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")
HUBSPOT_BASE_URL = "https://api.hubapi.com"
CSV_FILE = "D:/ClaudeEili/Scripts/carlsbad_staff_directory.csv"

def parse_name(full_name):
    """Split full name into first and last name"""
    if not full_name:
        return "", ""

    # Clean the name
    name = full_name.strip()

    # Skip invalid entries (phone numbers, office entries, etc.)
    if name.startswith("760-") or "office" in name.lower():
        return "", ""

    parts = name.split()
    if len(parts) == 1:
        return parts[0], ""
    elif len(parts) == 2:
        return parts[0], parts[1]
    else:
        # First name is first part, last name is the rest
        return parts[0], " ".join(parts[1:])

def load_contacts_from_csv():
    """Load and parse contacts from CSV file"""
    contacts = []

    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = row.get('Email', '').strip()

            # Skip entries without valid email
            if not email or '@' not in email:
                continue

            # Skip office/general emails
            if 'office.' in email.lower() or email.startswith('760-'):
                continue

            firstname, lastname = parse_name(row.get('Name', ''))

            # If no name parsed, try to get from email
            if not firstname and not lastname:
                email_name = email.split('@')[0]
                if '.' in email_name:
                    parts = email_name.split('.')
                    firstname = parts[0].capitalize()
                    lastname = parts[1].capitalize() if len(parts) > 1 else ""
                else:
                    firstname = email_name.capitalize()

            school = row.get('School', 'Carlsbad USD')
            position = row.get('Position', '')

            contact = {
                "email": email,
                "firstname": firstname,
                "lastname": lastname,
                "company": f"Teachers K12 - Carlsbad USD - {school}",
                "jobtitle": position if position else "Staff"
            }

            contacts.append(contact)

    return contacts

def create_contacts_batch(contacts):
    """Create multiple contacts using batch API (max 100 per batch)"""
    url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/contacts/batch/create"
    headers = {
        "Authorization": f"Bearer {HUBSPOT_API_KEY}",
        "Content-Type": "application/json"
    }

    inputs = []
    for contact in contacts:
        properties = {k: v for k, v in contact.items() if v}
        inputs.append({"properties": properties})

    payload = {"inputs": inputs}

    response = requests.post(url, headers=headers, json=payload)
    return response

def main():
    print("=" * 60)
    print("HUBSPOT - CARGA DE CONTACTOS")
    print("Carlsbad USD Staff Directory")
    print("Grupo: Teachers K12")
    print("=" * 60)

    # Load contacts
    print("\n[1/3] Cargando contactos del CSV...")
    contacts = load_contacts_from_csv()
    print(f"      Contactos validos encontrados: {len(contacts)}")

    if not contacts:
        print("\n[ERROR] No se encontraron contactos validos")
        return

    # Show sample
    print("\n      Muestra de contactos:")
    for c in contacts[:5]:
        print(f"        - {c['firstname']} {c['lastname']} ({c['email']})")
    print(f"        ... y {len(contacts)-5} mas")

    # Upload in batches of 100
    print("\n[2/3] Subiendo contactos a HubSpot...")

    batch_size = 100
    total_created = 0
    total_errors = 0

    for i in range(0, len(contacts), batch_size):
        batch = contacts[i:i+batch_size]
        batch_num = (i // batch_size) + 1
        total_batches = (len(contacts) + batch_size - 1) // batch_size

        print(f"\n      Batch {batch_num}/{total_batches} ({len(batch)} contactos)...")

        response = create_contacts_batch(batch)

        if response.status_code == 201:
            result = response.json()
            created = len(result.get('results', []))
            total_created += created
            print(f"      [OK] {created} contactos creados")

        elif response.status_code == 207:
            # Partial success
            result = response.json()
            created = len(result.get('results', []))
            errors = len(result.get('errors', []))
            total_created += created
            total_errors += errors
            print(f"      [PARCIAL] {created} creados, {errors} errores")

        else:
            print(f"      [ERROR] Status: {response.status_code}")
            error_data = response.json() if response.text else {}

            # Check if it's duplicate error
            if 'CONFLICT' in str(error_data):
                print(f"      (Algunos contactos ya existen)")
            else:
                print(f"      {str(error_data)[:200]}")

            total_errors += len(batch)

        # Rate limiting - wait between batches
        if i + batch_size < len(contacts):
            time.sleep(1)

    # Summary
    print("\n" + "=" * 60)
    print("RESUMEN DE CARGA")
    print("=" * 60)
    print(f"\n  Total procesados: {len(contacts)}")
    print(f"  Creados exitosamente: {total_created}")
    print(f"  Errores/Duplicados: {total_errors}")

    print("\n" + "=" * 60)
    print("CARGA COMPLETADA")
    print("=" * 60)
    print("\nPuedes ver los contactos en:")
    print("https://app-na2.hubspot.com/contacts/243912370/objects/0-1/views/all/list")
    print("\nPara filtrar por grupo, busca en Company: 'Teachers K12'")

if __name__ == "__main__":
    main()
