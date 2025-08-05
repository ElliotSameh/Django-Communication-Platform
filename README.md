# Django-Communication-Platform

A lightweight, real-time communication hub built with Django.  
Users can spin up topic-based rooms, chat live, and share resources – perfect for study groups, communities, or internal teams.

---

## ✨ Key Features

| Area               | Highlights                                                                             |
| ------------------ | -------------------------------------------------------------------------------------- |
| **Rooms & Topics** | Create, search, join, update, and delete discussion rooms – each tied to a topic tag.  |
| **Messaging**      | Live message feed in every room with instant activity stream.                          |
| **Authentication** | Sign-up, login, logout, and profile editing using Django’s auth system.                |
| **Responsive UI**  | Bootstrap-based templates plus custom CSS (see `static/` & `theme/`).                  |
| **Admin Panel**    | Full CRUD from Django admin for power users.                                           |
| **Extensible**     | Modular `studybud` app and reusable `base` app make feature-additions straightforward. |

---

## 🏗️ Project Structure

```
base/            # reusable layouts, core utilities
static/          # CSS, JS, images
studybud/        # domain logic: models, views, forms
templates/       # HTML templates
theme/           # Bootstrap theme overrides
manage.py        # Django entrypoint
requirements.txt # Python dependencies
```

---

## 🔧 Tech Stack

- **Backend:** Django 4+
- **Database:** SQLite (dev) – swap for Postgres/MySQL in prod
- **Frontend:** HTML / CSS / JavaScript (Bootstrap 5)
- **Languages mix:** ≈ 51 % HTML, 25 % Python, 21 % CSS, 3 % JS

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/ElliotSameh/Django-Communication-Platform.git
cd Django-Communication-Platform

# 2. Create & activate a virtual env (optional but recommended)
python -m venv env
source env/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations & create a superuser
python manage.py migrate
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver
```

Navigate to <http://127.0.0.1:8000> to explore the platform.  
Admin panel lives at <http://127.0.0.1:8000/admin>.

---

## ⚙️ Environment Variables (optional)

| Variable        | Purpose                                   | Default               |
| --------------- | ----------------------------------------- | --------------------- |
| `SECRET_KEY`    | Django secret – **change in production!** | auto‑generated in dev |
| `DEBUG`         | Toggle debug mode                         | `True`                |
| `ALLOWED_HOSTS` | Comma‑separated hostnames                 | `127.0.0.1,localhost` |

Create a `env` file (or export variables) for a production deploy.

---

## 🛠️ Development Tips

1. **Static files** – run `python manage.py collectstatic` for prod.
2. **Linting & Formatting** – add _ruff_ or _black_ if desired.
3. **Docker** – container‑ise with an official `python:3.12‑slim` image for easy CI.
4. **Testing** – Django’s `TestCase` + coverage are ready for use.

---

## 📬 Contact

Created & maintained by **[Elliot Sameh](mailto:elliotsameh@gmail.com)** – pull requests and suggestions welcome!
