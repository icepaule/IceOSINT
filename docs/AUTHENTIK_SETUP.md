# Authentik Setup für IceOSINT

**Zugriff nur für Mitglieder der AD-Gruppe `GRP_MHB_Members`**

---

## 1️⃣ Provider erstellen (OAuth2/OpenID)

**Authentik Admin UI → Applications → Providers → Create**

| Feld | Wert |
|------|------|
| **Name** | `IceOSINT Provider` |
| **Type** | `OAuth2/OpenID Provider` |
| **Authorization flow** | `default-provider-authorization-implicit-consent` |
| **Client type** | `Confidential` |
| **Client ID** | `iceosint-client` (automatisch) |
| **Client Secret** | **(generiert - notieren!)** |
| **Redirect URIs** | `https://iceosint.thesoc.de/outpost.goauthentik.io/callback` |
| **Signing Key** | `authentik Self-signed Certificate` |
| **Subject mode** | `Based on the User's UPN` |

**→ Speichern**

---

## 2️⃣ Application erstellen

**Authentik Admin UI → Applications → Create**

| Feld | Wert |
|------|------|
| **Name** | `IceOSINT` |
| **Slug** | `iceosint` |
| **Provider** | `IceOSINT Provider` (aus Schritt 1) |
| **Launch URL** | `https://iceosint.thesoc.de` |
| **Open in new tab** | ✓ |
| **Icon** | (optional) |

**→ Speichern**

---

## 3️⃣ Policy Binding für MHB-Gruppe

**Authentik Admin UI → Applications → IceOSINT → Bindings → Create Binding**

| Feld | Wert |
|------|------|
| **Policy / Group / User** | `GRP_MHB_Members` |
| **Order** | `10` |
| **Enabled** | ✓ |
| **Negate result** | ✗ |
| **Timeout** | `30` |

**Alternativ (falls Gruppe anders heißt):**
- `MHB-Mitglieder`
- `Domain Users` (falls alle MHB-Mitarbeiter)
- `APP-IceOSINT-Users` (dedizierte Gruppe)

**→ Speichern**

---

## 4️⃣ Outpost prüfen

**Authentik Admin UI → Outposts → Embedded Outpost**

- **Type:** `Proxy`
- **Applications:** `IceOSINT` muss in der Liste sein
- **Status:** ✓ Healthy

Falls nicht vorhanden:

**Create Outpost:**
- **Name:** `IceOSINT Outpost`
- **Type:** `Proxy`
- **Integration:** `Local Docker connection`
- **Applications:** `IceOSINT` auswählen

---

## 5️⃣ Test

### DNS-Check:
```bash
nslookup iceosint.thesoc.de
# Sollte: 63.180.189.205
```

### Browser-Test:
1. **https://iceosint.thesoc.de** öffnen
2. → Weiterleitung zu Authentik Login
3. Login mit **MHB-AD-Account**
4. → IceOSINT Dashboard erscheint

### Negativ-Test (ohne AD-Gruppe):
- Login mit User **ohne** `GRP_MHB_Members` Membership
- Erwartete Fehlermeldung: *"You don't have access to this application"*

---

## 🔧 Troubleshooting

### "Forbidden" / "Access Denied"
**Prüfe:**
```bash
# Auf itso-prod-traefik:
docker logs authentik-server | grep iceosint
docker logs traefik | grep iceosint
```

### "Bad Gateway 502"
**Prüfe Backend-Erreichbarkeit:**
```bash
# Von itso-prod-traefik aus:
curl -v http://10.128.134.30/health
# Sollte: {"status":"healthy","version":"1.0.0"}
```

### Let's Encrypt Zertifikat nicht ausgestellt
**Prüfe Traefik Logs:**
```bash
docker logs traefik 2>&1 | grep -i "iceosint.thesoc.de"
# Sollte: "certificate obtained for domain iceosint.thesoc.de"
```

---

## 📋 Checkliste

- [ ] Provider erstellt
- [ ] Client Secret notiert
- [ ] Application erstellt
- [ ] AD-Gruppe `GRP_MHB_Members` gebunden
- [ ] Outpost läuft und ist healthy
- [ ] DNS zeigt auf 63.180.189.205
- [ ] HTTPS-Zertifikat ausgestellt
- [ ] Login mit MHB-User erfolgreich
- [ ] Negativ-Test bestanden (Nicht-Mitglied blockiert)

---

**Status:** Traefik-Routing & Authentik-Middleware deployed ✅  
**Nächster Schritt:** Provider & Application in Authentik UI erstellen
