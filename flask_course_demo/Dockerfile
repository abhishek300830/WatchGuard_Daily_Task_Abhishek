FROM python
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
# first dot is about flask_course_demo and second dot is about working directory
COPY . . 
CMD [ "flask","run","--host","0.0.0.0" ] 