# ibtisham_evs_final  

A lightweight Django application that demonstrates a simple blockchain‑based record‑keeping system. The project includes a basic admin interface, candidate management, and a proof‑of‑concept blockchain implementation written in pure Python.

---

## Overview  

`ibtisham_evs_final` is a **Python/Django** project that showcases how blockchain concepts can be integrated into a web application. It stores immutable records of candidate data (e.g., images, tour information) and provides a UI for administrators to view and manage these records. The blockchain logic is encapsulated in `myapp/blockchain.py`, while the rest of the app follows standard Django conventions.

---

## Features  

- **Blockchain ledger** – each transaction is hashed and linked to the previous block, guaranteeing tamper‑evidence.  
- **Candidate management** – static assets (`candidates/*.png`, `candidates/tour.jpg`) are served through the Django admin.  
- **Admin dashboard** – full CRUD support for blockchain records via Django’s built‑in admin site.  
- **Custom forms** – simple Django forms for adding new blockchain entries (`myapp/forms.py`).  
- **Migrations** – incremental schema evolution (see `myapp/migrations/`).  
- **Self‑contained** – all required code lives inside the repository; no external services are needed.

---

## Tech Stack  

| Layer | Technology |
|-------|------------|
| Language | Python 3.9+ |
| Web Framework | Django 4.x |
| Database | SQLite (default) – can be swapped for PostgreSQL, MySQL, etc. |
| Front‑end | Django templates (no JS framework required) |
| Blockchain | Pure‑Python implementation (`hashlib`, `datetime`) |
| Version Control | Git (hosted on GitHub) |

---

## Installation  

> **Prerequisites**  
> - Python 3.9 or newer  
> - Git  

```bash
# 1. Clone the repository
git clone https://github.com/your-username/ibtisham_evs_final.git
cd ibtisham_evs_final

# 2. Create and activate a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install django  # or `pip install -r requirements.txt` if you add one later

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser for the admin interface
python manage.py createsuperuser
```

> **Optional** – If you add a `requirements.txt` later, replace step 3 with `pip install -r requirements.txt`.

---

## Usage  

```bash
# Start the development server
python manage.py runserver
```

1. Open your browser and navigate to `http://127.0.0.1:8000/admin/`.  
2. Log in with the superuser credentials created earlier.  
3. From the admin panel you can:  
   - View the list of **Blockchain Records** (each block shows its hash, previous hash, timestamp, and payload).  
   - Add new candidates or upload images located in `candidates/`.  
   - Inspect the underlying blockchain via the **BlockchainRecord** model.  

> **Note** – The demo data (e.g., `candidates/CS604p.png`) is stored in the repository for illustration purposes only. Replace these assets with