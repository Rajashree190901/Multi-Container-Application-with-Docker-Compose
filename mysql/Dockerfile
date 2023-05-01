FROM mysql:latest 
COPY ./db.sql /docker-entrypoint-initdb.d/
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=student_db
EXPOSE 3306
