const gplay = require('google-play-scraper').memoized();
const fs = require('fs');

const convertToJson = (data, fileName) => {
  const JSONdata = JSON.stringify(data);

  fs.writeFile(fileName, JSONdata, (err) => {
    if (err) {
      throw err;
    }
    console.log("JSON data is saved.");
  });
}

const camelize = (str) => {
  return str.replace(/(?:^\w|[A-Z]|\b\w|\s+)/g, function (match, index) {
    if (+match === 0) return "";
    return index === 0 ? match.toLowerCase() : match.toUpperCase();
  });
}

const main = async (term, num = 5) => {
  const appData = await gplay.search({
    term,
    num,
    throttle: 10,
    country: 'in',
    fullDetail: true,
  })
  const fileName = camelize(term);
  convertToJson(appData, `${fileName}_${num}.json`);
}

main("PG", 50);