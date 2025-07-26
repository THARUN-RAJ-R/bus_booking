

# 🚌 Bus Booking Web Application

A simple and secure bus booking web application built with **FastAPI**, **HTML**, **CSS**, and **JavaScript**. This project allows users to view, search, and book bus tickets, and includes an authentication system for secure user access.

---

## 🚀 Features

* 🔐 **User Authentication** (Register/Login with hashed password)
* 🚌 **View and Search Buses**
* 📅 **Book Tickets**
* 🧾 **View Bookings**
* 🧑‍💻 Admin-side features for managing buses *(if applicable)*
* ✅ RESTful APIs with FastAPI
* 🎨 Responsive frontend using HTML, CSS, and JavaScript

---

## 🛠️ Tech Stack

| Technology | Description                     |
| ---------- | ------------------------------- |
| FastAPI    | Backend framework (Python)      |
| SQLAlchemy | ORM for database interaction    |
| SQLite     | Lightweight relational database |
| HTML/CSS   | UI and styling                  |
| JavaScript | Frontend interactivity          |
| Jinja2     | HTML templating engine          |
| Passlib    | Password hashing                |

---

## 🔧 Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/THARUN-RAJ-R/bus_booking.git
   cd bus_booking
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**

   ```bash
   uvicorn main:app --reload
   ```

5. **Access the web app:**

   Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Project Structure

```bash
bus_booking/
├── static/                # CSS, JS files
├── templates/             # HTML templates
├── database.py            # DB models and setup
├── main.py                # Entry point of FastAPI app
├── models.py              # SQLAlchemy models
├── schemas.py             # Pydantic schemas
├── auth.py                # Authentication logic
├── routers/               # API routers (optional structure)
└── requirements.txt       # Python dependencies
```

---

## 🧪 Future Improvements

* ✅ Admin Dashboard
* 📱 Mobile responsive design
* 📊 Bus seat layout selection
* 📧 Email confirmations for bookings
* 💳 Payment integration (Razorpay/Stripe)
* 📂 Docker support

---

## 🙋‍♂️ Author

**Tharun Raj R**

* 🌐 [GitHub](https://github.com/THARUN-RAJ-R)
* 🎓 B.Tech CSE (IoT) Student at VIT

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

