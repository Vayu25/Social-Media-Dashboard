# Social Media Dashboard

A responsive social media dashboard that integrates platforms like Facebook and Twitter.
It allows users to schedule posts, view analytics, and interact with content (like, comment, share).

## 🔧 Features

* 🌐 Multi-platform integration (Facebook, Twitter, etc.)
* 📅 Schedule posts in advance
* 📊 Analytics for engagement and reach
* 👍 Like, 💬 comment, and 🔁 share functionalities
* 👥 User authentication and profile management

## 🛠️ Tech Stack

* **Frontend**: HTML, CSS, JavaScript / React (if used)
* **Backend**: Django (Python)
* **Database**: PostgreSQL / SQLite
* **APIs**: Social media API integration (mock or real)

## 🚀 Getting Started

Follow the steps below to set up the project locally on your machine:

### 1. Clone the Repository

```bash
git clone https://github.com/Vayu25/Social-Media-Dashboard.git
cd Social-Media-Dashboard
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# Activate the environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to view the application.
