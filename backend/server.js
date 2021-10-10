const dotenv = require('dotenv');
const mongoose = require('mongoose');

dotenv.config({path: `${__dirname}/config.env`});

const app = require('./app');
const DB = process.env.DATABASE.replace('<PASSWORD>', process.env.DATABASE_PASSWORD);

mongoose.connect(DB, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})

const port = process.env.PORT ?? 3000;

app.listen(port, () => {
    console.log(`app running at http://localhost:${port}`);
});


