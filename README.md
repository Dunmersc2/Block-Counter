# Block-Counter
A simple app to calcultate number of blocks required for a given area.

# Connecting docker build to database
```bash
sudo docker build -t block-counter .

sudo docker run -d -v "$(pwd)"/app:/app -p 5000:5000 --name block-counter block-counter

docker pull postgres

sudo docker run --name some-postgres -p 5433:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```