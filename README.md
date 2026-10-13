# Smart Load Balancer Simulation

## Overview

Smart Load Balancer Simulation is a Python Flask-based project that demonstrates how a load balancer distributes incoming client requests among multiple backend servers.

The project creates multiple Flask servers running on different ports and uses a load balancer to forward requests using a Round Robin algorithm.

This project helps understand the basic working of:

- Client-server architecture
- Load balancing
- Backend server communication
- API requests using Python Flask

## Features

- Multiple backend Flask servers
- Round Robin load distribution
- Automatic request forwarding
- Health check of backend servers
- Simple and lightweight implementation
- Easy to understand architecture

## Technologies Used

- Python
- Flask
- Requests Library

## Project Structure

Load-Balancer-Project
│
├── load_balancer.py # Main load balancer application
├── server1.py # Backend server 1
├── server2.py # Backend server 2
├── server3.py # Backend server 3
├── requirements.txt # Required Python packages
└── README.md # Project documentation

## Installation and Setup

### Step 1: Clone the Repository

git clone https://github.com/SHAIK-GHOUSE1/Load-Balancer-Project.git

Move into the project folder:

cd Load-Balancer-Project

### Step 2: Install Dependencies

Install required packages:

pip install -r requirements.txt

## How to Run the Project

### Step 1: Start Backend Servers

Open three separate terminals.

Run Server 1:

python server1.py

Run Server 2:

python server2.py

Run Server 3:

python server3.py

Each server runs on a different port:

Server 1 → Port 5001
Server 2 → Port 5002
Server 3 → Port 5003

### Step 2: Start Load Balancer

Open another terminal:

python load_balancer.py

The load balancer starts running on: http://127.0.0.1:5000

## Working Principle

1. Client sends a request to the load balancer.
2. Load balancer receives the request.
3. It selects a backend server using the Round Robin algorithm.
4. Request is forwarded to the selected server.
5. Backend server processes the request.
6. Response is returned back to the client.

## Load Balancing Algorithm

This project uses the **Round Robin Algorithm**.

Example:

Request 1 → Server 1
Request 2 → Server 2
Request 3 → Server 3
Request 4 → Server 1

Each server gets requests equally in a circular order.

## API Testing

Open browser:

http://127.0.0.1:5000

The response will show which backend server handled the request.

## Concepts Implemented

- Flask REST API
- HTTP Request Forwarding
- Client-Server Communication
- Round Robin Scheduling
- Backend Server Management

## Future Improvements

- Add server health monitoring
- Add weighted load balancing
- Add database logging
- Add user interface dashboard
