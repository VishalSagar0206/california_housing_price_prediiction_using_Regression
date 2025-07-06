# Dockerfile

FROM python:3.10-slim

WORKDIR /app

# Copy everything including model + .streamlit config
COPY . /app
COPY .streamlit /root/.streamlit
COPY artifacts /app/artifacts

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501"]

