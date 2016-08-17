var express = require('express');
var path = require('path');
var spawn = require("child_process").spawn;
var router = express.Router();


router.get('/', function(req, res) {
  res.render('record_form', { title: 'Express' });
});

router.post('/', function(req, res) {
  console.log(req.body);
    
  var countdown = req.body.countdown || 5;
  var scriptName = path.join(__dirname, '../../game0.py')
  console.log(scriptName);
  var python = spawn('python', [scriptName, countdown]);
  python.stdout.on('data', function (data) {
    console.log(data);
  });
  python.on('close', function (code) {
    console.log("exit with:" + code);
    res.render('record_start', { title: 'Done!' });
  });
});

module.exports = router;
