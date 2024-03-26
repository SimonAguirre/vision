import enum

class Purpose(enum.Enum):
        CONTINUE_PROCESS = 'continue process'
        UPDATE_PARAMETERS = 'update parameters'
        INITIALIZE = 'initialize'
        RETRY_REQUEST = 'retry request'
        STATUS_UPDATE = 'status update'
        START_ALL = 'start all components of pipeline'
        RESTART_CYCLE = 'restart worker cycle'
        UPDATE_DISPLAY = 'show image to viewport'