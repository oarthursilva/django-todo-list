FROM postgres:9.6.18-alpine

RUN mkdir -p /docker-entrypoint-initdb.d
ADD db-init.sql /docker-entrypoint-initdb.d
