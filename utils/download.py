# coding=utf-8
from datetime import datetime, timedelta
import requests


class MyDownloader(object):
    def __init__(self, headers=None, progress_bar_len=30, bar_symbol="="):
        """
        下载器的初始化方法
        :param headers: 可以添加，下载要求的请求头，没有的话，使用自带的 user-agent 头
        :param progress_bar_len: 进度条的长度, 默认为 30
        :param bar_symbol: 进度条显示的符号，默认为 =
        """
        if not headers:
            self.headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            }
        self.progress_bar_len = progress_bar_len
        self.bar_symbol = bar_symbol

    def show_line(self, current_size, total_size, start_time):
        """
        显示一行的下载信息
        :param current_size: 当前下载的大小
        :param total_size: 总的文件大小
        :param start_time: 下载的开始时间
        :return:
        """
        # 进度条
        progress_percent = current_size / total_size # 进度百分比
        progress_bar = "[%s%s]" % (self.bar_symbol*int((self.progress_bar_len*progress_percent)),
                                   " "*int((self.progress_bar_len*(1-progress_percent))))
        # 百分比
        percent_bar = "%.2fM/%.2fM" % (current_size/1024/1024, total_size/1024/1024)
        # 时间
        # time_bar = time.strftime("%H:%M:%S", time.localtime(time.time()-start_time))
        time_bar = str(datetime.now() - start_time)
        print("\r%s %s %s" % (progress_bar, percent_bar, time_bar), end="")

    def download(self, url, file_name="out"):
        """
        下载器
        :param url: 下载的链接
        :param file_name: 下载的文件名, 如果没有传，使用out
        :return:
        """
        # 1. 发送请求
        response = requests.get(url, headers=self.headers, stream=True)
        # 2. 获取文件大小
        file_size = int(response.headers["Content-Length"])
        current_size = 0
        # 3. 读取文件写入到本地
        f = open(file_name, "wb")
        now = datetime.now()
        print("%s download..." % file_name)
        for chunk in response.iter_content(chunk_size=1024):
            current_size += f.write(chunk)
            self.show_line(current_size, file_size, now)
        f.close()
        print("[ok]")


if __name__ == '__main__':
    d = MyDownloader()
    # d.show_line(10000, 100000, datetime.now() - timedelta(seconds=10))
    url = "http://v3-default.ixigua.com/77d725434b95f0fede386b5d20cf7cab/5e81c988/video/tos/cn/tos-cn-v-0015c002/05464977975a46dabc084efb64806651/?a=0&br=0&bt=9960&cr=3&cs=0&dr=0&ds=3&er=&l=202003301727010101440620382F08CFD7&lr=all&qs=13&rc=anBxbGV5O2xzdDMzN2kzM0ApPHYzaHg1ZWQzZTMzOTM1eWc2cC1ici9fXi1fLS0zLS9zc2Rqa2ZfczVmbW4tLTFjLS06Yw%3D%3D&vl=&vr="
    d.download(url)

