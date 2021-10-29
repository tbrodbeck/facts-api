FROM python:3.6
RUN pip install fastapi uvicorn
EXPOSE 80
WORKDIR /app
COPY main.py main.py
CMD ["uvicorn", "main:app"]