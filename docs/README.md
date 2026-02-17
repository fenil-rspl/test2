# Backend
This repository contains the backend API for the web application.

## Directory Structure

```
backend/
├── config/
│   ├── config.js
│   ├── config.py
│   ├── constants.js
│   ├── constants.py
│   ├── database.js
│   ├── database.py
│   └── storage.py
├── controllers/
│   ├── apiController.js
│   ├── apiController.py
│   ├── authController.js
│   ├── authController.py
│   ├── fileController.py
│   ├── userController.js
│   └── userController.py
├── docs/
│   ├── BACKEND.md
│   └── README.md
├── middleware/
│   ├── auth.js
│   ├── auth.py
│   ├── cors.js
│   ├── cors.py
│   ├── errorHandler.js
│   ├── errorHandler.py
│   ├── fileValidation.py
│   └── upload.py
├── models/
│   ├── File.py
│   ├── index.js
│   ├── index.py
│   ├── User.js
│   └── User.py
├── routes/
│   ├── api.js
│   ├── api.py
│   ├── auth.js
│   ├── auth.py
│   ├── files.py
│   ├── index.js
│   ├── index.py
│   ├── users.js
│   └── users.py
├── services/
│   ├── authService.js
│   ├── authService.py
│   ├── fileService.py
│   ├── s3Service.py
│   ├── userService.js
│   └── userService.py
├── utils/
│   ├── helpers.js
│   ├── helpers.py
│   ├── logger.js
│   ├── logger.py
│   ├── validators.js
│   └── validators.py
├── .env.example
├── .gitignore
├── app.js
├── app.py
├── architecture.json
├── architecture.md
├── docker-compose.yml
├── Dockerfile
├── package.json
├── readme.md
├── requirements.txt
├── server.js
└── server.py
```

## Quick Start
1. Clone the repository.
2. Create a `.env` file based on `.env.example`.
3. Run `npm install` to install dependencies.
4. Start the server with `npm start`.