# Backend Documentation

## Folder Structure
.
├── config
│   ├── config.js
│   ├── constants.js
│   └── database.js
├── controllers
│   ├── apiController.js
│   ├── authController.js
│   ├── fileController.py
│   └── userController.js
├── middleware
│   └── errorHandler.js
├── models
│   └── User.js
├── routes
│   ├── auth.js
│   ├── api.js
│   ├── index.js
│   └── users.js
├── services
│   ├── authService.js
│   ├── fileService.py
│   └── userService.js
├── utils
│   ├── helpers.js
│   ├── logger.js
│   └── validators.js
└── server.js

## API Reference
### Users
- **GET** `/api/users` - List users
- **POST** `/api/users` - Create user

### Auth
- **POST** `/api/auth/login` - Login user
- **POST** `/api/auth/register` - Register user

## Data Models
- **User**: Represents a user in the system with fields like id, username, email, and password.

## Application Structure
The application is structured into several layers: controllers handle the incoming requests, services contain the business logic, and models represent the data.

## Environment Variables
- `PORT`: The port on which the server runs (default is 3000).
- `DATABASE_URL`: The URL for connecting to the database.
- `JWT_SECRET`: Secret key for signing JWT tokens.# Backend API Documentation

## Folder Structure

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

## API Reference
### Auth
- **POST /api/auth/login**: Logs in a user.
  - Request Body: `{ email, password }`
  - Response: `{ token }`

- **POST /api/auth/register**: Registers a new user.
  - Request Body: `{ name, email, password }`
  - Response: `{ user }`

### Users
- **GET /api/users/:id**: Retrieves a user by ID.
  - Response: `{ user }`

### Health Check
- **GET /api/health**: Checks if the API is running.
  - Response: `{ message: 'API is running' }`

## Data Models
### User
- **name**: String
- **email**: String (unique)
- **password**: String

## Application Structure
- **config/**: Configuration files.
- **controllers/**: Business logic handlers.
- **middleware/**: Middleware functions.
- **models/**: Database models.
- **routes/**: API routes.
- **services/**: Business logic services.
- **utils/**: Utility functions.

## Environment Variables
- **PORT**: Port for the server to run on.
- **DATABASE_URL**: MongoDB connection string.
- **JWT_SECRET**: Secret key for JWT.