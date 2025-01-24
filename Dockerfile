FROM continuumio/miniconda3

WORKDIR /home/app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY Dashboard.py .

COPY pages/ ./pages/



CMD streamlit run ./Dashboard.py
