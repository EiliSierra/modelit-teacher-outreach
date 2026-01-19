#!/usr/bin/env python3
"""
Carlsbad Unified School District - Staff Directory Scraper
============================================================
Extracts staff information from Carlsbad USD schools.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import os
from datetime import datetime

# Configuration
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
DELAY = 2  # seconds between requests
TIMEOUT = 15  # request timeout

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
}

# Schools with their staff directory URLs
SCHOOLS = [
    ("Carlsbad High", "https://chs.carlsbadusd.net/3820_1"),
    ("Sage Creek High", "https://schs.carlsbadusd.net/5032_1"),
    ("Valley Middle", "https://vms.carlsbadusd.net/5297_1"),
    ("Calavera Hills Middle", "https://chms.carlsbadusd.net/134148_2"),
    ("Aviara Oaks Middle", "https://aoms.carlsbadusd.net/staff"),
    ("Hope Elementary", "https://hes.carlsbadusd.net/19712_2"),
    ("Poinsettia Elementary", "https://pes.carlsbadusd.net/19851_2"),
    ("Buena Vista Elementary", "https://bves.carlsbadusd.net/staff"),
    ("Jefferson Elementary", "https://jes.carlsbadusd.net/staff"),
    ("Kelly Elementary", "https://kes.carlsbadusd.net/staff"),
    ("Magnolia Elementary", "https://mes.carlsbadusd.net/staff"),
    ("Pacific Rim Elementary", "https://pres.carlsbadusd.net/staff"),
    ("Aviara Oaks Elementary", "https://aoes.carlsbadusd.net/staff"),
    ("Calavera Hills Elementary", "https://ches.carlsbadusd.net/staff"),
    ("Carlsbad Seaside Academy", "https://csa.carlsbadusd.net/staff"),
    ("Carlsbad Village Academy", "https://cva.carlsbadusd.net/staff"),
]

# Known Google Doc URLs for staff directories (found during research)
GOOGLE_DOC_URLS = {
    "Carlsbad High - Administration": "https://docs.google.com/document/d/1yfItJ7LkJPAM5Dos93XMN6itcFnI17jG8PT2tNnAu-4/preview",
}


def extract_emails_and_names(text):
    """Extract email addresses and associated names from text."""
    results = []

    # Pattern: Name followed by email
    pattern1 = r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)[,\s\-:]*(\d{3}[\.\-]\d{3}[\.\-]\d{4})?[,\s\-:]*([a-zA-Z0-9._%+-]+@carlsbadusd\.net)'

    for match in re.finditer(pattern1, text):
        name = match.group(1).strip()
        phone = match.group(2) or ""
        email = match.group(3)
        results.append({
            'Name': name,
            'Phone': phone,
            'Email': email
        })

    # Pattern: Just emails (will try to find name nearby)
    all_emails = re.findall(r'([a-zA-Z0-9._%+-]+@carlsbadusd\.net)', text)
    existing_emails = [r['Email'] for r in results]

    for email in all_emails:
        if email not in existing_emails:
            # Try to extract name from email
            name_part = email.split('@')[0]
            name_parts = re.split(r'[._]', name_part)
            name = ' '.join(p.capitalize() for p in name_parts if len(p) > 1)

            results.append({
                'Name': name,
                'Phone': "",
                'Email': email
            })

    return results


def fetch_url(url, session):
    """Fetch URL and follow redirects."""
    try:
        print(f"    Fetching: {url[:60]}...")
        response = session.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        return response
    except Exception as e:
        print(f"    Error: {e}")
        return None


def scrape_google_doc(url, session):
    """Scrape staff info from Google Doc."""
    staff = []
    response = fetch_url(url, session)
    if not response:
        return staff

    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    # Clean up text
    text = re.sub(r'\s+', ' ', text)

    # Find all carlsbadusd.net emails
    staff = extract_emails_and_names(text)

    return staff


def scrape_school_page(url, session):
    """Scrape staff info from school page."""
    staff = []
    response = fetch_url(url, session)
    if not response:
        return staff

    # Check if redirected to Google Docs
    if 'docs.google.com' in response.url:
        print(f"    -> Redirected to Google Doc")
        return scrape_google_doc(response.url, session)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Get all text and find emails
    text = soup.get_text()
    staff = extract_emails_and_names(text)

    # Also check for mailto links
    for link in soup.find_all('a', href=re.compile(r'^mailto:')):
        href = link.get('href', '')
        email = href.replace('mailto:', '').split('?')[0]
        if '@carlsbadusd.net' in email:
            existing = [s['Email'] for s in staff]
            if email not in existing:
                name = link.get_text().strip()
                if '@' in name or not name:
                    name_part = email.split('@')[0]
                    name = ' '.join(p.capitalize() for p in re.split(r'[._]', name_part))
                staff.append({
                    'Name': name,
                    'Phone': "",
                    'Email': email
                })

    # Look for links to sub-pages (Administration, Faculty, etc.)
    sub_links = []
    for link in soup.find_all('a', href=True):
        href = link.get('href', '')
        text = link.get_text().lower()
        if any(kw in text for kw in ['admin', 'faculty', 'teacher', 'counseling', 'staff']):
            if href.startswith('/'):
                base = '/'.join(url.split('/')[:3])
                href = base + href
            if href not in sub_links and 'carlsbadusd.net' in href:
                sub_links.append(href)

    # Check first 3 sub-links
    for sub_url in sub_links[:3]:
        print(f"    Checking sub-page...")
        time.sleep(1)
        sub_response = fetch_url(sub_url, session)
        if sub_response:
            if 'docs.google.com' in sub_response.url:
                sub_staff = scrape_google_doc(sub_response.url, session)
            else:
                sub_soup = BeautifulSoup(sub_response.text, 'html.parser')
                sub_staff = extract_emails_and_names(sub_soup.get_text())

            # Add new staff
            existing = [s['Email'] for s in staff]
            for s in sub_staff:
                if s['Email'] not in existing:
                    staff.append(s)

    return staff


def main():
    print("=" * 60)
    print("Carlsbad USD Staff Directory Scraper")
    print("=" * 60)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    session = requests.Session()
    all_staff = []

    # First, scrape known Google Docs
    print("[Known Google Doc Sources]")
    for name, url in GOOGLE_DOC_URLS.items():
        print(f"\n  {name}")
        staff = scrape_google_doc(url, session)
        for s in staff:
            s['School'] = name.split(' - ')[0]
            s['Position'] = name.split(' - ')[1] if ' - ' in name else ""
        all_staff.extend(staff)
        print(f"    Found: {len(staff)} staff")
        time.sleep(DELAY)

    # Then scrape school pages
    print("\n[School Websites]")
    for school_name, url in SCHOOLS:
        print(f"\n  {school_name}")
        staff = scrape_school_page(url, session)
        for s in staff:
            s['School'] = school_name
            if 'Position' not in s:
                s['Position'] = ""

        # Add only new staff (avoid duplicates)
        existing_emails = [s['Email'] for s in all_staff]
        new_staff = [s for s in staff if s['Email'] not in existing_emails]
        all_staff.extend(new_staff)

        print(f"    Found: {len(new_staff)} new staff")
        time.sleep(DELAY)

    print("\n" + "=" * 60)
    print(f"Total staff found: {len(all_staff)}")

    if all_staff:
        # Create DataFrame
        df = pd.DataFrame(all_staff)

        # Reorder columns
        columns = ['School', 'Name', 'Position', 'Email', 'Phone']
        df = df.reindex(columns=[c for c in columns if c in df.columns])

        # Sort
        df = df.sort_values(['School', 'Name'])

        # Save CSV
        csv_path = os.path.join(OUTPUT_DIR, 'carlsbad_staff_directory.csv')
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f"\nSaved: {csv_path}")

        # Save Excel
        excel_path = os.path.join(OUTPUT_DIR, 'carlsbad_staff_directory.xlsx')
        df.to_excel(excel_path, index=False, sheet_name='Staff')
        print(f"Saved: {excel_path}")

        # Summary
        print("\n" + "-" * 40)
        print("Summary by School:")
        for school in df['School'].unique():
            count = len(df[df['School'] == school])
            print(f"  {school}: {count}")
    else:
        print("\nNo staff found.")

    print("\n" + "=" * 60)
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
