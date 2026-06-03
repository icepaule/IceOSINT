# IceOSINT API Documentation

Base URL: `https://iceosint.thesoc.de/api`

## Authentication

All requests require Authentik authentication via Traefik middleware.

## Endpoints

### POST /api/requests

Create new OSINT request.

**Request Body:**
```json
{
  "email": "user@mhb.de",
  "domain": "example.com",
  "questions": "Is this our customer? Any ransomware incidents?"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "email": "user@mhb.de",
  "domain": "example.com",
  "questions": "...",
  "status": "pending",
  "requester": "user@mhb.de",
  "created_at": "2026-06-03T14:00:00Z",
  "completed_at": null
}
```

**Errors:**
- `403 Forbidden` - Domain not whitelisted
- `422 Unprocessable Entity` - Invalid input

### GET /api/requests

List all requests (latest 100).

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "email": "user@mhb.de",
    "domain": "example.com",
    "status": "completed",
    "requester": "user@mhb.de",
    "created_at": "2026-06-03T14:00:00Z",
    "completed_at": "2026-06-03T14:05:00Z"
  }
]
```

### GET /api/requests/{id}

Get request details.

**Response:** `200 OK`
```json
{
  "id": 1,
  "email": "user@mhb.de",
  "domain": "example.com",
  "questions": "...",
  "status": "completed",
  "requester": "user@mhb.de",
  "created_at": "2026-06-03T14:00:00Z",
  "completed_at": "2026-06-03T14:05:00Z",
  "results": [
    {
      "id": 1,
      "data": {...},
      "report_text": "# OSINT Report\n\n...",
      "created_at": "2026-06-03T14:05:00Z"
    }
  ]
}
```

### GET /api/whitelist

List whitelisted domains.

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "domain": "mhb.de",
    "active": true,
    "created_at": "2026-06-03T10:00:00Z"
  }
]
```

### POST /api/whitelist (Admin only)

Add domain to whitelist.

**Request Body:**
```json
{
  "domain": "newdomain.com"
}
```

**Response:** `201 Created`

## Rate Limiting

- 100 requests/hour per user
- 1000 requests/day per domain
