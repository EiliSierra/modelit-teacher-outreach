# Plan de Campaña v2: Teacher Outreach ModelIt

## Repositorio GitHub

**Nombre**: `modelit-teacher-outreach`
**URL**: https://github.com/EiliSierra/modelit-teacher-outreach
**Ubicación local**: `D:/ClaudeEili/Proyectos/modelit-teacher-outreach/`
**Visibilidad**: Privado

### Estructura del repositorio

```
modelit-teacher-outreach/
├── README.md
├── .gitignore
├── requirements.txt
├── docs/
│   ├── campaign-plan.md         # Este archivo
│   ├── email_templates_v2.md    # 8 templates de email
│   ├── survey_questions.md      # Preguntas de encuesta
│   ├── lead_scoring.md          # Sistema de puntuación
│   └── implementation_checklist.md
├── scripts/
│   ├── hubspot/
│   │   ├── upload_carlsbad_to_hubspot.py
│   │   ├── hubspot_ucla_contacts.py
│   │   └── upload_to_hubspot.py
│   └── scrapers/
│       └── carlsbad_staff_scraper.py
└── data/
    └── example_contacts.csv
```

---

## Resumen Ejecutivo

**Objetivo**: Convertir 342 profesores de Carlsbad USD en compradores de ModelIt a través de una lección gratuita, feedback cualificado, y webinars.

**Cambio clave vs Plan Original**: Dar valor primero (lección gratuita) antes de pedir compromiso (webinar).

### Comparación de Funnels

**Plan Original (v1):**
```
Email → Webinar → TPT
```

**Plan Mejorado (v2):**
```
Lección Gratuita → Encuesta Feedback → Segmentación → Webinar/TPT
```

### Por qué funciona mejor

1. **Dar valor primero**: Lección completa gratis genera confianza
2. **Calificar leads**: La encuesta identifica quiénes están interesados
3. **Segmentar inteligentemente**: Hot leads → webinar, Cold → TPT directo
4. **Reducir fricción**: Solo invertimos tiempo en los más interesados
5. **Todo lleva a TPT**: Cada camino termina en la tienda

---

## Lección de Muestra

### "From Plug to Steam: How Energy Boils Water"

| Atributo | Valor |
|----------|-------|
| **Grado objetivo** | 8th Grade (adaptable 6-9) |
| **Tema** | Transferencia de energía |
| **Estándares** | NGSS PS3.A, PS3.B |
| **Plataforma** | ModelIt (Cell Collective) |
| **Valor en TPT** | $7.99 → **GRATIS como muestra** |
| **Duración** | ~45 minutos |

### Contenido del paquete

- Teacher Guide (PDF, 8 páginas)
- Student Activity Pack (printable + digital)
- PowerPoint slides (PPTM)
- Quick Start Guide (PDF)
- Teacher Walkthrough Video (MP4)
- Link directo a simulación en ModelIt

### Las 4 actividades

1. **Build and Label Components** - Identificar partes del sistema
2. **Connect Energy Flow** - Mostrar cómo fluye la energía
3. **Simulate with Energy OFF** - Probar sin energía
4. **Simulate with Energy ON** - Comparar resultados

### Ubicación de archivos

```
D:\Alexandria´s Design\ModelIt\8th Grade\From Plug to Steam How Energy Boils Water\
├── From Plug to Steam How Energy Boils Water.zip
├── Teacher Guide. From Plug to Steam How Energy Boils Water.pdf
├── Activity Pack. From Plug to Steam How Energy Boils Water.pdf
├── From Plug to Steam – How Energy Boils Water.pptm
├── READ FIRST — Quick Start for Teachers.pdf
└── Teacher Lesson Walkthrough. From Plug to Steam (1).mp4
```

---

## Funnel de Conversión Detallado

```
                    [Email 1: Lección Gratuita]
                              │
                    ┌─────────┴─────────┐
                    │                   │
              No descargó          Descargó ✓
                    │                   │
           [Email 2: Reminder]    (Esperar 7 días)
                    │                   │
                    └─────────┬─────────┘
                              │
                    [Email 3: Encuesta]
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
        4-5 ⭐              1-3 ⭐           Sin respuesta
        Hot Lead          Cold Lead         Unknown
            │                 │                 │
   [Email 4: Webinar]  [Email 5: TPT]    [Email 5: TPT]
            │                 │                 │
         Webinar              │                 │
            │                 │                 │
   [Email 6: Replay]          │                 │
            │                 │                 │
   [Email 7: Descuento]       │                 │
            │                 │                 │
            └─────────────────┴─────────────────┘
                              │
                    [Email 8: Final Follow-up]
                              │
                            TPT 🛒
```

---

## Secuencia de Emails

### Resumen de los 8 emails

| # | Nombre | Día | Audiencia | Objetivo |
|---|--------|-----|-----------|----------|
| 1 | Free Lesson | 1 | Todos | Ofrecer lección gratuita |
| 2 | Reminder | 3 | No descargaron | Segundo intento |
| 3 | Survey | 10 | Descargaron | Recopilar feedback |
| 4 | Webinar Invite | 12 | Hot leads (4-5⭐) | Invitar a webinar |
| 5 | More Resources | 12 | Cold/No response | Dirigir a TPT |
| 6 | Replay | 14 | Registrados webinar | Compartir replay + descuento |
| 7 | Discount Reminder | 17 | Asistieron webinar | Urgencia descuento |
| 8 | Final Follow-up | 21 | Todos engageados | Cierre + demo |

**Detalle completo de cada email:** Ver `docs/email_templates_v2.md`

---

## Encuesta de Feedback

### Preguntas clave

1. ¿Usaste la lección con tus estudiantes?
2. Rating general (1-5 estrellas)
3. ¿Qué te gustó más? (checkboxes)
4. ¿Qué podría mejorar? (texto libre)
5. ¿Qué grado enseñas?
6. ¿Qué temas te gustaría ver?
7. ¿Te interesa un webinar gratuito?

### Segmentación automática

| Respuesta | Clasificación | Acción |
|-----------|---------------|--------|
| 4-5 ⭐ + "Sí, webinar" | **Hot Lead** | Email 4 (webinar) |
| 3 ⭐ + "Quizás" | **Warm Lead** | Email 4 (soft) |
| 1-2 ⭐ o "No" | **Cold Lead** | Email 5 (TPT) |
| Sin respuesta | **Unknown** | Email 5 (TPT) |

**Detalle completo:** Ver `docs/survey_questions.md`

---

## Lead Scoring

### Puntuación de acciones

| Acción | Puntos |
|--------|--------|
| Abrió email | +5 |
| Click en email | +10 |
| Descargó lección gratuita | +20 |
| Completó encuesta | +15 |
| Rating 4-5 estrellas | +20 |
| Rating 1-2 estrellas | -10 |
| Registro webinar | +25 |
| Asistió webinar | +30 |
| Visitó TPT | +15 |
| Compró en TPT | +100 |

### Umbrales de acción

| Score | Segmento | Acción |
|-------|----------|--------|
| 0-15 | Frío | Solo nurture mensual |
| 16-40 | Tibio | Emails de valor + TPT |
| 41-70 | Caliente | Invitación webinar prioritaria |
| 71+ | Muy caliente | Contacto personal / oferta especial |

**Detalle completo:** Ver `docs/lead_scoring.md`

---

## Configuración Técnica

### HubSpot: Listas requeridas

| Lista | Criterio |
|-------|----------|
| Teachers K12 - Carlsbad | 342 contactos iniciales |
| Downloaded Free Lesson | click en download link |
| Survey - Hot Leads | rating ≥ 4 |
| Survey - Cold Leads | rating < 4 o sin respuesta |
| Webinar Registered | completó registro |
| Webinar Attended | asistió al webinar |
| TPT Visitors | click en link TPT |
| Purchased | confirmación compra |

### HubSpot: Propiedades personalizadas

| Propiedad | Tipo | Descripción |
|-----------|------|-------------|
| `downloaded_lesson` | Boolean | Descargó la lección |
| `download_date` | Date | Fecha de descarga |
| `survey_completed` | Boolean | Completó encuesta |
| `survey_rating` | Number | Rating 1-5 |
| `survey_webinar_interest` | Dropdown | yes/maybe/no |
| `webinar_registered` | Boolean | Se registró |
| `webinar_attended` | Boolean | Asistió |
| `tpt_clicked` | Boolean | Visitó TPT |
| `purchased_tpt` | Boolean | Compró |
| `lead_score` | Number | Puntuación calculada |

### Workflows de automatización

**Workflow 1: Email Sequence**
```
Nuevo contacto → Email 1 → Esperar 3 días →
  SI no descargó → Email 2
  SI descargó → Esperar 7 días → Email 3 (Survey)
```

**Workflow 2: Survey Segmentation**
```
Survey completada →
  SI rating ≥ 4 → Add to "Hot Leads" → Email 4
  SI rating < 4 → Add to "Cold Leads" → Email 5
  SI no response (5 días) → Add to "Cold Leads" → Email 5
```

**Workflow 3: Post-Webinar**
```
Webinar terminado → Email 6 (replay) →
  Esperar 3 días → SI no click TPT → Email 7 (reminder)
  Esperar 4 días → Email 8 (final)
```

---

## Webinar

### Detalles

| Aspecto | Valor |
|---------|-------|
| Título | "Teaching Systems Thinking with ModelIt" |
| Duración | 45 min + 15 min Q&A |
| Plataforma | Zoom |
| Horario sugerido | Martes/Miércoles, 4 PM PST |
| Capacidad | 100 personas |

### Agenda

| Tiempo | Contenido |
|--------|-----------|
| 0-5 min | Intro y presentación |
| 5-20 min | Demo de 3 lecciones ModelIt |
| 20-30 min | Cómo integrar en curriculum |
| 30-40 min | Tips de implementación |
| 40-45 min | Oferta especial + CTA |
| 45-60 min | Q&A |

### Beneficios para asistentes

- Código descuento 20% (WEBINAR20)
- Acceso anticipado a nuevas lecciones
- PDF de slides del webinar
- Link al replay

---

## Métricas de Éxito

### KPIs objetivo

| Métrica | Objetivo | Cálculo |
|---------|----------|---------|
| Tasa descarga lección | >30% | Descargas / Emails enviados |
| Tasa respuesta encuesta | >40% | Respuestas / Descargas |
| Rating promedio | >4.0 | Suma ratings / Total respuestas |
| Registro webinar | >20% | Registros / Hot leads |
| Asistencia webinar | >50% | Asistentes / Registrados |
| Visitas TPT | >25% | Visitantes / Total contactados |
| Conversión compra | >5% | Compradores / Visitantes TPT |

### Proyección

```
342 contactos iniciales
├── ~100 descargan lección (30%)
├── ~40 completan encuesta (40%)
├── ~16 hot leads (40% de encuestas)
├── ~8 asisten webinar (50%)
├── ~85 visitan TPT (25% de total)
└── ~4-5 compras primer mes (5%)
```

---

## Calendario de Implementación

### Fase 1: Preparación (Día 1-2)

- [ ] Subir lección a hosting (Google Drive/Dropbox)
- [ ] Crear encuesta en Google Forms
- [ ] Crear templates de email en HubSpot
- [ ] Configurar propiedades personalizadas
- [ ] Crear listas de segmentación

### Fase 2: Configuración Técnica (Día 3-4)

- [ ] Configurar workflows en HubSpot
- [ ] Conectar Google Forms → HubSpot (Zapier)
- [ ] Configurar UTM tracking
- [ ] Pruebas internas (email a ti mismo)
- [ ] Verificar links y descarga

### Fase 3: Lanzamiento (Día 5+)

| Día | Acción |
|-----|--------|
| 1 | Enviar Email 1 a 342 contactos |
| 3 | Enviar Email 2 a no-descargadores |
| 10 | Enviar Email 3 (encuesta) a descargadores |
| 12 | Procesar encuestas → Email 4 o 5 |
| TBD | Ejecutar webinar |
| +1 | Email 6 (replay + descuento) |
| +4 | Email 7 (reminder descuento) |
| +8 | Email 8 (seguimiento final) |

### Fase 4: Análisis (Día 30+)

- [ ] Revisar métricas vs objetivos
- [ ] Identificar emails con bajo rendimiento
- [ ] Analizar feedback de encuestas
- [ ] Planificar optimizaciones para siguiente mes

---

## Verificación Pre-Lanzamiento

### Checklist técnico

- [ ] ZIP de lección subido y link funcionando
- [ ] Encuesta Google Forms creada y probada
- [ ] Emails configurados en HubSpot
- [ ] Workflows activados
- [ ] Segmentación automática funcionando
- [ ] Email de prueba enviado a ti mismo
- [ ] Links UTM verificados
- [ ] Webinar programado en Zoom

### Checklist de contenido

- [ ] Subject lines A/B configurados
- [ ] Personalización {{firstname}} funciona
- [ ] CTA buttons visibles en mobile
- [ ] Unsubscribe link presente
- [ ] Firma de email correcta
- [ ] Links TPT con UTM

---

## Recursos Relacionados

| Documento | Ubicación | Descripción |
|-----------|-----------|-------------|
| Email Templates v2 | `docs/email_templates_v2.md` | 8 templates completos |
| Survey Questions | `docs/survey_questions.md` | Preguntas de encuesta |
| Lead Scoring | `docs/lead_scoring.md` | Sistema de puntuación |
| Implementation Checklist | `docs/implementation_checklist.md` | Tareas paso a paso |
| Carlsbad Contacts | `data/` | Datos de contactos |
| HubSpot Scripts | `scripts/hubspot/` | Automatización |

---

## Contacto y Soporte

**Repositorio GitHub:** https://github.com/EiliSierra/modelit-teacher-outreach

**TPT Store:** https://www.teacherspayteachers.com/store/modelit

---

*Última actualización: Enero 2026*
