# Plan de Campaña: Outreach Teachers K12 - ModelIt

## Repositorio GitHub

**Nombre**: `modelit-k12-campaign`
**Ubicación local**: `D:/ClaudeEili/GitHub-Repos/modelit-k12-campaign/`
**Visibilidad**: Privado

### Estructura del repositorio
```
modelit-k12-campaign/
├── README.md                    # Documentación del proyecto
├── .env.example                 # Variables de entorno (sin secrets)
├── .gitignore                   # Excluir .env, node_modules, etc.
├── docs/
│   ├── campaign-plan.md         # Este plan
│   ├── email-templates.md       # Contenido de los emails
│   └── metrics-tracking.md      # KPIs y métricas
├── scripts/
│   ├── hubspot_setup.py         # Configurar HubSpot (listas, propiedades)
│   ├── email_campaign.py        # Enviar emails via SendGrid
│   ├── campaign_tracker.py      # Obtener métricas
│   └── sync_zoom_hubspot.py     # Sincronizar asistentes Zoom → HubSpot
├── workflows/
│   ├── email_sequence.json      # Workflow n8n: secuencia de emails
│   ├── post_webinar.json        # Workflow n8n: post-webinar
│   └── interest_tracking.json   # Workflow n8n: tracking de interés
├── templates/
│   ├── email_1_intro.html       # Template Email 1
│   ├── email_2_reminder.html    # Template Email 2
│   └── ...                      # Resto de templates
└── assets/
    ├── modelit_logo.png         # Logo para emails
    └── video_thumbnail.png      # Thumbnail del video demo
```

---

## Resumen Ejecutivo

**Objetivo**: Convertir 365 profesores K12 (Teachers K12 - Carlsbad USD) en clientes de ModelIt a través de webinars mensuales y ventas en TPT.

**Funnel de conversión**:
```
Email inicial → Registro Webinar → Asistencia → Explorar TPT → Compra
```

**Herramientas**: HubSpot + n8n + SendGrid + Zoom

---

## Fase 1: Configuración Base (Día 1-2)

### 1.1 Segmentación en HubSpot
- Crear lista "Teachers K12 - Cold" (365 contactos)
- Crear lista "Webinar Registrados"
- Crear lista "Webinar Asistieron"
- Crear lista "TPT Visitors"
- Crear lista "Compradores"

### 1.2 Propiedades personalizadas en HubSpot
```
- campaign_status: cold | invited | registered | attended | visited_tpt | purchased
- webinar_date: fecha del webinar al que se registró
- interest_score: 0-100 (calculado automáticamente)
```

### 1.3 Crear Video Corto (2-3 min)
- Intro a ModelIt
- Qué problema resuelve
- Preview de una lección
- CTA: "Únete al webinar gratuito"

---

## Fase 2: Secuencia de Emails (5 emails)

### Email 1: Introducción (Día 1)
**Subject**: "Una nueva forma de enseñar ciencias que tus estudiantes van a amar"
**Contenido**:
- Problema: Enseñar pensamiento sistémico es difícil
- Solución: ModelIt (video de 2 min embebido)
- CTA: "Regístrate al webinar gratuito [FECHA]"
- Link: Formulario de registro

### Email 2: Recordatorio (Día 4)
**Subject**: "¿Viste el video? Quedan X lugares para el webinar"
**Contenido**:
- Para los que NO abrieron Email 1
- Resumen de beneficios
- Testimonial corto
- CTA: Registro webinar

### Email 3: Valor adicional (Día 7)
**Subject**: "Recurso gratuito: Guía de Pensamiento Sistémico para tu clase"
**Contenido**:
- Lead magnet: PDF descargable
- Preview de lo que verán en el webinar
- CTA: Registro webinar

### Email 4: Urgencia (Día 10)
**Subject**: "El webinar es en 3 días - ¿Te registraste?"
**Contenido**:
- Solo para NO registrados
- FOMO: "87 profesores ya se registraron"
- Último chance
- CTA: Registro webinar

### Email 5: Día del webinar (Día 13)
**Subject**: "Hoy es el día - Link para unirte al webinar"
**Contenido**:
- Solo para REGISTRADOS
- Link de Zoom
- Agenda del webinar
- Bonus por asistir

---

## Fase 3: Secuencia Post-Webinar (3 emails)

### Email 6: Gracias + Replay (Día 14)
**Subject**: "Gracias por asistir - Aquí tu replay + recursos"
**Contenido**:
- Link al replay (para todos los registrados)
- Slides PDF
- CTA: "Explora las lecciones en TPT"
- Link: https://www.teacherspayteachers.com/store/modelit

### Email 7: Oferta especial (Día 17)
**Subject**: "Oferta exclusiva para asistentes del webinar"
**Contenido**:
- Solo para los que ASISTIERON
- Descuento especial en TPT (si aplica)
- Bundle destacado
- CTA: Comprar en TPT

### Email 8: Seguimiento final (Día 21)
**Subject**: "¿Tienes preguntas sobre ModelIt?"
**Contenido**:
- Para registrados que NO compraron
- FAQ
- Ofrecer demo 1-on-1
- CTA: Agendar llamada o comprar en TPT

---

## Fase 4: Lead Scoring Automático

### Puntuación de interés (0-100)

| Acción | Puntos |
|--------|--------|
| Abrió email | +5 |
| Click en email | +10 |
| Registró webinar | +25 |
| Asistió webinar | +30 |
| Visitó TPT (tracking link) | +15 |
| Compró en TPT | +100 |

### Segmentación por score

| Score | Clasificación | Acción |
|-------|---------------|--------|
| 0-10 | Frío | Mantener en nurture |
| 11-30 | Tibio | Email adicional personalizado |
| 31-60 | Caliente | Prioridad para follow-up |
| 61+ | Muy caliente | Contacto personal/llamada |

---

## Fase 5: Automatización n8n

### Workflow 1: Email Sequence Automation
```
Trigger: Nuevo contacto en lista "Teachers K12 - Cold"
↓
Esperar 0 días → Enviar Email 1
↓
Esperar 3 días → Verificar si abrió
  → No abrió: Enviar Email 2
  → Sí abrió: Esperar
↓
Esperar 3 días → Enviar Email 3
↓
Verificar si registrado webinar
  → No: Enviar Email 4
  → Sí: Agregar a lista "Webinar Registrados"
↓
Día del webinar → Enviar Email 5 (solo registrados)
```

### Workflow 2: Post-Webinar Sequence
```
Trigger: Webinar completado (webhook de Zoom)
↓
Obtener lista de asistentes de Zoom
↓
Actualizar HubSpot: marcar como "attended"
↓
Esperar 1 día → Enviar Email 6 (replay)
↓
Esperar 3 días → Verificar si visitó TPT
  → Sí visitó: Enviar Email 7 (oferta)
  → No visitó: Enviar reminder con link TPT
↓
Esperar 4 días → Enviar Email 8 (seguimiento final)
```

### Workflow 3: Interest Tracking
```
Trigger: Click en link de TPT (UTM tracking)
↓
Actualizar HubSpot: +15 puntos
↓
Mover a lista "TPT Visitors"
↓
Si score > 60: Notificar por Slack/Email para follow-up manual
```

---

## Fase 6: Tracking con UTM Parameters

### Links con tracking
```
TPT Store:
https://www.teacherspayteachers.com/store/modelit?utm_source=hubspot&utm_medium=email&utm_campaign=teachers_k12_jan2026

Webinar Registration:
[ZOOM_LINK]?utm_source=hubspot&utm_medium=email&utm_campaign=webinar_jan2026

Video Demo:
[VIDEO_LINK]?utm_source=hubspot&utm_medium=email&utm_campaign=intro_video
```

---

## Fase 7: Calendario de Webinars

### Propuesta: Webinar mensual
- **Primer webinar**: Última semana de Enero 2026
- **Horario sugerido**: Martes o Miércoles, 4:00 PM PST
- **Duración**: 45 min + 15 min Q&A
- **Plataforma**: Zoom (integrado con n8n)

### Agenda del webinar
1. (5 min) Intro y problema
2. (15 min) Demo de ModelIt
3. (10 min) Caso de éxito / testimonial
4. (10 min) Cómo empezar + recursos
5. (5 min) Oferta especial
6. (15 min) Q&A

---

## Archivos a Crear

| Archivo | Ubicación | Descripción |
|---------|-----------|-------------|
| `email_templates.py` | `D:/ClaudeEili/Scripts/` | Templates HTML de los 8 emails |
| `hubspot_setup.py` | `D:/ClaudeEili/Scripts/` | Crear listas y propiedades |
| `n8n_email_workflow.json` | `D:/ClaudeEili/Scripts/` | Workflow de email sequence |
| `n8n_postwebinar_workflow.json` | `D:/ClaudeEili/Scripts/` | Workflow post-webinar |
| `campaign_tracker.py` | `D:/ClaudeEili/Scripts/` | Script para ver métricas |

---

## Métricas de Éxito

### KPIs objetivo (primer mes)

| Métrica | Objetivo | Cálculo |
|---------|----------|---------|
| Open rate emails | >25% | Aperturas / Enviados |
| Click rate | >5% | Clicks / Aperturas |
| Registro webinar | >10% | Registros / Contactados |
| Asistencia webinar | >40% | Asistentes / Registrados |
| Visitas TPT | >20% | Visitantes / Asistentes |
| Conversión compra | >5% | Compradores / Visitantes |

### Proyección
- 365 contactos iniciales
- ~90 registros webinar (25%)
- ~36 asistentes (40%)
- ~7 visitas TPT (20%)
- ~1-2 compras primer mes

**Nota**: Las tasas mejoran con optimización en meses siguientes.

---

## Verificación del Plan

### Para probar que funciona:
1. Ejecutar script de setup de HubSpot → Verificar listas creadas
2. Enviar email de prueba a ti mismo → Verificar formato y links
3. Registrar 5 contactos de prueba → Verificar workflow n8n
4. Click en link TPT → Verificar tracking UTM funciona
5. Revisar dashboard de métricas → Confirmar datos se registran

---

## Resumen de Implementación

**Día 1**: Setup HubSpot (listas, propiedades)
**Día 2**: Crear video demo + templates de email
**Día 3**: Configurar workflows en n8n
**Día 4**: Pruebas internas
**Día 5**: Programar webinar en Zoom
**Día 6**: Lanzar campaña (Email 1 a todos)
**Día 7-21**: Automatización maneja todo
**Día 22+**: Revisar métricas, optimizar, repetir
