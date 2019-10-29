const {ObjectId} = require('mongodb');

const express = require('express');
const path = require('path');
const formidable = require('formidable');
const router = express.Router();
const fs = require('fs');
const checkIfAuthenticated = require('../middlewares/checkIfAuthenticated');
const dbClient = require('../app/db-manager');

router.get('/', (req, res) => {
    console.log(req.query.id);
    let path;
    dbClient.client.connect((err, client) => {
        console.log("Connected to database");

        const db = client.db("cpd");
        console.log("Switched to database cpd");

        db.collection('videos', (err, collection) => {
            collection.findOne({
                _id: ObjectId(req.query.id),
            }, {
                projection: {path: 1, _id: 0}
            }).then((vid_path) => {
                // console.log(vid_path);
                path = vid_path.path;
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
                client.close().then(() => {
                    console.log("Closed Connection to database",);
                }, () => {
                    console.log("Error closing connection to database");
                });
            });
        });
    });
    // const path = './assets/sample.mp4';

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
            dbClient.client.connect((err, client) => {
                console.log("Connected to database");

                const db = client.db("cpd");
                console.log("Switched to database cpd");


                const python = require('child_process').spawn(
                    'python',
                    // second argument is array of parameters, e.g.:
                    [path.join(__dirname, '../utils/thumb-maker.py')
                        , path.join(__dirname, '../assets', file.name)
                        , file.name]
                );
                let output = "";
                python.stdout.on('data', function(data){ output += data });
                python.on('close', (code) => {
                    if (code !== 0) {
                        res.status(500).json({
                            result: false,
                            message: 'File list not retrieved successfully'
                        });
                    }

                    db.collection('videos').insertOne({
                        path: file.path,
                        user_id: req.user.sub,
                        thumbnail_name: output.trim()
                    }).then((result) => {
                        // console.log(file);

                        client.close().then(() => {
                            console.log("Closed Connection to database",);
                        }, () => {
                            console.log("Error closing connection to database");
                        });

                        res.status(200).json({
                            result: true,
                            message: 'File list retrieved successfully',
                            // something: output
                        });
                    });
                });

            });

        })
        .on('aborted', () => {
            console.error('Request aborted by the user');
        })
        .on('error', (err) => {
            console.error('Error', err);
            throw err;
        })
        .on('end', () => {

            // res.json({
            //     result: true,
            //     message: 'File Uploaded Successfully'
            // });
        })
});

router.get('/all', checkIfAuthenticated, (req, res) => {
    dbClient.client.connect((err, client) => {
        console.log("Connected to database");

        const db = client.db("cpd");
        console.log("Switched to database cpd");

        db.collection('users', (err, collection) => {
            collection.findOne({
                _id: ObjectId(req.user.sub),
            },{
                projection: {_id: 1}
            }).then((userId) => {
                if (!userId) {
                    res.status(400).json({
                        result: false,
                        message: 'Please enter correct details'
                    })
                } else {
                    console.log(userId._id.toString());
                    db.collection('videos', (err, collection) => {
                        collection.find({
                            user_id: userId._id.toString()
                        }).project({
                            _id: 1, thumbnail_name: 1
                        }).toArray().then((videos) => {
                            if (videos.length < 1) {
                                res.status(200).json({
                                    result: true,
                                    message: 'Please add a video first'
                                });
                            } else {
                                res.status(200).json({
                                    result: true,
                                    message: 'Here are your videos',
                                    videos: videos
                                })
                            }
                            client.close().then(() => {
                                console.log("Closed Connection to database",);
                            }, () => {
                                console.log("Error closing connection to database");
                            });
                        })
                    });
                }

            });
        });

    });
});

module.exports = router;


// const {PythonShell} = require('python-shell');
//
// var options = {
//     mode: 'text',
//     pythonPath: 'python',
//     pythonOptions: ['-u'],
//     scriptPath: 'C:\\Users\\Pawan\\Desktop\\color-pigment-delineate\\backend\\utils',
//     args: [path.join(__dirname, '../utils/thumb-maker.py'),
//         'C:\\Users\\Pawan\\Desktop\\color-pigment-delineate\\backend\\assets\\sample.mp4']
// };
//
// PythonShell.run('thumb-maker.py', options, function (err, results) {
//     if (err) {
//         console.log(err);
//         throw err;
//     }
//
//     // Results is an array consisting of messages collected during execution
//     console.log('results: %j', results);
// });
