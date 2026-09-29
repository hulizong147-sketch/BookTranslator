from loguru import logger
import sys, os

# 获取绝对目录
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log_dir = os.path.join(root_dir, "logs")

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

LOG_FILE = "translation.log"


class Logger:
    def __init__(self):
        log_file_path = os.path.join(log_dir, LOG_FILE)
        self.logger = logger
        self.logger.remove()

        # 控制台输出
        self.logger.add(sys.stdout, level='DEBUG',
                        format="<green>{time:YYYYMMDD HH:mm:ss}</green> | "
                               "{process.name} | "
                               "{thread.name} | "
                               "<cyan>{module}</cyan>.<cyan>{function}</cyan>"
                               ":<cyan>{line}</cyan> | "
                               "<level>{level}</level>: "
                               "<level>{message}</level>",
                        )
        # 输出到文件
        self.logger.add(log_file_path, level='DEBUG', encoding='UTF-8',
                        format='{time:YYYYMMDD HH:mm:ss} - '
                               "{process.name} | "
                               "{thread.name} | "
                               '{module}.{function}:{line} - {level} -{message}',
                        rotation="10 MB",
                        retention=20
                        )

    def get_logger(self):
        return self.logger


log = Logger().get_logger()
if __name__ == '__main__':
    log = Logger().get_logger()
    log.debug("这是一个BUDEG")
    log.info("这是一个info")
    log.warning("这是一个警告")
    log.trace("这是一个trace")