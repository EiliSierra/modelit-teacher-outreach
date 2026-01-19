"""
Upload Rhoades School Faculty Contacts to HubSpot
"""

import sys
import requests
import json
import os
from dotenv import load_dotenv

# Fix encoding for Windows
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables
load_dotenv("D:/ClaudeEili/.env")

HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")
HUBSPOT_BASE_URL = "https://api.hubapi.com"

# Faculty data to upload
faculty_data = [
    # Leadership Team
    {"firstname": "Regina", "lastname": "McDuffie", "jobtitle": "Head of School", "email": "rmcduffie@rhoadesschool.com", "phone": "760.436.1102 ext. 308", "company": "The Rhoades School"},
    {"firstname": "Stephanie", "lastname": "Turtz", "jobtitle": "Director of Admissions", "email": "sturtz@rhoadesschool.com", "phone": "760-436-1102 ext. 302", "company": "The Rhoades School"},
    {"firstname": "J.", "lastname": "Pate", "jobtitle": "Middle School Principal", "email": "jpate@rhoadesschool.com", "phone": "760.944.6335 ext. 501", "company": "The Rhoades School"},
    {"firstname": "D.", "lastname": "Schott", "jobtitle": "Business Manager", "email": "dschott@rhoadesschool.com", "phone": "760.436.1102", "company": "The Rhoades School"},

    # Faculty
    {"firstname": "Amaya", "lastname": "Aladross", "jobtitle": "Lower School Before & After School Counselor", "email": "aaladross@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Katie", "lastname": "Atkinson", "jobtitle": "4th Grade Teacher", "email": "katkinson@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Mary", "lastname": "Bologna", "jobtitle": "Middle School Math Teacher", "email": "mbologna@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Ansuya", "lastname": "Bose", "jobtitle": "Dean of Students", "email": "abose@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Kimberly", "lastname": "Cirillo", "jobtitle": "Kindergarten Teacher", "email": "kcirillo@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Siobhan", "lastname": "Crews", "jobtitle": "Middle School Drama Teacher", "email": "screws@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Nick", "lastname": "Dei", "jobtitle": "Middle School Physical Education Teacher", "email": "ndei@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Maggie", "lastname": "DiGrazia", "jobtitle": "Lower School Fine Arts Teacher", "email": "mdigrazia@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Priscilla", "lastname": "Drew", "jobtitle": "Enrollment Director", "email": "pdrew@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Robert", "lastname": "Ellison", "jobtitle": "Middle School Math Teacher", "email": "rellison@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Mariam", "lastname": "Enayat", "jobtitle": "Preschool Teacher", "email": "menayat@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Ron", "lastname": "Florentine", "jobtitle": "Middle School & Lower School Music Teacher", "email": "rflorentine@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Christelle", "lastname": "Francois", "jobtitle": "Preschool Teacher", "email": "cfrancois@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Miranda", "lastname": "Garcia", "jobtitle": "2nd Grade Teacher", "email": "mgarcia@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Barbara", "lastname": "Govea Garcia", "jobtitle": "Preschool Office Administrator", "email": "bgoveagarcia@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
    {"firstname": "Kristofer", "lastname": "Gray", "jobtitle": "Middle School Spanish Teacher", "email": "kgray@rhoadesschool.com", "phone": "", "company": "The Rhoades School"},
]


def create_contact(contact_data):
    """Create a single contact in HubSpot"""
    url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/contacts"
    headers = {
        "Authorization": f"Bearer {HUBSPOT_API_KEY}",
        "Content-Type": "application/json"
    }

    # Build properties, excluding empty values
    properties = {}
    for key, value in contact_data.items():
        if value:  # Only include non-empty values
            properties[key] = value

    payload = {"properties": properties}

    response = requests.post(url, headers=headers, json=payload)
    return response


def create_contacts_batch(contacts):
    """Create multiple contacts using batch API"""
    url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/contacts/batch/create"
    headers = {
        "Authorization": f"Bearer {HUBSPOT_API_KEY}",
        "Content-Type": "application/json"
    }

    # Build batch payload
    inputs = []
    for contact in contacts:
        properties = {k: v for k, v in contact.items() if v}  # Exclude empty values
        inputs.append({"properties": properties})

    payload = {"inputs": inputs}

    response = requests.post(url, headers=headers, json=payload)
    return response


def main():
    print("=" * 60)
    print("HUBSPOT - CARGA DE CONTACTOS")
    print("The Rhoades School Faculty")
    print("=" * 60)

    print(f"\nAPI Key: {HUBSPOT_API_KEY[:20]}...")
    print(f"Total contactos a cargar: {len(faculty_data)}")

    print("\n" + "-" * 60)
    print("Iniciando carga de contactos...")
    print("-" * 60)

    # Try batch upload first
    print("\n[1/2] Intentando carga por lotes (batch)...")

    batch_response = create_contacts_batch(faculty_data)

    if batch_response.status_code == 201:
        result = batch_response.json()
        print(f"\n✅ EXITO! {len(result.get('results', []))} contactos creados por lotes")

        print("\nContactos creados:")
        for contact in result.get('results', []):
            props = contact.get('properties', {})
            print(f"  - {props.get('firstname', '')} {props.get('lastname', '')} ({props.get('email', '')})")
            print(f"    ID: {contact.get('id')} | URL: {contact.get('url', 'N/A')}")

    elif batch_response.status_code == 207:
        # Partial success
        result = batch_response.json()
        print(f"\n⚠️ Carga parcial completada")
        print(f"   Exitosos: {len(result.get('results', []))}")
        print(f"   Errores: {len(result.get('errors', []))}")

        for error in result.get('errors', []):
            print(f"   Error: {error.get('message', 'Unknown error')}")

    else:
        print(f"\n⚠️ Batch fallido (Status: {batch_response.status_code})")
        print(f"   Respuesta: {batch_response.text[:500]}")

        # Fall back to individual uploads
        print("\n[2/2] Cargando contactos individualmente...")

        success_count = 0
        error_count = 0
        errors = []

        for i, contact in enumerate(faculty_data, 1):
            response = create_contact(contact)

            if response.status_code == 201:
                result = response.json()
                print(f"  ✅ {i}/{len(faculty_data)} - {contact['firstname']} {contact['lastname']}")
                success_count += 1
            elif response.status_code == 409:
                print(f"  ⚠️ {i}/{len(faculty_data)} - {contact['firstname']} {contact['lastname']} (ya existe)")
                success_count += 1  # Count as success since contact exists
            else:
                print(f"  ❌ {i}/{len(faculty_data)} - {contact['firstname']} {contact['lastname']}")
                error_count += 1
                errors.append({
                    "contact": f"{contact['firstname']} {contact['lastname']}",
                    "error": response.text
                })

        print("\n" + "=" * 60)
        print("RESUMEN DE CARGA")
        print("=" * 60)
        print(f"\n✅ Exitosos: {success_count}")
        print(f"❌ Errores: {error_count}")

        if errors:
            print("\nDetalles de errores:")
            for err in errors:
                print(f"  - {err['contact']}: {err['error'][:100]}...")

    print("\n" + "=" * 60)
    print("CARGA COMPLETADA")
    print("=" * 60)
    print("\nPuedes ver los contactos en:")
    print("https://app-na2.hubspot.com/contacts/243912370/objects/0-1/views/all/list")


if __name__ == "__main__":
    main()
