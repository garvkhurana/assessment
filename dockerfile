FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app


COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=False

CMD ["streamlit", "run", "app.py"]
