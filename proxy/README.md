# Ajax Secure Proxy

Proxy sécurisé pour l'intégration Ajax Home Assistant. Ce proxy permet aux utilisateurs de se connecter sans avoir besoin de leur propre clé API.

## Architecture

```
[Home Assistant] <---> [Ce Proxy] <---> [Ajax API]
                           |
                           +---> [SSE Events] ---> [Home Assistant]
```

## Fonctionnalités

- **Injection de clé API** : Les utilisateurs n'ont jamais accès à la clé API
- **Forward des requêtes** : Toutes les requêtes sont relayées vers l'API Ajax
- **SSE (Server-Sent Events)** : Events temps réel pour Home Assistant
- **Support SQS** : Écoute la queue SQS pour les events Ajax
- **Support 2FA** : Gestion de l'authentification à deux facteurs

## Déploiement Local (Docker)

```bash
# Copier le fichier d'environnement
cp .env.example .env

# Éditer .env avec votre clé API
nano .env

# Lancer avec Docker Compose
docker-compose up -d
```

## Variables d'Environnement

| Variable | Requis | Description |
|----------|--------|-------------|
| `AJAX_API_KEY` | Oui | Clé API Ajax Systems |
| `AWS_ACCESS_KEY_ID` | Non | Clé AWS pour SQS |
| `AWS_SECRET_ACCESS_KEY` | Non | Secret AWS pour SQS |
| `SQS_QUEUE_NAME` | Non | Nom de la queue SQS |
| `AWS_REGION` | Non | Région AWS (défaut: eu-west-1) |
| `LOG_LEVEL` | Non | Niveau de log (défaut: INFO) |
| `PORT` | Non | Port du serveur (défaut: 8080) |

## Déploiement AWS

### Option 1: EC2 / Lightsail

1. Créer une instance EC2 t3.micro ou Lightsail
2. Installer Docker
3. Cloner ce repo et configurer `.env`
4. Lancer avec `docker-compose up -d`
5. Configurer un certificat SSL (Let's Encrypt)

### Option 2: ECS Fargate

```bash
# Créer un repository ECR
aws ecr create-repository --repository-name ajax-proxy

# Build et push l'image
docker build -t ajax-proxy .
docker tag ajax-proxy:latest <account>.dkr.ecr.<region>.amazonaws.com/ajax-proxy:latest
docker push <account>.dkr.ecr.<region>.amazonaws.com/ajax-proxy:latest

# Créer un cluster ECS et service Fargate
```

## Endpoints

| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `/health` | GET | Health check |
| `/api/login` | POST | Authentification |
| `/api/2fa/verify` | POST | Vérification 2FA |
| `/api/events/stream` | GET | SSE events |
| `/api/*` | * | Forward vers Ajax API |
| `/webhook/events` | POST | Webhook pour events |

## Sécurité

- La clé API n'est jamais exposée aux clients
- Les tokens de session sont générés par le proxy
- Support HTTPS recommandé en production
- Rate limiting à implémenter si nécessaire

## Configuration Home Assistant

Dans Home Assistant, utiliser le mode "Proxy Sécurisé" :

1. URL du proxy : `https://votre-proxy.com`
2. Email : votre email Ajax
3. Password : votre mot de passe Ajax
