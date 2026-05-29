# Flask App with Docker 🐳

A simple **Python Flask** web application containerized using **Docker** — built to understand containerization fundamentals and how to ship Python apps consistently across environments.

---

## 🛠️ Tech Stack

- **Python** — core language
- **Flask** — lightweight web framework
- **Docker** — containerization
- **Docker Compose** — multi-container orchestration (if applicable)

---

## 🚀 Getting Started

### Prerequisites
- Docker installed on your machine

### Run with Docker

```bash
# Clone the repo
git clone https://github.com/imTanush02/flask-project.git
cd flask-project

# Build the Docker image
docker build -t flask-app .

# Run the container
docker run -p 5000:5000 flask-app
```

Then open `http://localhost:5000` in your browser.

---

## 📁 Project Structure

```
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image configuration
└── README.md
```

---

## 🐳 Dockerfile Overview

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

---

## 💡 What I Learned

- Writing a `Dockerfile` for a Python/Flask app
- Managing dependencies with `requirements.txt` inside containers
- Understanding how containers isolate environments
- Running and exposing containerized web apps on local ports
