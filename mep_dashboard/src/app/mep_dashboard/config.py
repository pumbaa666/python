import os

from app.lib.itconfig.sqexp_lib_itconfig import ITConfig

itconfig = ITConfig()


class Config(object):
    # Env variables
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bullshitkey'
    SECURITY_BLUEPRINT_NAME = os.environ.get('auth') or 'auth'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True

    # Config from itconfig
    config = itconfig.get_application_configs('operations-mep-dashboard')

    webapp_name = config['app.operations-mep-dashboard']['name']

    # Database config
    mysql_db_host = config['app.' + webapp_name]['MYSQL_HOST']
    mysql_db_name = config['app.' + webapp_name]['MYSQL_DATABASE']
    mysql_db_user = config['app.' + webapp_name]['MYSQL_USER']
    mysql_db_pass = config['app.' + webapp_name]['MYSQL_ROOT_PASSWORD']
    mysql_db_port = config['app.' + webapp_name]['MYSQL_PORT']

    # Database connection
    mysql_connection_string = ('mysql+pymysql://%s:%s@%s:%s/%s' % (mysql_db_user, mysql_db_pass, mysql_db_host,
                                                                   mysql_db_port, mysql_db_name))

    SQLALCHEMY_DATABASE_URI = mysql_connection_string

    # Config from itconfig
    config = itconfig.get_application_configs('operations-mep-dashboard')

    webapp_name = config['app.operations-mep-dashboard']['name']

    # Jira configuration
    jira_user = config['app.' + webapp_name]['jira.user']
    jira_pass = config['app.' + webapp_name]['jira.password']
    jira_server = config['app.' + webapp_name]['jira.server']
    jira_port = config['app.' + webapp_name]['jira.port']

    # Datastore (Redis) configuration
    datastore_host = config['datastore.deployment']['host']
    datastore_port = config['datastore.deployment']['port']
    datastore_database = config['datastore.deployment']['database']
    datastore_keyspace = config['datastore.deployment']['keyspace']

    # Connection AD
    ldap_host = config['app.' + webapp_name]['ldap_host']
    ldap_port = config['app.' + webapp_name]['ldap_port']
    ldap_suffix = config['app.' + webapp_name]['ldap_suffix']

    # XL Deploy lib configuration
    xldeploy_host = config['rest.xl-deploy']['host']
    xldeploy_port = config['rest.xl-deploy']['port']
    xldeploy_protocol = config['rest.xl-deploy']['protocol']
    xldeploy_context = config['rest.xl-deploy']['context']
    xldeploy_user = config['rest.xl-deploy']['username']
    xldeploy_password = config['rest.xl-deploy']['password']