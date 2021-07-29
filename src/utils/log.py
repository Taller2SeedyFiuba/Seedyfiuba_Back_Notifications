from src.core.config import config

log = {
  'error': not ("LOG_ERROR" in config and config['LOG_ERROR'].lower() == 'false'),
  'warn': not ("LOG_WARN" in config and config['LOG_WARN'].lower() == 'false'),
  'info': not ("LOG_INFO" in config and config['LOG_INFO'].lower() == 'false'),
  'debug': not ("LOG_DEBUG" in config and config['LOG_DEBUG'].lower() == 'false'),
}

def logInfo(message):
  if (log['info']):
    print('Info: ' + message)


def logDebug(message):
  if (log['debug']):
    print('Debug: ' + message)

def logWarn(message):
  if (log['warn']):
    print('Warn: ' + message)


def logError(message):
  if (log['error']):
    print('Error: ' + message)

