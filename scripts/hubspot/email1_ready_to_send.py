"""
Email 1 - Ready to Send
========================
Generates the HTML email template and provides HubSpot instructions.
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

# Email configuration
EMAIL_CONFIG = {
    "subject_a": "Free lesson: Your students will simulate boiling water",
    "subject_b": "A gift for your science class — view it free",
    "from_name": "ModelIt Team",
    "lesson_link": "https://drive.google.com/file/d/1x5cygfmfAQdpsGzCi-ksZ3cX-kdJ7bHc/view",
    "utm_params": "?utm_source=hubspot&utm_medium=email&utm_campaign=free_lesson_jan2026&utm_content=email1_free_lesson"
}

LESSON_LINK = "https://drive.google.com/file/d/1x5cygfmfAQdpsGzCi-ksZ3cX-kdJ7bHc/view"
UTM_PARAMS = "?utm_source=hubspot&utm_medium=email&utm_campaign=free_lesson_jan2026&utm_content=email1_free_lesson"

EMAIL_HTML = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="font-family: Arial, Helvetica, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">

    <div style="padding: 20px 0;">
        <p>Hi {{{{ contact.firstname | default: "there" }}}},</p>

        <p>Have you ever wished your students could SEE how energy flows through a system — not just read about it?</p>

        <p>We created a free lesson called <strong>"From Plug to Steam: How Energy Boils Water"</strong> that lets students build and test a digital model of energy transfer.</p>

        <div style="background: #f5f5f5; padding: 15px; border-radius: 8px; margin: 20px 0;">
            <p style="margin: 5px 0;"><strong>Simple 45-minute lesson flow:</strong></p>
            <p style="margin: 5px 0;">→ <strong>Launch</strong> (5 min): Introduce the energy system</p>
            <p style="margin: 5px 0;">→ <strong>Build</strong> (15 min): Connect components with arrows</p>
            <p style="margin: 5px 0;">→ <strong>Simulate</strong> (15 min): Test with energy ON vs OFF</p>
            <p style="margin: 5px 0;">→ <strong>Discuss</strong> (10 min): "Because ___, then ___"</p>
        </div>

        <p><strong>Your students will:</strong></p>
        <p><span style="color: #2563EB;">✓</span> Identify components of an energy system</p>
        <p><span style="color: #2563EB;">✓</span> Connect cause-and-effect relationships</p>
        <p><span style="color: #2563EB;">✓</span> Run simulations to test "what if" scenarios</p>
        <p><span style="color: #2563EB;">✓</span> Practice explaining: "Because energy enters, then temperature rises"</p>

        <p><span style="color: #2563EB;">✓</span> <strong>Aligned with California NGSS standards</strong> (PS3.A, PS3.B)<br>
        <span style="color: #2563EB;">✓</span> Perfect for 8th grade physical science</p>

        <p style="text-align: center;">
            <a href="{LESSON_LINK}{UTM_PARAMS}" style="display: inline-block; background: #2563EB; color: white; padding: 14px 28px; text-decoration: none; border-radius: 6px; font-weight: bold; margin: 20px 0;">View Free Lesson</a>
        </p>

        <p><strong>What's included:</strong></p>
        <p>• Teacher Guide with step-by-step instructions<br>
        • Student Activity Pack (printable + digital)<br>
        • PowerPoint slides<br>
        • Video walkthrough for you<br>
        • Direct link to the simulation — no student accounts needed</p>

        <p>View it anytime — it's on Google Drive, no download required.</p>

        <p>Best,<br>
        <strong>The ModelIt Team</strong></p>

        <p style="font-style: italic; color: #666; margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee;">P.S. This lesson introduces systems thinking—the foundation of all our ModelIt resources. Over 150 teachers have already tried it!</p>
    </div>

    <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 12px; color: #666; text-align: center;">
        <p>Discovery Collective | San Diego, CA</p>
        <p><a href="{{{{ unsubscribe_link }}}}">Unsubscribe</a> | <a href="{{{{ subscription_preferences_link }}}}">Manage Preferences</a></p>
    </div>
</body>
</html>
"""

def verify_setup():
    """Verify HubSpot configuration"""
    print("=" * 70)
    print("VERIFICACION DE CONFIGURACION - EMAIL 1")
    print("ModelIt Teacher Outreach")
    print("=" * 70)

    # Check list
    print("\n[1/3] Verificando lista...")
    url = f"{HUBSPOT_BASE_URL}/contacts/v1/lists/2"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        list_name = data.get("name")
        size = data.get("metaData", {}).get("size", 0)
        print(f"  [OK] Lista: {list_name}")
        print(f"  [OK] Contactos en lista: {size}")
    else:
        print(f"  [WARN] No se pudo verificar la lista")

    # Check test contact
    print("\n[2/3] Verificando contacto de prueba...")
    url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/contacts/search"
    payload = {
        "filterGroups": [{
            "filters": [{
                "propertyName": "email",
                "operator": "EQ",
                "value": "eilisierra@hootmail.com"
            }]
        }],
        "properties": ["email", "firstname", "lastname"]
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code == 200:
        data = response.json()
        if data.get("total", 0) > 0:
            contact = data["results"][0]
            print(f"  [OK] Contacto: eilisierra@hootmail.com (ID: {contact['id']})")
        else:
            print(f"  [WARN] Contacto de prueba no encontrado")
    else:
        print(f"  [ERROR] {response.status_code}")

    # Check Marketing Email capability
    print("\n[3/3] Verificando permisos de Marketing Email...")
    url = f"{HUBSPOT_BASE_URL}/marketing/v3/emails"
    response = requests.get(url, headers=HEADERS, params={"limit": 1})

    if response.status_code == 200:
        print(f"  [OK] API de Marketing Email accesible")
    elif response.status_code == 403:
        print(f"  [INFO] Marketing Hub requerido para crear emails via API")
        print(f"  [INFO] Usar la interfaz web de HubSpot para crear el email")
    else:
        print(f"  [INFO] Status: {response.status_code}")

    return True

def save_html_template():
    """Save the HTML template to a file"""
    output_path = "D:/ClaudeEili/Proyectos/modelit-teacher-outreach/templates/email1_free_lesson.html"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(EMAIL_HTML)

    print(f"\n[OK] Template HTML guardado en:")
    print(f"     {output_path}")

    return output_path

def main():
    verify_setup()

    print("\n" + "=" * 70)
    print("TEMPLATE DEL EMAIL 1")
    print("=" * 70)

    html_path = save_html_template()

    print(f"""
CONFIGURACION DEL EMAIL:
========================
  Subject Line A: {EMAIL_CONFIG['subject_a']}
  Subject Line B: {EMAIL_CONFIG['subject_b']}

  From Name: {EMAIL_CONFIG['from_name']}
  Reply-to: (usar email de cuenta HubSpot)

  Lista destino: Teachers K12 - Carlsbad (ID: 2)

  CTA Link:
  {EMAIL_CONFIG['lesson_link']}{EMAIL_CONFIG['utm_params']}

INSTRUCCIONES PARA HUBSPOT:
===========================
1. Ir a: https://app-na2.hubspot.com/email/243912370/manage

2. Click "Create email" > "Regular"

3. Elegir plantilla "Simple" o "Blank"

4. Copiar el contenido del email desde:
   {html_path}

5. Configurar:
   - Subject: {EMAIL_CONFIG['subject_a']}
   - From name: {EMAIL_CONFIG['from_name']}
   - Lista: Teachers K12 - Carlsbad

6. ANTES DE ENVIAR A TODOS:
   - Enviar prueba a: eilisierra@hootmail.com
   - Verificar que el email se ve bien

7. Si todo OK, programar envio:
   - Martes o Miercoles, 10 AM PST (recomendado)
""")

    print("=" * 70)
    print("CONTENIDO DEL EMAIL (TEXTO PLANO)")
    print("=" * 70)
    print("""
Hi {{ contact.firstname | default: "there" }},

Have you ever wished your students could SEE how energy flows
through a system — not just read about it?

We created a free lesson called "From Plug to Steam: How Energy
Boils Water" that lets students build and test a digital model
of energy transfer.

**Simple 45-minute lesson flow:**
→ Launch (5 min): Introduce the energy system
→ Build (15 min): Connect components with arrows
→ Simulate (15 min): Test with energy ON vs OFF
→ Discuss (10 min): "Because ___, then ___"

Your students will:
✓ Identify components of an energy system
✓ Connect cause-and-effect relationships
✓ Run simulations to test "what if" scenarios
✓ Practice explaining: "Because energy enters, then temperature rises"

✓ Aligned with California NGSS standards (PS3.A, PS3.B)
✓ Perfect for 8th grade physical science

[View Free Lesson]
https://drive.google.com/file/d/1x5cygfmfAQdpsGzCi-ksZ3cX-kdJ7bHc/view?utm_source=hubspot&utm_medium=email&utm_campaign=free_lesson_jan2026&utm_content=email1_free_lesson

What's included:
• Teacher Guide with step-by-step instructions
• Student Activity Pack (printable + digital)
• PowerPoint slides
• Video walkthrough for you
• Direct link to the simulation — no student accounts needed

View it anytime — it's on Google Drive, no download required.

Best,
The ModelIt Team

P.S. This lesson introduces systems thinking—the foundation of
all our ModelIt resources. Over 150 teachers have already tried it!
""")

    return True

if __name__ == "__main__":
    main()
