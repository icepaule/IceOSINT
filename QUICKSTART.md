# IceOSINT Quick Start

## Status: MVP in Development

Die komplette Struktur wird schrittweise erstellt.

## Aktuell verfügbar:

✅ Docker Compose Setup
✅ Backend-Struktur (FastAPI)
✅ Frontend-Struktur (React)  
✅ PostgreSQL Schema
✅ .env.example Templates

## Nächste Schritte:

Ich erstelle jetzt **via SSM direkt auf Int-2**:
1. Alle Backend-Services (OSINT-Tools)
2. Frontend-Dashboard (React)
3. Database-Migrations
4. Deployment-Scripts

## Deploy auf Int-2:

```bash
# Auf Int-2
cd /opt
git clone https://github.com/icepaule/IceOSINT.git
cd IceOSINT
cp .env.example .env
# Edit .env
docker-compose up -d
```

## Entwicklung läuft...

Claude Code erstellt das System parallel zu diesem README.
