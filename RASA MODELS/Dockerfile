# Use an official Python runtime as a parent image
FROM python:3.9

# Sets the working directory in the Docker container
WORKDIR /app

# Copies the requirements.txt file from your local directory to the container
COPY requirements.txt ./

# Installs any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copies the rest of your local directory contents into the Docker container
COPY . .

# Specifies what command to run within the container
CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*", "--debug"]