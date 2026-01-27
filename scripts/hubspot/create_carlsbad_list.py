"""
Create Static List in HubSpot for Carlsbad Teachers
Uses the correct HubSpot Lists API v3
"""

import sys
import requests
import os
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv("D:/ClaudeEili/.env")

HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")
HUBSPOT_BASE_URL = "https://api.hubapi.com"

HEADERS = {
    "Authorization": f"Bearer {HUBSPOT_API_KEY}",
    "Content-Type": "application/json"
}

def get_carlsbad_contact_ids():
    """Get all Carlsbad contact IDs"""
    print("[1/4] Buscando contactos de Carlsbad USD...")

    all_ids = []
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
            "properties": ["email"],
            "limit": 100
        }

        if after:
            payload["after"] = after

        response = requests.post(url, headers=HEADERS, json=payload)

        if response.status_code != 200:
            print(f"  [ERROR] {response.status_code}")
            break

        data = response.json()
        results = data.get("results", [])

        for contact in results:
            all_ids.append(contact["id"])

        paging = data.get("paging", {}).get("next", {})
        after = paging.get("after")

        if not after:
            break

    print(f"  [OK] {len(all_ids)} contactos encontrados")
    return all_ids

def list_existing_lists():
    """List existing contact lists"""
    print("\n[2/4] Verificando listas existentes...")

    url = f"{HUBSPOT_BASE_URL}/crm/v3/lists"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        lists = data.get("lists", [])
        if lists:
            print("  Listas existentes:")
            for lst in lists:
                print(f"    - {lst.get('name')} (ID: {lst.get('listId')}, Tamano: {lst.get('size', 0)})")
            return lists
        else:
            print("  [INFO] No hay listas existentes")
            return []
    else:
        print(f"  [INFO] Status: {response.status_code}")
        # Try alternative endpoint
        return check_lists_legacy()

def check_lists_legacy():
    """Try legacy lists endpoint"""
    url = f"{HUBSPOT_BASE_URL}/contacts/v1/lists"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        lists = data.get("lists", [])
        if lists:
            print("  Listas existentes (legacy):")
            for lst in lists[:5]:
                print(f"    - {lst.get('name')} (ID: {lst.get('listId')})")
            return lists
    return []

def create_list_v1(name, contact_ids):
    """Create list using legacy v1 API (more reliable)"""
    print(f"\n[3/4] Creando lista: {name}...")

    # First, create empty static list
    url = f"{HUBSPOT_BASE_URL}/contacts/v1/lists"

    payload = {
        "name": name,
        "dynamic": False  # Static list
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code == 200:
        data = response.json()
        list_id = data.get("listId")
        print(f"  [OK] Lista creada con ID: {list_id}")

        # Now add contacts to the list
        add_contacts_to_list_v1(list_id, contact_ids)
        return list_id

    elif response.status_code == 400:
        error = response.json()
        if "already exists" in str(error).lower():
            print("  [INFO] La lista ya existe, buscando...")
            existing = find_list_by_name_v1(name)
            if existing:
                print(f"  [OK] Lista encontrada con ID: {existing}")
                # Add contacts to existing list
                add_contacts_to_list_v1(existing, contact_ids)
                return existing
    else:
        print(f"  [ERROR] {response.status_code}: {response.text[:300]}")

    return None

def find_list_by_name_v1(name):
    """Find list by name using v1 API"""
    url = f"{HUBSPOT_BASE_URL}/contacts/v1/lists"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        for lst in data.get("lists", []):
            if lst.get("name") == name:
                return lst.get("listId")
    return None

def add_contacts_to_list_v1(list_id, contact_ids):
    """Add contacts to list using v1 API"""
    print(f"\n[4/4] Agregando {len(contact_ids)} contactos a la lista...")

    # v1 API accepts up to 500 VIDs per request
    batch_size = 500
    total_added = 0

    for i in range(0, len(contact_ids), batch_size):
        batch = contact_ids[i:i+batch_size]

        url = f"{HUBSPOT_BASE_URL}/contacts/v1/lists/{list_id}/add"

        # v1 API uses "vids" (Visitor IDs) which are the same as contact IDs
        payload = {
            "vids": [int(cid) for cid in batch]
        }

        response = requests.post(url, headers=HEADERS, json=payload)

        if response.status_code == 200:
            result = response.json()
            updated = result.get("updated", [])
            total_added += len(updated)
            print(f"  [OK] Batch: {len(updated)} agregados (total: {total_added})")
        else:
            print(f"  [ERROR] {response.status_code}: {response.text[:200]}")

    print(f"\n  Total contactos agregados: {total_added}")
    return total_added

def main():
    print("=" * 60)
    print("CREAR LISTA ESTATICA - TEACHERS K12 CARLSBAD")
    print("=" * 60)

    # Get contacts
    contact_ids = get_carlsbad_contact_ids()

    if not contact_ids:
        print("\n[ERROR] No se encontraron contactos")
        return

    # Check existing lists
    list_existing_lists()

    # Create list and add contacts
    list_id = create_list_v1("Teachers K12 - Carlsbad", contact_ids)

    # Final verification
    if list_id:
        print("\n" + "=" * 60)
        print("LISTA CREADA EXITOSAMENTE")
        print("=" * 60)
        print(f"""
  Nombre: Teachers K12 - Carlsbad
  ID: {list_id}
  Contactos: {len(contact_ids)}

  Ver lista en HubSpot:
  https://app-na2.hubspot.com/contacts/243912370/lists/{list_id}
""")
    else:
        print("\n[ERROR] No se pudo crear la lista")

if __name__ == "__main__":
    main()
