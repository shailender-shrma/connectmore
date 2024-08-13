# Django Application with Docker Containerization

This project is a Django-based web application containerized using Docker. The application includes two models:
1. **Mail Tracker**: Tracks user mail sending information.
2. **PDF Upload**: Allows users to upload PDF files.

## Features

- **Django Framework**: The web application is built using Django, a high-level Python web framework.
- **Docker Containerization**: The entire application is containerized with Docker, making it easy to deploy and manage.
- **CRUD Operations**: Implemented Create, Read, Update, and Delete (CRUD) functionality for:
  - Tracking user mail sending information.
  - Uploading and managing PDF files.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   
2. **build the project**
    docker-compose up --build
   
The application should be accessible at http://localhost:8000.

