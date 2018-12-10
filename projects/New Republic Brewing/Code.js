function UTFB() {  
  var url = 'https://business.untappd.com/api/v1/sessions';
  const readKey = 'W4RN9bm5QdTDWCDtzTMK';
  const writeKey = 'os6813YdZ3tiYmDGyJWW';
  
  var payload = {
    'method': 'POST',
//    'contentType': 'application/json',
    'headers' : {
      'Content-Type': 'application/json'
    },
    'data': {
      'email': 'joshuakbell@gmail.com',
      'password': 'josh5271!'
    }
  };
  
  var response = UrlFetchApp.fetch(url, payload)
  
  
//  Logger.log(JSON.stringify(response));
  Logger.log(response)
}

function fuck() {
  Logger.log(UrlFetchApp.getRequest("https://business.untappd.com/api/v1/sessions"))
}