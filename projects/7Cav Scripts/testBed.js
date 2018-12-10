// For testing things, not for official use.

function testRecord() {
  var ID = 2782;
  var HTML = UrlFetchApp.fetch('https://7cav.us/rosters/profile?uniqueid='+ID).getContentText();
  var output = {};
  
  try { // try...catch defines rawAwards if the trooper has no awards
    var rawAwards = HTML.match(/awardList.[\s\S]*?<\/table/i)[0].match(/<td.*?awardDate.[\s\S]*?<\/tr>/g);
  } catch(e) {
    var rawAwards = [];
  }
  
  output.awards = [];
  for (var aI in rawAwards) {
    Logger.log(aI);
    output.awards.push({
      date: new Date(rawAwards[aI].match(/awardDate..(.*)?<\//)[1]).toUTCString(),
      name: rawAwards[aI].match(/<td.*awardTitle..(.*)?<\/td>/)[1],
      details: rawAwards[aI].replace(/\s+|\n+/g, ' ').match(/awardDetails..(.*)?<\//)[1]
    });
  }
}



function testMilpac() {
  var ID = 2782;
  var tools = new siteTools().getMilpac(ID);
  
  Logger.log(JSON.stringify(tools.records))
}

function testBed() {
  var string = "This is a string";
  
  try {
    var match = string.match(/asd/i)[0];
  } catch(e) {
    var match = [];
  }
  
  Logger.log(match)
}