
import  logging
import os
from logging.handlers import TimedRotatingFileHandler
from common.handle_path import FUTURE_LOAN_LOGS_DIR

def crate_logs():
    # 创建日志收集器
    log = logging.getLogger("jianyi")
    # 设置日志收集等级
    log.setLevel("INFO")

    # 创建时间轮转的文件输出渠道
    fh = TimedRotatingFileHandler(filename=os.path.join(FUTURE_LOAN_LOGS_DIR,"logs.log"),
                                  when='d',
                                  interval=7,
                                  backupCount=3,
                                  encoding="utf-8")
    # 创建到控制台的输出渠道
    sh = logging.StreamHandler()

    # 设置日志输出等级
    fh.setLevel("INFO")
    sh.setLevel("INFO")

    # 将输出渠道添加到收集器
    log.addHandler(fh)
    log.addHandler(sh)
    # 日志输出的格式
    formats = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
    mate = logging.Formatter(formats)
    fh.setFormatter(mate)
    sh.setFormatter(mate)
    return log

log = crate_logs()

