FROM node:10-alpine

LABEL maintainer="mrpetrovic@outlook.com" version="1.0"

ENV YARN_VERSION 1.17.3

RUN apk add yarn

WORKDIR /usr/src/app

COPY ./package*.json ./

RUN yarn install

EXPOSE 8081

CMD ["node", "main.js"]
