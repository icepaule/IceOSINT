# IceOSINT - Features

## Core Features

### 1. OSINT-Tools Integration

#### Ransomware Check
- **API:** ransomware.live
- **Funktion:** Prüft ob Domain in Ransomware-Leak-Listen erscheint
- **Coverage:** 100+ Ransomware-Gruppen weltweit
- **Datenpunkte:**
  - Victim name
  - Ransomware group
  - Discovery date
  - Description
  - Screenshot (wenn verfügbar)

#### DNS/WHOIS/SSL Analysis
- DNS Records (A, MX, NS, TXT, SPF)
- WHOIS Lookup (Registrar, Dates, Contacts)
- SSL Certificate Check (Issuer, Validity, SAN)

#### theHarvester
- E-Mail-Enumeration
- Host/Subdomain-Discovery
- Quellen: Google, Bing, LinkedIn

#### Sublist3r
- Subdomain-Enumeration
- Multi-Source (Google, Virustotal, DNSdumpster)

### 2. AI-Powered Analysis (Bedrock)

- **Model:** Claude Sonnet 4.5
- **Features:**
  - Automatische Risikobewertung
  - Identitätsverifizierung
  - Firmen-/Rechtsform-Analyse
  - Strukturierte Berichte
  - Handlungsempfehlungen

### 3. Domain Whitelist

**Erlaubte Domains:**
- mhb.de
- thesoc.de
- mpauli.de

**Verwaltung:**
- GUI-basiert (Admin-Panel)
- Dynamisch erweiterbar
- API-Endpoint: `/api/whitelist`

### 4. Web Dashboard

#### Request Management
- Submit new OSINT requests
- View request history
- Real-time status tracking
- Detail-Views per Request

#### Status Types
- `pending` - Wartet auf Verarbeitung
- `running` - Analyse läuft
- `completed` - Fertig
- `error` - Fehler aufgetreten

#### Export
- PDF-Export (geplant)
- JSON-Export
- Markdown-Reports

### 5. Security & Access Control

#### Authentik Integration
- AD-Gruppe: MHB-Mitglieder
- SSO via Authentik
- Role-Based Access Control

#### Guacamole Integration
- Zugriff via Guacamole
- Kein direkter Port-Zugriff nötig
- Session-Management

#### Audit Logging
- Alle Requests geloggt
- Requester-Tracking
- Timestamp-basiert

## Geplante Features

### Phase 2
- [ ] HaveIBeenPwned Integration
- [ ] Shodan API Integration
- [ ] Certificate Transparency Logs
- [ ] VirusTotal Integration

### Phase 3
- [ ] Automated Scheduling (Cron-Jobs)
- [ ] Alerting (E-Mail/Slack)
- [ ] Diff-Tracking (Änderungen über Zeit)
- [ ] Historical Reports

### Phase 4
- [ ] GraphQL API
- [ ] Webhooks
- [ ] Custom OSINT-Tool-Integration
- [ ] Machine Learning Risk-Scoring
