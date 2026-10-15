# StockFlow

## What is this project used for?
StockFlow helps a small clothing wholesaler track products, spot low stock, record orders and export inventory. Recording an order reduces stock, and the backend rejects an order when there is not enough inventory.

## Features
- React inventory and order interface with product/SKU search.
- Django JSON endpoints for products, orders and a summary dashboard.
- Atomic stock reduction to prevent overselling.
- Order totals preserve the price at the time of order.
- CSV inventory export and SQLite persistence.
- CSRF protection and six backend regression tests.

## Run locally
Python 3.12+ is sufficient to use the included frontend build:
```bash
python -m venv .venv
# Activate: Windows .venv\Scripts\activate; macOS/Linux source .venv/bin/activate
python -m pip install -r requirements.txt
cd backend
python manage.py migrate
python seed.py
python manage.py test
python manage.py runserver
```
Open http://127.0.0.1:8000/ . Seeding creates eight fictional products and preserves existing records. No database or user credentials are committed.

## Rebuild the frontend (optional)
Node.js and npm are required only when editing the React source:
```bash
cd frontend
npm ci
npm run build
```
The built assets are served by Django in local development. API examples are in `API_EXAMPLES.md`.

## Example workflow
Search for a product, record an order, observe the reduced quantity, try ordering more than available stock, and export the inventory CSV.

## Real interface walkthrough
Follow [the recording guide](docs/WALKTHROUGH.md) to capture orders, stock updates and CSV export using the real running application. The guide includes expected results and an acceptance checklist. Recording remains pending.

## Current scope
Self-created local prototype with fictional products and customers, not paid client work. Backend tests verify stock reduction, overselling prevention, invalid quantities, duplicate SKUs, CSV export and CSRF. A genuine browser UI walkthrough is still pending. Login, roles, payments, production deployment, comprehensive input hardening and browser end-to-end tests are not included. Do not expose this local development configuration publicly.
