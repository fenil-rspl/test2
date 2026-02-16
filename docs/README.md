# Backend
This repository contains the backend API for the web application.

## Directory Structure

```
backend/
├── config/
│   ├── config.py
│   ├── constants.py
│   ├── database.py
│   └── storage.py
├── controllers/
│   ├── apiController.py
│   ├── authController.py
│   ├── fileController.py
│   └── userController.py
├── docs/
│   ├── BACKEND.md
│   └── README.md
├── middleware/
│   ├── auth.py
│   ├── cors.py
│   ├── errorHandler.py
│   ├── fileValidation.py
│   └── upload.py
├── models/
│   ├── File.py
│   ├── index.py
│   └── User.py
├── routes/
│   ├── api.py
│   ├── auth.py
│   ├── files.py
│   ├── index.py
│   └── users.py
├── services/
│   ├── authService.py
│   ├── fileService.py
│   ├── s3Service.py
│   └── userService.py
├── utils/
│   ├── helpers.py
│   ├── logger.py
│   └── validators.py
├── app.py
├── architecture.json
├── architecture.md
├── readme.md
├── requirements.txt
└── server.py
```

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Configure environment variables in `.env`
3. Run the application: `uvicorn app:app --reload`