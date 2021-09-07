# DIJI-DOM DATABASE RESTAPIDocs

This repostory is about [DİJİ-DOM Database API](https://github.com/teknofest-2021/dijidom-database-api) and so the api will return
JSON responses.

Where full URLs are provided in responses they will be rendered as if service
is running on 'http://194.31.79.154:6066/'.

## Built with

* [Python](https://github.com/teknofest-2021/dijidom-database-api) - The backend API
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Used Framework
* No external libraries were used in this project

## Open Endpoints

Open endpoints require no Authentication.

### Similarity Rate Related

Each endpoint manipulates or displays information related to the image which provided:

* [pushDataToDatabase](readme/database/pushDataToDatabase.md) : `POST /api/database/pushDataToDatabase`

### API Test Related

* [getTest](readme/test/getImageList.md) : `GET /api/test/getTest`
* [getTestJenkins](readme/test/getImageBase64FromQR.md) : `GET /api/test/getTestJenkins`

## Authors

* **Fehmi Şener** - [Github](https://github.com/fehmiisener)

See also the list of [contributors](https://github.com/teknofest-2021/dijidom-database-api) who participated in this project.

## Acknowledgments

* Dear Teachers
* Teknofest Executives
* All Team Members
