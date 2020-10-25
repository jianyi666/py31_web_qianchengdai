#_*_coding:utf-8 -*-
#@Time     :2020/10/2518:19
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :handle_config.py
#@Sotfware :PyCharm
from configparser import ConfigParser
from common.handle_path import C0NF_DIR
import os
class HandleConfig(ConfigParser):

    def __init__(self,filename,encoding='utf-8'):
        super().__init__()
        self.filename = filename
        self.encoding=encoding
        self.read(filename,encoding)

    def write_data(self,section,option,value):

        self.set(section,option,value)
        self.write(fp=open(self.filename,'w',encoding=self.encoding))

config = HandleConfig(os.path.join(C0NF_DIR,'config.ini'))


if __name__ == '__main__':

    print(config.get("class_party","BASE_URL"))

