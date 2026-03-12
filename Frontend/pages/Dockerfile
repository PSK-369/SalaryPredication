FROM python:3.13.3
WORKDIR /main
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .
ENV Mydev=QA
EXPOSE 2001
CMD [ "python","-m","streamlit","run","./main.py","--server.address","0.0.0.0","--server.port","2001" ]