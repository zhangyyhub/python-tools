import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


class logProcess:
    def __init__(self, logfile:str, when:str='D', interval:int=1, backupCount:int=30) -> None:
        """Initial configuration logging."""
        self.logfile     = logfile      # log file absolute path.
        self.when        = when         # cut in seconds, minute, hour, days.
        self.interval    = interval     # interval number.
        self.backupCount = backupCount  # backup number.

        logger_format = logging.Formatter("%(asctime)s[%(levelname)s] %(filename)s %(message)s", "%Y-%m-%d %H:%M:%S")
    
        self.logger = logging.getLogger("test")
        self.logger.setLevel(logging.INFO)

        time_handler = TimedRotatingFileHandler(
            self.logfile, 
            when=self.when, 
            interval=self.interval, 
            backupCount=self.backupCount, 
            encoding="utf-8",
            delay=False, 
            utc=True, 
            atTime=False
            )
        
        time_handler.setFormatter(logger_format)
        self.logger.addHandler(time_handler)

mylog = logProcess('/Users/zhang/datum/github/python-tools/logs/test.log')

# # test
# for _ in range(20):
#     mylog.logger.info("这是一个info信息")
#     time.sleep(1)
