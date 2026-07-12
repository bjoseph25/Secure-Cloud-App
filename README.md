# Secure Cloud App

A production-style backend application built with **FastAPI**, **PostgreSQL**, **Docker**, and **AWS** to demonstrate modern backend development, cloud deployment, DevOps practices, and secure application design.

> **Project Status:** 🚧 In Development

---

## Overview

Secure Cloud App is a portfolio project designed to simulate a real-world backend application from development through deployment. The project focuses on building secure, scalable, and maintainable software while following industry best practices.

The application will include user authentication, RESTful APIs, database management, containerization, cloud deployment, CI/CD automation, and monitoring.

---

## Project Goals

- Build a production-ready REST API using FastAPI
- Design a secure authentication system using JWT
- Store application data in PostgreSQL
- Containerize the application with Docker
- Deploy the application to AWS EC2
- Configure Nginx as a reverse proxy
- Implement CI/CD with GitHub Actions
- Follow secure software development practices

---

## Planned Features

### Authentication

- User registration
- User login
- JWT authentication
- Password hashing
- Protected API endpoints

### Project Management

- Create projects
- Update projects
- Delete projects
- View project details

### Task Management

- Create tasks
- Assign priorities
- Update task status
- Delete tasks
- Due dates

### API

- RESTful API design
- Request validation
- Error handling
- OpenAPI documentation

### Security

- Secure password storage
- Environment variable management
- HTTPS deployment
- Input validation
- Authentication middleware

---

## Technology Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Database

- PostgreSQL
- Alembic

### DevOps

- Docker
- Docker Compose
- GitHub Actions
- Nginx

### Cloud

- AWS EC2

### Version Control

- Git
- GitHub

---

## Project Structure

```text
secure-cloud-app/
├── app/
│   ├── api/
│   ├── auth/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── tests/
├── alembic/
├── docker/
├── nginx/
├── scripts/
│
├── .github/
│   └── workflows/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Architecture

### Development

```text
                Client
                   │
                   ▼
             FastAPI Backend
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
 Authentication         Business Logic
        │                     │
        └──────────┬──────────┘
                   ▼
             PostgreSQL Database
```

### Production

```text
Internet
    │
    ▼
AWS EC2
    │
    ▼
Nginx
    │
    ▼
Docker Container
    │
    ▼
FastAPI
    │
    ▼
PostgreSQL
```

---

## API Documentation

Once the application is running:

### Swagger UI

```
http://localhost:8000/docs
```

### ReDoc

```
http://localhost:8000/redoc
```

---

## Development Roadmap

### Phase 1 – Project Initialization

- [ ] Configure FastAPI
- [ ] Create project structure
- [ ] Health check endpoint

### Phase 2 – Database

- [ ] PostgreSQL
- [ ] SQLAlchemy
- [ ] Alembic migrations

### Phase 3 – Authentication

- [ ] User registration
- [ ] Login
- [ ] JWT Authentication
- [ ] Password hashing

### Phase 4 – Containerization

- [ ] Dockerfile
- [ ] Docker Compose
- [ ] Environment variables

### Phase 5 – Cloud Deployment

- [ ] AWS EC2
- [ ] Nginx
- [ ] HTTPS

### Phase 6 – CI/CD

- [ ] GitHub Actions
- [ ] Automated deployment

### Phase 7 – Production Features

- [ ] Logging
- [ ] Monitoring
- [ ] Health checks

---

## Skills Demonstrated

- Backend Development
- REST API Development
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Linux
- AWS
- Nginx
- GitHub Actions
- CI/CD
- Secure Authentication
- Software Architecture
- Database Design

---

## Future Enhancements

- Role-Based Access Control (RBAC)
- Redis caching
- Email verification
- Password reset
- API rate limiting
- Unit testing
- Integration testing
- Monitoring dashboard
- Kubernetes deployment
- Terraform Infrastructure as Code

---

## Learning Objectives

This project was created to strengthen practical experience with:

- Backend software engineering
- Cloud infrastructure
- Secure application development
- DevOps workflows
- Containerization
- Production deployments
- Database management
- Authentication and authorization

---

## License

This project is intended for educational and portfolio purposes.

---

## Author

**Brandon Joseph**

- GitHub: https://github.com/bjoseph25
- LinkedIn: https://linkedin.com/in/brandonjosephcs
