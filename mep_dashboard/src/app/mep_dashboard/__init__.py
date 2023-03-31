from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from app.mep_dashboard.config import Config
from app.lib.dscom.DatastoreCommunicator import DatastoreCommunicator
from app.mep_dashboard.config import itconfig
from app.lib.logger.ExpLogging import ExpLogging

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


# Initialisation of Logging
logger = ExpLogging(log_dir=Config.config['app.operations-mep-dashboard']['log_path'], log_name=Config.webapp_name,
                    daily_log=True, log_level="INFO").get_logging_object()

# Initialisation of Redis Data Store
datastore = DatastoreCommunicator(host=Config.datastore_host, port=Config.datastore_port,
                                  database=Config.datastore_database, keyspace=Config.datastore_keyspace, logg=logger)

# Get tickets data from Redis
keys_found = datastore.get_keys_by_pattern(pattern="MEP-*")
logger.info("Found %i tickets to scan for metadata" % len(keys_found))
key_list = ["application", "version", "classifier", "environment", "XLD", "CR", "CR:parent", "DMDB", "nexus",
            "classifier", "jira_application", "jira_format_ok", "nexus_exists"]
environment_map = {"Pre": "Environments/pre/Pre", "Stg": "Environments/staging/Staging",
                   "FDPre": "Environments/fdpre/FDPre", "FDProd": "Environments/fdprod/FDProd",
                   "Prod": "Environments/prod/Prod", "PFPre": "Environments/pfpre/PFPre", "UAT": "Environments/uat/UAT"}

from app.mep_dashboard.auth import auth, models

app.register_blueprint(auth, url_prefix='/auth')

from app.mep_dashboard.errors import errors
app.register_blueprint(errors)

from . import routes
