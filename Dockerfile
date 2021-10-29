FROM python:3.6
RUN pip install fastapi uvicorn
WORKDIR /app
COPY main.py main.py
EXPOSE 8000
CMD ["uvicorn", "--log-level", "trace", "--host", "0.0.0.0", "main:app"]