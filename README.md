# Flask + React + Docker Starter

Starter repo for getting a React app up and running on a Flask server.
Additional scripts are provided for packaging the app into a docker container. 

## Installation

Install npm, nodejs and docker followed by:

```
npm i
npm run build
npm run docker
```

The last command only works if you're in the docker group (which isn't
recommended). After running the above, you should be able to have a server that prints "Hello World" on https://localhost:5000/ (note that the certificate is self-signed).
