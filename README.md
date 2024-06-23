# HOW TO RUN THE APP

## First time (or after changes in Dockerfile)
1 Build Docker image and start the container `docker-compose up --build`

## Each time
1 Build and run the Docker cointainer `docker-compose up`
2 In your browser open `http://localhost:8000` to access the aplication
3 When finished stop Docker containers, simply pressing `Ctrl+C` or if that doesn't work, then `docker-compose down`