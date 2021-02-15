FROM python:3.6
RUN pip install fastapi uvicorn
EXPOSE 80
COPY summarization-toolbox /app
WORKDIR /app
RUN sh install_dependencies.sh
COPY main.py main.py
COPY saved_model saved_model
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]