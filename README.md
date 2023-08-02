# Carpool API Documentation

## User Endpoints

- **GET /api/users/**: Retrieve a list of all users.
- **POST /api/users/**: Create a new user. Requires a JSON body with all fields for the User model.
- **GET /api/users/{id}/**: Retrieve the details of a specific user by their ID.
- **PUT /api/users/{id}/**: Update a specific user. Requires a JSON body with all fields for the User model.
- **DELETE /api/users/{id}/**: Delete a specific user.

## Car Endpoints

- **GET /api/cars/**: Retrieve a list of all cars.
- **POST /api/cars/**: Create a new car. Requires a JSON body with all fields for the Car model.
- **GET /api/cars/{id}/**: Retrieve the details of a specific car by its ID.
- **PUT /api/cars/{id}/**: Update a specific car. Requires a JSON body with all fields for the Car model.
- **DELETE /api/cars/{id}/**: Delete a specific car.

## Trip Endpoints

- **GET /api/trips/**: Retrieve a list of all trips.
- **POST /api/trips/**: Create a new trip. Requires a JSON body with all fields for the Trip model.
- **GET /api/trips/{id}/**: Retrieve the details of a specific trip by its ID.
- **PUT /api/trips/{id}/**: Update a specific trip. Requires a JSON body with all fields for the Trip model.
- **DELETE /api/trips/{id}/**: Delete a specific trip.

## User Route Endpoints

- **GET /api/user_routes/**: Retrieve a list of all user routes.
- **POST /api/user_routes/**: Create a new user route. Requires a JSON body with all fields for the UserRoute model.
- **GET /api/user_routes/{id}/**: Retrieve the details of a specific user route by its ID.
- **PUT /api/user_routes/{id}/**: Update a specific user route. Requires a JSON body with all fields for the UserRoute model.
- **DELETE /api/user_routes/{id}/**: Delete a specific user route.
