import logging


logger_configs = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "std_format": {
            "format": "[%(asctime)s %(name)s] [%(levelname)s] [%(module)s:%(funcName)s:%(lineno)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": logging.INFO,
            "formatter": "std_format",
        }
    },
    "loggers": {
        "app_logger": {
            "level": logging.INFO,
            "handlers": ["console"],
            "propagate": False
        },
    }
}
