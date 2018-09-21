import logging
import os
from utils.config import LOG_PATH
from logging.handlers import TimedRotatingFileHandler
from utils.config import Config


class Logger(object):
    def __init__(self, logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        c = Config().get('log')
        self.log_file_name = c.get('file_name') if c and c.get('file_name') else 'test.log'  # 有配置则取配置否则默认
        self.backup_count = c.get('backup') if c and c.get('backup') else 5
        self.console_output_level = c.get('console_level') if c and c.get('console_level') else'WARNING'
        self.file_output_level = c.get('file_level') if c and c.get('file_level') else 'DEBUG'
        pattern = c.get('pattern') if c and c.get('pattern') else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        """console_handle 输出到终端；
           file_handle    输出到文件。
        """
        if not self.logger.handlers:   # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.console_output_level)
            console_handler.setFormatter(self.formatter)
            self.logger.addHandler(console_handler)

            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                    when='D',     # 按天切割
                                                    interval=1,
                                                    backupCount=self.backup_count,     # 最多保留backup_count份
                                                    delay=True,
                                                    encoding='utf-8 '
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger


logger = Logger().get_logger()

