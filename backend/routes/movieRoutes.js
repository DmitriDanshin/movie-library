const express = require('express');
const movieController = require('../controllers/movieController');
const router = express.Router();

router.route('/')
    .get(movieController.getMovies)
    .post(movieController.createMovie);

module.exports = router;
