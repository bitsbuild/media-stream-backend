# 🎬 Media Stream Backend

This is a Django REST Framework-based backend service for a media streaming application. It offers full-fledged APIs for managing multimedia content, user reviews, artists, content categorization, and subscription plans. It also supports file uploads, filtering, search, ordering, and authentication.

---

## 🌐 Hosted API

The live version of this backend is available here:

**🔗 https://mstream-dg6r.onrender.com/**

You can test all endpoints from the base URL above. Make sure to use the correct `Authorization` header (see [🔐 Authentication](#-authentication)).

---

## 📁 Repository Structure

```

media-stream-backend/
│
├── mstream/                    # Main Django project folder
│   ├── app/                   # Core app handling content, artists, subscriptions, etc.
│   ├── user/                  # App for user management (sign up, login, delete)
│   ├── mstream/               # Project-level settings, urls, and wsgi
│   ├── manage.py              # Django's CLI utility
│   └── .env                   # Environment variables (not tracked)
└── README.md                  # This file

````

---

## 🧠 Features

- User Signup, Login (Token-based), and Delete account.
- Content management with support for:
  - Multiple genres
  - Parental control tags
  - Artists and cast
  - Content types (e.g., Movie, Show)
- Reviews and rating aggregation
- Artist-to-content relation with custom roles (e.g., Director, Actor)
- Subscription plans and user subscription mapping
- Media file uploads associated with content
- Filtering, searching, ordering across most API endpoints
- Pagination support
- Token-based authentication
- Rate throttling enabled (60 req/min/user)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip
- virtualenv (optional but recommended)
- SQLite (default)
- Git

### Clone the repository

```bash
git clone https://github.com/bitsbuild/media-stream-backend.git
cd media-stream-backend/mstream
````

### Setup Environment

Create a `.env` file inside `mstream/` directory:

```
DSK=your-django-secret-key
```

### Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not yet created, you can generate it with:
>
> ```bash
> pip freeze > requirements.txt
> ```

### Run Migrations & Start Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🔐 Authentication

* Uses token-based authentication.
* After registering (`/user/signup/`) and logging in (`/user/login/`), the API will return an `auth_token`.
* Pass the token in headers as:

```
Authorization: Token your_token_here
```

---

## 🧪 API Endpoints

### User Authentication

| Method | Endpoint        | Description             |
| ------ | --------------- | ----------------------- |
| POST   | `/user/signup/` | Register a new user     |
| POST   | `/user/login/`  | Obtain auth token       |
| DELETE | `/user/delete/` | Delete the current user |

---

### Content Management (Admin only)

| Resource                 | Base Endpoint          | Permissions |
| ------------------------ | ---------------------- | ----------- |
| Content                  | `/api/contents/`       | Admin Only  |
| Content Genres           | `/api/genre/`          | Admin Only  |
| Parental Control Tags    | `/api/parcontag/`      | Admin Only  |
| Content Types            | `/api/contype/`        | Admin Only  |
| Content Media Files      | `/api/conmediafile/`   | Admin Only  |
| Artists                  | `/api/artists/`        | Admin Only  |
| Artist-Content Relations | `/api/artconrelation/` | Admin Only  |

---

### Reviews (Authenticated users)

| Method | Endpoint             | Description       |
| ------ | -------------------- | ----------------- |
| GET    | `/api/reviews/`      | List all reviews  |
| POST   | `/api/reviews/`      | Add a new review  |
| PUT    | `/api/reviews/<id>/` | Update own review |
| DELETE | `/api/reviews/<id>/` | Delete own review |

> Ratings are automatically averaged and updated on the related content whenever a review is created.

---

### Subscriptions (Admin only)

| Resource           | Endpoint          |
| ------------------ | ----------------- |
| Subscription Plans | `/api/submodels/` |
| User Subscriptions | `/api/submap/`    |

---

## 🔎 Filtering, Searching, and Ordering

* Most endpoints support:

  * `filter` via query params (e.g., `?name=Action`)
  * `search` (e.g., `?search=thriller`)
  * `ordering` (e.g., `?ordering=-created`)
* Pagination is enabled (20 per page).

### Example

```http
GET /api/contents/?genre=some_uuid&ordering=-created&search=Avengers
```

---

## 📦 Media Handling

* Media files are uploaded via `/api/conmediafile/`.
* Accessible at `http://localhost:8000/content/<file_path>` during development.
* Stored in `content/` directory (as per `MEDIA_ROOT` setting).

---

## 🔐 Admin Panel

To create a superuser for admin operations:

```bash
python manage.py createsuperuser
```

Access the admin panel at: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 🔧 Environment Variables

| Key   | Description       |
| ----- | ----------------- |
| `DSK` | Django secret key |

Use `.env` file to store them securely.

---

## 🛠️ Technologies Used

* **Django** - Web framework
* **Django REST Framework** - API development
* **SQLite** - Default database
* **TokenAuthentication** - Secure user login
* **django-filter** - Filtering support
* **dotenv** - Environment variable management

---

## 🤝 Contributing

If you'd like to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit and push (`git commit -am 'Add your message'`)
5. Create a Pull Request

---

## 📃 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Jash Upadhyay**
🔗 GitHub: [bitsbuild](https://github.com/bitsbuild)

---

## 💬 Feedback

Have suggestions or issues? Feel free to [open an issue](https://github.com/bitsbuild/media-stream-backend/issues) or reach out!
