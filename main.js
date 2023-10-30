const fs = require('fs');
const csv = require('csv-parser');

const data = [];

fs.createReadStream('base_de_donnees_clean.csv')
  .pipe(csv())
  .on('data', (row) => {
    // Process each row of data here
    data.push(row);
  })
  .on('end', () => {
    // Data processing or visualization code here
    console.log(data); // For demonstration, you can print the data
  });
