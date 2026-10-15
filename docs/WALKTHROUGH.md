# Record the real StockFlow interface

This guide records the actual React interface connected to Django. A browser recording has not been completed in the assistant environment: its browser blocks local-server URLs. Do not describe backend graphics as a UI recording.

## Start
From the repository root, activate your Python environment and run:
```bash
python -m pip install -r requirements.txt
cd backend
python manage.py migrate
python seed.py
python manage.py test
python manage.py runserver
```
Open http://127.0.0.1:8000/ in Chrome or Edge. Confirm that eight seeded products appear. Existing records are preserved, so stock totals can differ after previous orders.

## A 45–60 second recording
On Windows press **Win+Alt+R** to start/stop an Xbox Game Bar recording of the browser, or use your normal screen recorder. Keep the app and its real responses visible.

| Step | Action | Proof to capture |
|---|---|---|
| 1 | Inventory: search `AP-001` | Read and record the starting stock S |
| 2 | Orders → Record order | Choose Classic Cotton Shirt, customer `Walkthrough Buyer`, quantity 2 |
| 3 | Save order | Success notice and the new order with total ₹1,598 |
| 4 | Inventory: search `AP-001` | Stock is now S minus 2 |
| 5 | Optional: order more than available | Clear insufficient-stock response; no successful extra order |
| 6 | Inventory → Export CSV | Actual browser download completes |
| 7 | Open the downloaded CSV in Excel | AP-001 row shows the updated quantity |

Use fictional customer details only. If starting stock is below 2, add a separate test product and use it instead. Do not reset an existing database that contains useful work.

## Acceptance checklist
- Video shows actual clicks and server responses without simulated UI.
- Order appears after saving and product stock decreases by exactly two.
- Downloaded CSV has eight products for an unchanged seeded catalog, plus its header.
- CSV stock agrees with the interface.
- Capture three real screenshots: initial stock, successful order, exported CSV.
- Name the recording `stockflow-ui-walkthrough.mp4` and keep it under Fiverr's current upload limit.

## Current verification
The six Django regression tests cover stock reduction, overselling prevention, invalid quantities, duplicate SKUs, CSV export and CSRF. Browser interactions and a video must be verified separately. This guide does not claim they have already been recorded.
