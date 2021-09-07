# Push Data To Database

Push Data which came from RasperyPI to Database

**URL** : `/api/database/pushDataToDatabase`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide Data String

```json
{
    "stringData" : "[unicode chars max] (Data which came from RasperyPI)"
}
```

**Data example** All fields must be sent.

```json
{
    "stringData" : "2021-08-27 15:27:22.853592#1#66.31#66.31#66.31#66.31#66.31"
}
```

## Success Response

**Condition** : If everything is OK and Server is UP.

**Code** : `200 SUCCESSFUL`

**Content example**

```json
{
    "measurementDate": "2021-08-27 15:27:22",
    "PlantID": "1",
    "soilHumidity": "66.31",
    "soilTemperature": "66.31",
    "AirQuality": "66.31",
    "Temperature": "66.31",
    "Humidity": "66.31",
    "Database Message": "Successfully written to database"
}
```

## Error Responses

**Condition** : If any database error. (May caused by dataString)

**Code** : `200 SUCCESSFUL`

```json
{
    "measurementDate": "2021-08-27 15:27:22",
    "PlantID": "1",
    "soilHumidity": "66.31",
    "soilTemperature": "66.31",
    "AirQuality": "66.31",
    "Temperature": "66.31",
    "Humidity": "66.31asd",
    "Database Message": "Could not write to database"
}
```