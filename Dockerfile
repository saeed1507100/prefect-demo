# Use Prefect image as a base
FROM prefecthq/prefect:2.18-python3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in container
WORKDIR /usr/src/app

# Copy local code to the container image
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt