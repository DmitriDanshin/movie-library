const mongoose = require('mongoose')

const movieSchema = new mongoose.Schema({
    "name": {
        type: String,
        trim: true,
        required: [true, "A movie must has a name"],
    },
    "country": {
        trim: true,
        type: String,
        required: [true, "A movie must has a country"]
    },
    "year": {
        type: Number,
        default: null
    },
    "genres": {
        type: [String],
        default: []
    }
});

const Movie = mongoose.model('Movie', movieSchema);

module.exports = Movie;

