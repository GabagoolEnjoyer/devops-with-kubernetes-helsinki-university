FROM python:3.11-alpine
WORKDIR /app
COPY /app/todo_app_server.py .
ENV PORT=8000
EXPOSE 8000
CMD ["python", "-u", "todo_app_server.py"]