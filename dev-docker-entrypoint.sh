version: '3.9'
services:
  backend:
    build:
      context: .
      dockerfile: dev.Dockerfile
    ports:
      - "8000:8000"

