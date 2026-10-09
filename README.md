# ShopFlow – Developer Handoff 📦

Hi DevOps team 👋 Here is our app. We wrote the code; please make it build, ship and run.

## The 3 parts

| Folder      | What it is                         | Tech                 | Port it listens on |
|-------------|------------------------------------|----------------------|--------------------|
| frontend/   | Web page that shows the products   | Plain HTML + JS      | (static files)     |
| backend/    | API that reads products from the DB| Python 3.12 + Flask  | 5000               |
| db/         | Database setup script              | PostgreSQL 17        | 5432               |

## How the parts talk

- The browser opens the frontend.
- The frontend calls the backend at: http://localhost:5000/api/products
- The backend connects to PostgreSQL using these environment variables:
  DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
- On first start, the database must run db/init.sql (creates the products table + 3 products).

## Backend commands (from inside backend/)

- Install: pip install -r requirements.txt
- Test:    pytest
- Run:     python app.py

## Endpoints

- GET /health        → {"status": "ok"}   (does not need the database)
- GET /api/products  → list of products   (needs the database)

## Our requests to DevOps

1. Every part must run in Docker.
2. One command should start the whole app.
3. Database data must survive restarts.
4. Jenkins must test, build, push and deploy on every change.
5. Never put the database password in Git.
