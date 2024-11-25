# Base image
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port for the Gradio app
EXPOSE 7860

# Run the Gradio app
CMD ["python", "app/gradio_app.py"]
