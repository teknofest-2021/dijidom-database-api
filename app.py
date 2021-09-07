from flask import Flask, jsonify, request
import database

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['ENV'] = 'development'

@app.route('/api/database/pushDataToDatabase', methods=['POST'])
def pushDataToDatabase():
    print('[INFO]--[getImageBase64FromQR]--[FUNCTION]')
    stringData = request.form['stringData']
    dataList   = stringData.split('#')

    MeasurementDate = dataList[0].split('.')[0]
    PlantID         = dataList[1]
    SoilHumidity    = dataList[2]
    SoilTemperature = dataList[3]
    AirQuality      = dataList[4]
    Temperature     = dataList[5]
    Humidity        = dataList[6]

    response = database.pushSoilData(plantID=PlantID,soilHumidity=SoilHumidity,
                        soilTemperature=SoilTemperature,measurementDate=MeasurementDate)
    response = database.pushAmbientData(airQuality=AirQuality,temperature=Temperature,
                            humidity=Humidity,measurementDate=MeasurementDate)

    responseMessage = 'Could not write to database'
    if(response==True):
        responseMessage = 'Successfully written to database'

    return jsonify(
        {
            'measurementDate'   :   MeasurementDate,
            'PlantID'           :   PlantID,
            'soilHumidity'      :   SoilHumidity,
            'soilTemperature'   :   SoilTemperature,
            'AirQuality'        :   AirQuality,
            'Temperature'       :   Temperature,
            'Humidity'          :   Humidity,
            'Database Message'  :   responseMessage
        }
    )

@app.route('/api/test/getTest', methods=['GET'])
def getTest():
    print('[INFO]--[getTest]--[FUNCTION]')
    return jsonify('Test Successful')

@app.route('/api/test/getTestJenkins', methods=['GET'])
def getTestJenkins():
    print('[INFO]--[getTest]--[FUNCTION]')
    return jsonify('Test Successful for Jenkins')

@app.route('/', methods=['GET'])
def home():
    print('[INFO]--[home]--[FUNCTION]')
    homePage = '''
        <html>
    <head>
        <style>
            h1 {text-align: center;}
        </style>
    </head>
    <body>
        <h1>WELCOME TO THE DIJI-DOM DATABASE WEB API</h1>
    </body>
    </html>
    '''
    return homePage

@app.route('/favicon.ico')
def favicon():
    return 'None'
    
if __name__ == '__main__':
    app.run()
    