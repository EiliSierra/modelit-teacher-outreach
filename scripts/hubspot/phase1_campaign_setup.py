"""
Phase 1: HubSpot Campaign Setup for ModelIt
============================================
Creates static list, adds test contact, and prepares email sending.
"""

import sys
import requests
import os
import json
from dotenv import load_dotenv

# Fix encoding for Windows
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables
load_dotenv("D:/ClaudeEili/.env")

HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")
HUBSPOT_BASE_URL = "https://api.hubapi.com"

HEADERS = {
    "Authorization": f"Bearer {HUBSPOT_API_KEY}",
    "Content-Type": "application/json"
}

# ============================================================================
# STEP 1: Get all Carlsbad contacts
# ============================================================================

def get_carlsbad_contacts():
    """Fetch all contacts with @carlsbadusd.net emails"""
    print("\n[STEP 1] Buscando contactos de Carlsbad USD...")

    all_contacts = []
    after = None

    while True:
        url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/contacts/search"
        payload = {
            "filterGroups": [{
                "filters": [{
                    "propertyName": "email",
                    "operator": "CONTAINS_TOKEN",
                    "value": "carlsbadusd.net"
                }]
            }],
            "properties": ["email", "firstname", "lastname", "company"],
            "limit": 100
        }

        if after:
            payload["after"] = after

        response = requests.post(url, headers=HEADERS, json=payload)

        if response.status_code != 200:
            print(f"  [ERROR] {response.status_code}: {response.text[:200]}")
            break

        data = response.json()
        results = data.get("results", [])
        all_contacts.extend(results)

        # Check for pagination
        paging = data.get("paging", {})
        next_page = paging.get("next", {})
        after = next_page.get("after")

        if not after:
            break

    print(f"  [OK] Encontrados {len(all_contacts)} contactos @carlsbadusd.net")
    return all_contacts

# ============================================================================
# STEP 2: Create static list
# ============================================================================

def create_static_list(list_name="Teachers K12 - Carlsbad"):
    """Create a static list for the campaign"""
    print(f"\n[STEP 2] Creando lista estatica: {list_name}...")

    url = f"{HUBSPOT_BASE_URL}/crm/v3/lists"

    payload = {
        "name": list_name,
        "processingType": "MANUAL",  # Static list
        "objectTypeId": "0-1"  # Contacts
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code == 200 or response.status_code == 201:
        list_data = response.json()
        list_id = list_data.get("listId")
        print(f"  [OK] Lista creada con ID: {list_id}")
        return list_id
    elif response.status_code == 409:
        print(f"  [INFO] La lista ya existe. Buscando ID...")
        # Try to find existing list
        existing_id = find_list_by_name(list_name)
        if existing_id:
            print(f"  [OK] Lista encontrada con ID: {existing_id}")
            return existing_id
        else:
            print(f"  [ERROR] No se pudo encontrar la lista existente")
            return None
    else:
        print(f"  [ERROR] {response.status_code}: {response.text[:300]}")
        return None

def find_list_by_name(list_name):
    """Find a list by its name"""
    url = f"{HUBSPOT_BASE_URL}/crm/v3/lists/search"

    payload = {
        "query": list_name,
        "processingTypes": ["MANUAL"]
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code == 200:
        data = response.json()
        lists = data.get("lists", [])
        for lst in lists:
            if lst.get("name") == list_name:
                return lst.get("listId")
    return None

# ============================================================================
# STEP 3: Add contacts to list
# ============================================================================

def add_contacts_to_list(list_id, contact_ids):
    """Add contacts to a static list"""
    print(f"\n[STEP 3] Agregando {len(contact_ids)} contactos a la lista...")

    # HubSpot limits: 500 contacts per request
    batch_size = 500
    total_added = 0

    for i in range(0, len(contact_ids), batch_size):
        batch = contact_ids[i:i+batch_size]

        url = f"{HUBSPOT_BASE_URL}/crm/v3/lists/{list_id}/memberships/add"

        payload = batch

        response = requests.put(url, headers=HEADERS, json=payload)

        if response.status_code == 200:
            total_added += len(batch)
            print(f"  [OK] Agregados {len(batch)} contactos (total: {total_added})")
        else:
            print(f"  [ERROR] {response.status_code}: {response.text[:200]}")

    return total_added

# ============================================================================
# STEP 4: Add test contact
# ============================================================================

def add_test_contact(email="eilisierra@hootmail.com", firstname="Test", lastname="Campaign"):
    """Add a test contact for email preview"""
    print(f"\n[STEP 4] Agregando contacto de prueba: {email}...")

    # Check if contact exists
    search_url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/contacts/search"
    search_payload = {
        "filterGroups": [{
            "filters": [{
                "propertyName": "email",
                "operator": "EQ",
                "value": email
            }]
        }],
        "properties": ["email", "firstname", "lastname"]
    }

    response = requests.post(search_url, headers=HEADERS, json=search_payload)

    if response.status_code == 200:
        data = response.json()
        if data.get("total", 0) > 0:
            contact = data["results"][0]
            print(f"  [INFO] Contacto ya existe con ID: {contact['id']}")
            return contact["id"]

    # Create new contact
    create_url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/contacts"
    create_payload = {
        "properties": {
            "email": email,
            "firstname": firstname,
            "lastname": lastname,
            "company": "Test - Campaign Preview"
        }
    }

    response = requests.post(create_url, headers=HEADERS, json=create_payload)

    if response.status_code == 201:
        contact = response.json()
        print(f"  [OK] Contacto creado con ID: {contact['id']}")
        return contact["id"]
    else:
        print(f"  [ERROR] {response.status_code}: {response.text[:200]}")
        return None

# ============================================================================
# STEP 5: List verified email addresses
# ============================================================================

def get_verified_emails():
    """Get list of verified sender emails"""
    print("\n[STEP 5] Verificando emails remitentes disponibles...")

    # This endpoint requires Marketing Hub
    url = f"{HUBSPOT_BASE_URL}/marketing/v3/emails/send-from-addresses"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        addresses = data.get("results", [])
        print(f"  [OK] Emails verificados encontrados:")
        for addr in addresses:
            print(f"      - {addr.get('email')} ({addr.get('name', 'N/A')})")
        return addresses
    else:
        print(f"  [INFO] No se pudo obtener emails (Status: {response.status_code})")
        print(f"  [INFO] Usaremos el email por defecto de la cuenta HubSpot")
        return []

# ============================================================================
# STEP 6: Get account info
# ============================================================================

def get_account_info():
    """Get HubSpot account information"""
    print("\n[STEP 6] Obteniendo informacion de cuenta HubSpot...")

    url = f"{HUBSPOT_BASE_URL}/account-info/v3/details"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        portal_id = data.get("portalId")
        print(f"  [OK] Portal ID: {portal_id}")
        return data
    else:
        print(f"  [INFO] Status: {response.status_code}")
        return None

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 70)
    print("HUBSPOT CAMPAIGN SETUP - PHASE 1")
    print("ModelIt Teacher Outreach - Carlsbad USD")
    print("=" * 70)

    # Step 1: Get Carlsbad contacts
    contacts = get_carlsbad_contacts()

    if not contacts:
        print("\n[ERROR] No se encontraron contactos de Carlsbad")
        return

    contact_ids = [c["id"] for c in contacts]

    # Show sample
    print("\n  Muestra de contactos:")
    for c in contacts[:5]:
        props = c.get("properties", {})
        print(f"    - {props.get('firstname', '')} {props.get('lastname', '')} ({props.get('email', '')})")
    print(f"    ... y {len(contacts)-5} mas")

    # Step 2: Create static list
    list_id = create_static_list("Teachers K12 - Carlsbad")

    # Step 3: Add contacts to list
    if list_id:
        add_contacts_to_list(list_id, contact_ids)

    # Step 4: Add test contact
    test_contact_id = add_test_contact()

    # Add test contact to the list as well
    if list_id and test_contact_id:
        print("\n  Agregando contacto de prueba a la lista...")
        add_contacts_to_list(list_id, [test_contact_id])

    # Step 5: Check verified emails
    verified_emails = get_verified_emails()

    # Step 6: Get account info
    account_info = get_account_info()

    # Summary
    print("\n" + "=" * 70)
    print("RESUMEN - FASE 1 COMPLETADA")
    print("=" * 70)
    print(f"""
  Contactos Carlsbad: {len(contacts)}
  Lista creada: Teachers K12 - Carlsbad (ID: {list_id})
  Contacto de prueba: eilisierra@hootmail.com

  SIGUIENTE PASO:
  1. Ve a HubSpot > Marketing > Email
  2. Crea un nuevo email con el template del Email 1
  3. Envia prueba a eilisierra@hootmail.com
  4. Si todo OK, programa el envio a la lista

  URL de HubSpot:
  https://app-na2.hubspot.com/email/243912370/manage
""")
    print("=" * 70)

    return {
        "contacts_count": len(contacts),
        "list_id": list_id,
        "test_contact_id": test_contact_id
    }

if __name__ == "__main__":
    result = main()
