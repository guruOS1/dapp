FROM continuumio/anaconda3

RUN pip3 install flasgger

WORKDIR /app
COPY app.py /app/app.py
EXPOSE 5000
COPY model/logreg.pkl /app/model/logreg.pkl

CMD ["python3", "app.py"]