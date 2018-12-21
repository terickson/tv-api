from flask import Flask, request
from flask_cors import CORS
from lib import config, log
from werkzeug.exceptions import HTTPException
from routes.tv import tv_template
from flask_swagger_ui import get_swaggerui_blueprint
from lib.exlink import ExLink

try:
    c = config.Configuration('config.ini')
except Exception as e:
    exit()

fileLocation = None
log.setup_custom_logger(c.Logging.moduleName, c.Logging.level, fileLocation)
swaggerUiUrl = ''
swaggerDocUrl = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(swaggerUiUrl, swaggerDocUrl, config={'app_name': 'TV API', 'validatorUrl': None, 'layout': 'BaseLayout'})

app = Flask(__name__, static_url_path="/static")
cors = CORS(app)
app.tv = ExLink(c.TV.serialPort, c.TV.type)


@app.errorhandler(HTTPException)
def handle_bad_request(e):
    if not hasattr(e, 'code'):
        return str(e), 500
    elif e.code > 499:
        app.logger.error(e)
    return e


app.register_blueprint(tv_template, url_prefix='/tv')
app.register_blueprint(swaggerui_blueprint, url_prefix=swaggerUiUrl)

if __name__ == '__main__':
    app.run(debug=False, threaded=True, host='0.0.0.0', port=8080)
