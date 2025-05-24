# Frontend Documentation

This project currently does not include a frontend user interface. All interactions are handled via the backend Flask API.

## How to Interact
- Use tools like Postman, curl, or any HTTP client to send POST requests to the `/chat` endpoint.
- Example:
  ```bash
  curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"msg": "What is diabetes?"}'
  ```

## Extending with a Frontend
If you wish to add a frontend (e.g., React, Vue, or static HTML), create a new directory (e.g., `frontend/`) and build your UI to interact with the Flask API endpoints.
