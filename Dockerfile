# Use the official Python 3.11.9 image as the base image
FROM python:3.11.9

# Set the working directory in the container
WORKDIR /opt/zen

# Copy the rest of the application code into the container at /app
COPY . /opt/zen/

# Create and activate the virtual environment
RUN python3 -m venv myvenv && \
    /bin/bash -c "source myvenv/bin/activate"

# Install FastAPI, Uvicorn, SQLAlchemy, and mysql-connector-python
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy mysql-connector-python

# Expose port 80 to allow external access to the FastAPI application
EXPOSE 80

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

