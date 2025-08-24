
# API Assignments Module

> Hands-on REST API assignments for the GenAI Systems Bootcamp. This module covers the foundations of building, securing, and documenting robust APIs, with a focus on real-world best practices and developer workflows.

---

## 📚 What You'll Learn

- **REST API Fundamentals**: Principles, HTTP methods, status codes, and design patterns
- **CRUD Operations**: Implementing Create, Read, Update, Delete with validation
- **Authentication & Authorization**: API Key, JWT, and securing endpoints
- **Rate Limiting**: Protecting APIs from abuse
- **Pagination, Sorting, Filtering**: Handling large datasets efficiently
- **OpenAPI/Swagger Docs**: Auto-generating and maintaining API documentation
- **Testing & CI Integration**: Writing tests and automating checks
- **Observability Basics**: Logging, monitoring, and debugging APIs

---

## 📂 Directory Structure

```
api-assignments/
├─ api-request-1.py   # Assignment 1: Basic REST API
├─ api-request-2.py   # Assignment 2: CRUD with validation
├─ api-request-3.py   # Assignment 3: Auth & rate limiting
├─ api-request-4.py   # Assignment 4: Pagination & docs
├─ api-request.py     # (Optional) Shared utilities or base code
├─ requirements.txt   # Python dependencies
└─ README.md          # This guide
```

---

## 🚦 Getting Started

1. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```
2. **Work through each assignment in order.**
3. **Test your code** using the provided instructions or your own test cases.
4. **Document your API** using OpenAPI/Swagger where required.

---

## 📝 Assignment Overview

| File                | Focus                        |
|---------------------|------------------------------|
| api-request-1.py    | REST basics, endpoints       |
| api-request-2.py    | CRUD, validation             |
| api-request-3.py    | Auth, rate limiting          |
| api-request-4.py    | Pagination, docs             |

---

## 💡 Tips

- Use [FastAPI](https://fastapi.tiangolo.com/) or [Flask](https://flask.palletsprojects.com/) for rapid API development.
- Validate all inputs and handle errors gracefully.
- Keep your code modular and well-documented.
- Use tools like [httpie](https://httpie.io/) or [Postman](https://www.postman.com/) for manual API testing.

---

Happy coding! 🚀
