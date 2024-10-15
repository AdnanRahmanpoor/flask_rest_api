# RESTful API with Flask

## Overview

This project is a simple RESTful API built using Flask, designed to manage resources like tasks or books (customizable based on needs). The API allows users to perform common CRUD (Create, Read, Update, Delete) operations, and provides authentication with JWT (JSON Web Token) to secure the endpoints. This project demonstrates the implementation of RESTful principles while leveraging Flask-RESTful for resource management and Flask-JWT-Extended for secure authentication.

## Features

- **JWT Authentication:** Secure the API using JSON Web Tokens (JWT). Users must log in to obtain a token to access protected routes.
- **CRUD Operations:** 
  - **Create:** Add a new resource.
  - **Read:** Fetch a list of resources or a single resource by ID.
  - **Update:** Modify an existing resource.
  - **Delete:** Remove a resource from the database.
- **Flask-RESTful:** Simplifies the API by structuring routes as resources.
- **Postman Testing:** API endpoints have been thoroughly tested using Postman.

## Technologies

- **Flask**: For creating the API and managing the server-side logic.
- **Flask-RESTful**: A Flask extension to quickly build REST APIs by organizing routes as resources.
- **Flask-JWT-Extended**: To handle authentication and secure endpoints with JWT.
- **Postman**: Used for API testing to ensure that all endpoints behave as expected.

## Endpoints

Here’s a list of the available API endpoints:

- **POST /login:** Authenticates a user and returns a JWT token.
- **GET /resources:** Retrieves a list of resources for the authenticated user.
- **POST /resources:** Creates a new resource.
- **GET /resources/<resource_id>:** Retrieves the details of a specific resource.
- **PUT /resources/<resource_id>:** Updates an existing resource.
- **DELETE /resources/<resource_id>:** Deletes a resource.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create secrets in the .env
```bash
# In python shell
import secrets
print(secrets.token_hex(16)) # generate 2 times, 1 for SECRECTS_KET other for JWT_SECRETS_KEY and put them in .env at the root dir
```

4. Run the app:
   ```bash
   flask run
   ```

5. Test the API using Postman or curl commands.

## What I Learned

By building this project, I gained experience with:
- **Building RESTful APIs**: Understanding the structure of API endpoints, and how to organize routes effectively.
- **JWT Authentication**: Implementing secure access to API endpoints using JSON Web Tokens.
- **Flask Extensions**: Using Flask-RESTful to simplify route management and Flask-JWT-Extended for authentication.
- **CRUD Operations**: Performing Create, Read, Update, and Delete operations on resources using SQLAlchemy ORM.
- **Postman**: Testing the API to ensure it works as expected and handles edge cases properly.
  
This project improved my knowledge of API development and reinforced the importance of securing endpoints when working with sensitive data.
