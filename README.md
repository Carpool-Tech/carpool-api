# Carpool API Documentation

The Carpool API allows for the management of Users, Cars, Trips, and User Routes in the Carpool application. The following endpoints are available.

## Users

Users are the people who use the Carpool application. They can be drivers or passengers.

- **GET /api/users/**: Retrieves a list of all users. Each user object includes all User model fields.
- **POST /api/users/**: Creates a new user. Requires a JSON body with all the User model fields.
- **GET /api/users/{id}/**: Retrieves the details of a specific user identified by their ID.
- **PUT /api/users/{id}/**: Updates a specific user identified by their ID. Requires a JSON body with all the User model fields.
- **DELETE /api/users/{id}/**: Deletes a specific user identified by their ID.

## Cars

Cars belong to users and are used for trips.

- **GET /api/cars/**: Retrieves a list of all cars. Each car object includes all Car model fields.
- **POST /api/cars/**: Creates a new car. Requires a JSON body with all the Car model fields.
- **GET /api/cars/{id}/**: Retrieves the details of a specific car identified by its ID.
- **PUT /api/cars/{id}/**: Updates a specific car identified by its ID. Requires a JSON body with all the Car model fields.
- **DELETE /api/cars/{id}/**: Deletes a specific car identified by its ID.

## Trips

Trips represent the journey from one location to another. Trips are associated with a user (the driver) and a car.

- **GET /api/trips/**: Retrieves a list of all trips. Each trip object includes all Trip model fields.
- **POST /api/trips/**: Creates a new trip. Requires a JSON body with all the Trip model fields.
- **GET /api/trips/{id}/**: Retrieves the details of a specific trip identified by its ID.
- **PUT /api/trips/{id}/**: Updates a specific trip identified by its ID. Requires a JSON body with all the Trip model fields.
- **DELETE /api/trips/{id}/**: Deletes a specific trip identified by its ID.

## User Routes

User Routes represent the desired travel routes of users. They can be associated with both drivers and passengers.

- **GET /api/user_routes/**: Retrieves a list of all user routes. Each user route object includes all UserRoute model fields.
- **POST /api/user_routes/**: Creates a new user route. Requires a JSON body with all the UserRoute model fields.
- **GET /api/user_routes/{id}/**: Retrieves the details of a specific user route identified by its ID.
- **PUT /api/user_routes/{id}/**: Updates a specific user route identified by its ID. Requires a JSON body with all the UserRoute model fields.
- **DELETE /api/user_routes/{id}/**: Deletes a specific user route identified by its ID.
