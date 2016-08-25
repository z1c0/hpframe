var path = require('path');
var moment = require('moment');
var fs = require('fs');
var config = require('./config');


module.exports = {
  getVideos : function() {
    var videos = [];
    console.log("getVideos: " + config.videoDir);
    var files = fs.readdirSync(config.videoDir);
    for (var i in files) {
      var f = files[i];
      var stats = fs.statSync(path.join(config.videoDir, f));
      if (!stats.isDirectory()) {
        //console.log(stats);
        videos.push({
          name : f,
          size : stats.size,
          created : moment(stats.birthtime).format('MMMM Do YYYY, h:mm:ss a')
        });
      }
    }    
    return videos;
  }
};