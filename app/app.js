const express = require('express');
const users = require('../routes/users');
const videos = require('../routes/videos');
const path = require('path');
const app = express();

// app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Headers", "*");
    res.setHeader("Access-Control-Allow-Methods", "*");
    next();
});

// app.use((req, res, next) => {
//     console.log(req.headers);
// });

app.use('/api/users', users);
app.use('/api/videos', videos);

app.use((req, res, next) => {
    console.log('First MiddleWare');
    res.send('Some Shit yup');
});

module.exports = app;
