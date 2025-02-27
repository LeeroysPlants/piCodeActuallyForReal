const express = require('express'); 
const bodyParser = require('body-parser'); 
const app = express(); 
const port = 3000

var waterPlant = false; 
app.use(bodyParser.urlencoded({extended:true})); 

app.get('/', (req, res) => {
  console.log("main route called"); 
  res.send('Hello World!')
})

app.post('/data', (req, res) => {
  console.log("post route called"); 
  const currentTime = req.body.time
  const waterLevel = req.body.waterLevel; 
  const soilMoisture = req.body.soilMoisture; 
  const temperature = req.body.temperature; 
  const humidity = req.body.humidity;
  console.log("Sensor Data: \n" +"Current Time: " + currentTime + "\n Water Level: " + waterLevel + "\n Soil Moisture: " + soilMoisture + "\n Temperature: " + temperature + "\n Humidity: " + humidity); 
  res.send("data read!"); 
});

app.get('/waterPlantButtonPressed', (req, res) =>{
  if(waterPlant = true){
    console.log("button pressed while water plant was true"); 
  }
  waterPlant = true; 
  res.send("Plant will be watered shortly!"); 
}); 
app.get('/doesPiNeedToWaterPlant', (req, res) => {
  console.log("pi hit endpoint"); 
  res.send(waterPlant); 
  if(waterPlant){
    waterPlant = false; 
    console.log("plant was watered"); 
  }
}); 

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})


