FROM ho0707/front:1.0.2

ADD . .
RUN npm install

ENV NODE_ENV=production


EXPOSE 8080
ENTRYPOINT [ "npm", "run", "serve" ]
