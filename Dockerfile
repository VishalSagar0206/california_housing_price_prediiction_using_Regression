# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose default Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.enableCORS=false"]
