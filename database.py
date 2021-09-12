import psycopg2

def pushNewPlantType(typeName):
    try:
        print('[INFO]--[pushNewPlantType]--[FUNCTION]')
        conn = psycopg2.connect(database = "DIJIDOM", user = "postgres", 
                                password = "passwrd", host = '194.31.79.154', 
                                port = '5432')
        cur = conn.cursor()
        sqlStr = '''INSERT INTO "DigitalTwin"."PlantTypes"("TypeID", "TypeName") VALUES (DEFAULT, %s);'''
        cur.execute(sqlStr,(typeName,));
        conn.commit()
        print('[INFO]--[pushNewPlantType]--[SUCCESSFUL]--[FUNCTION]')
        conn.close()
    except:
        return False

def pushNewPlant(plantName,plantTypeID,plantingDate):
    try:
        print('[INFO]--[pushNewPlant]--[FUNCTION]')
        conn = psycopg2.connect(database = "DIJIDOM", user = "postgres", 
                                password = "passwrd", host = '194.31.79.154', 
                                port = '5432')
        cur = conn.cursor()
        sqlStr = '''INSERT INTO "DigitalTwin"."Plants"("PlantID", "PlantName", "TypeID", "PlantingDate") VALUES (DEFAULT, %s, %s, %s);'''
        cur.execute(sqlStr,(plantName,plantTypeID,plantingDate));
        conn.commit()
        print('[INFO]--[pushNewPlant]--[SUCCESSFUL]--[FUNCTION]')
        conn.close()
    except:
        return False

def pushSoilsData(plantID,soilHumidity,soilTemperature,measurementDate):
    try:
        print('[INFO]--[pushSoilData]--[FUNCTION]')
        conn = psycopg2.connect(database = "DIJIDOM", user = "postgres", 
                                password = "passwrd", host = '194.31.79.154', 
                                port = '5432')
        cur = conn.cursor()
        sqlStr = '''INSERT INTO "DigitalTwin"."Soils"("SoilID", "PlantID", "SoilHumidity", "SoilTemperature", "MeasurementDate") VALUES (DEFAULT,%s, %s, %s, %s);'''
        cur.execute(sqlStr,(plantID,soilHumidity,soilTemperature,measurementDate));
        conn.commit()
        print('[INFO]--[pushSoilData]--[SUCCESSFUL]--[FUNCTION]')
        conn.close()
    except:
        return False

def pushAmbientsData(airQuality,temperature,humidity,measurementDate):
    try:
        print('[INFO]--[pushAmbientsData]--[FUNCTION]')
        conn = psycopg2.connect(database = "DIJIDOM", user = "postgres", 
                                password = "passwrd", host = '194.31.79.154', 
                                port = '5432')
        cur = conn.cursor()
        sqlStr = '''INSERT INTO "DigitalTwin"."Ambients"("AmbientID", "AirQuality", "Temperature", "Humidity", "MeasurementDate") VALUES (DEFAULT, %s, %s, %s, %s);'''
        cur.execute(sqlStr,(airQuality,temperature,humidity,measurementDate));
        conn.commit()
        print('[INFO]--[pushAmbientsData]--[SUCCESSFUL]--[FUNCTION]')
        conn.close()
        return True
    except:
        return False