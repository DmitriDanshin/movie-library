const express = require('express');

const app = express();

const movieRouter = require('./routes/movieRoutes')

app.use(express.json());
app.use(express.static(`${__dirname}/public`));

app.use("/api/v1/movies", movieRouter);

module.exports = app;
