const Movie = require('../models/movieModel');
const APIFeatures = require('../utils/apiFeatures');

exports.getMovies = async (req, res) => {
    try {
        const features = new APIFeatures(Movie.find(), req.query)
            .filter()
            .limitFields()
            .paginate()
            .sort();
        const movies = await features.query;
        res.status(200).json({
            'status': 'success',
            'results': movies.length,
            'data': {
                movies: movies
            }
        });
    } catch (err) {
        return res.status(400).json({
            'status': 'fail',
            'message': err
        });
    }
}

exports.createMovie = async (req, res) => {
    try {
        const newMovie = await Movie.create(req.body);
        res.status(200).json({
            'status': 'success',
            'data': {
                'movie': newMovie
            }
        });
    } catch (err) {
        res.status(400).json({
            'status': 'fail',
            'message': err
        });
    }
}
