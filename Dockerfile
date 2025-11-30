FROM python:3.9-slim

WORKDIR /app
COPY app.py .

# Install runtime deps
RUN pip install flask

# Security best practice: non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]