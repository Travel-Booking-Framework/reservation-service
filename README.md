# Reservation Microservice

A **Django REST Framework (DRF)**-based microservice for handling reservations, integrated with **gRPC**, **Kafka**, and **PostgreSQL**. It follows best practices like the **Command Pattern**, **Repository Pattern**, and **Circuit Breaker Pattern**.

---

## Features

- **Reservation Management**: Create and cancel reservations for hotels, flights, and trains.
- **gRPC Integration**: Communicate with other microservices (Hotel, Flight, Train, Payment, Notification).
- **Kafka**: Asynchronous messaging for data synchronization.
- **PostgreSQL**: Scalable and production-ready database.
- **Modular Design**: Uses Command, Repository, and Circuit Breaker patterns for clean and maintainable code.

---

## Technologies Used

- **Backend**: Django, Django REST Framework (DRF)
- **Database**: PostgreSQL
- **Inter-Service Communication**: gRPC
- **Message Broker**: Kafka
- **Patterns**: Command, Repository, Circuit Breaker

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/reservation-microservice.git
cd reservation-microservice
