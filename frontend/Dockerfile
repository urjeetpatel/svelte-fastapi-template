FROM node:15-buster
USER $USER
RUN mkdir -p /home/node/app
WORKDIR /home/node/app
COPY ./app/package*.json ./
RUN npm install
COPY ./app/ ./
EXPOSE 5000 35729
ENV HOST=0.0.0.0
CMD [ "npm","run","dev" ]
