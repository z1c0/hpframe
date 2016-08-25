var express = require('express');
var videos = require("../video");

var router = express.Router();

router.get('/', function(req, res) {
  res.render('index', {
    videos :  videos.getVideos(),
    title: 'Video List' }
  );
});

module.exports = router;
