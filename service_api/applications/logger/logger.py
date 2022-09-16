import logging.config

from service_api.applications.logger.logger_config import logger_configs


logging.config.dictConfig(logger_configs)
app_logger = logging.getLogger("app_logger")
