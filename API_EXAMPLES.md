# API examples

Run the server locally first. Open the React interface to obtain a CSRF cookie and submit forms; writes without the CSRF token are rejected.

Product POST `/api/products/`:
```json
{"sku":"AP-009","name":"Demo Linen Kurta","category":"Ethnic","price":"1199.00","stock":20}
```
Order POST `/api/orders/` (replace product ID with one returned by GET):
```json
{"product_id":1,"quantity":2,"customer":"Demo Retailer C"}
```
Expected: 201 for valid requests, 400 for invalid input or insufficient stock, 403 without valid CSRF protection. GET `/api/products/` and GET `/api/orders/` show persisted data. GET `/api/summary/` returns totals. GET `/api/export/` downloads CSV.

No authentication is implemented; run on localhost only. CSRF is not a substitute for authentication.
