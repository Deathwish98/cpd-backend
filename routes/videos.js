const express = require('express');
const path = require('path');
const formidable = require('formidable');
const router = express.Router();
const fs = require('fs');
const checkIfAuthenticated = require('../middlewares/checkIfAuthenticated')

router.get('/', (req, res) => {
    const path = './assets/sample.mp4';
    const stat = fs.statSync(path);
    const fileSize = stat.size;
    const range = req.headers.range;

    if (range) {
        const parts = range.replace(/bytes=/, "").split("-");
        const start = parseInt(parts[0], 10);
        const end = parts[1]
            ? parseInt(parts[1], 10)
            : fileSize-1;

        const chunksize = (end-start)+1;
        const file = fs.createReadStream(path, {start, end});
        const head = {
            'Content-Range': `bytes ${start}-${end}/${fileSize}`,
            'Accept-Ranges': 'bytes',
            'Content-Length': chunksize,
            'Content-Type': 'video/mp4',
        };

        res.writeHead(206, head);
        file.pipe(res);
    } else {
        const head = {
            'Content-Length': fileSize,
            'Content-Type': 'video/mp4',
        };
        res.writeHead(200, head);
        fs.createReadStream(path).pipe(res);
    }
});

router.post('/new', checkIfAuthenticated, (req, res) => {
    console.log(req.user);
    new formidable.IncomingForm().parse(req)
        .on('fileBegin', (name, file) => {
            file.path = path.join(__dirname, '../assets/', file.name);
        })
        .on('field', (name, field) => {
            console.log('Field', name, field);
        })
        .on('file', (name, file) => {
            // console.log('Uploaded file', name, file);

        })
        .on('aborted', () => {
            console.error('Request aborted by the user');
        })
        .on('error', (err) => {
            console.error('Error', err);
            throw err;
        })
        .on('end', () => {
            res.json({
                result: true,
                message: 'File Uploaded Successfully'
            });
        })
});

module.exports = router;
