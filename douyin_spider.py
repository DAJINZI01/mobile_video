# coding=utf-8
from settings import BASE_DIR
from utils import download

import requests
import os
import json


class DouYin(object):
    def __init__(self):
        self.headers = {
            # "X-SS-REQ-TICKET": "1585487676447",
            # "sdk-version": "1",
            # "Cookie": "odin_tt=9c7ef2bb926863a0f8fcfb6d06532d569a6eb5cbfae6186b76f1046e269479630288340487398d82b9d4c346eefd7ecca0c1ae41aed65a51d1b92ea7cb381838; install_id=104392158277; ttreq=1$34c948237e9c5447e4a79e2b2a196db4e7845adb; sid_guard=3d396bfeb06b92101fc3d29c127172d9%7C1585486945%7C5184000%7CThu%2C+28-May-2020+13%3A02%3A25+GMT; uid_tt=acc78696ba27990a477b092ae95e900b; sid_tt=3d396bfeb06b92101fc3d29c127172d9; sessionid=3d396bfeb06b92101fc3d29c127172d9; qh[360]=1",
            # "x-tt-token": "003d396bfeb06b92101fc3d29c127172d9b13a081789d0d9f368f9890562fa422c1f58b29bf7c80257820fbb7382e8411f39",
            # "X-Gorgon": "0401c0d2400101345a666d88d3a4bf821513bbbee98c700d5efc",
            # "X-Khronos": "1585487676",
            # "Host": "aweme-hl.snssdk.com",
            "User-Agent": "okhttp/3.10.0.1", # 经过测试只需要这个 user-agent 头
        }
        self.downloader = download.MyDownloader(bar_symbol="*")

    def get_info(self):
        """
        获取播放数据的接口，很容易找到。
        返回的数据，如下:
        {
            "status_code":0,
            "min_cursor":0,
            "max_cursor":0,
            "has_more":1,
            "aweme_list":Array[6],
            "home_model":1,
            "refresh_clear":1,
            "extra":Object{...},
            "log_pb":Object{...},
            "preload_ads":Array[0],
            "preload_awemes":null
        }
        :return: 字典
        """
        url = "https://aweme-hl.snssdk.com/aweme/v1/feed/"
        params = {
            # "type": "0",
            # "max_cursor": "0",
            # "min_cursor": "0",
            # "count": "20",
            # "aweme_id": "id",
            # "volume": "0.7333333333333333",
            # "pull_type": "0",
            # "need_relieve_aweme": "0",
            # "filter_warn": "0",
            # "req_from": "enter_auto",
            "cached_item_num": "4",
            # "last_ad_show_interval": "-1",
            # "ts": "1585487675",
            # "app_type": "lite",
            # "os_api": "23",
            "device_type": "MI 5s",
            "device_platform": "android",
            # "ssmix": "a",
            # "iid": "104392158277",
            # "manifest_version_code": "290",
            # "dpi": "270",
            # "uuid": "490000000085156",
            "version_code": "290",
            "app_name": "douyin_lite",
            # "cdid": "b20c68ce-2e2f-4b3e-a3b8-74b2e490df41",
            # "version_name": "2.9.0",
            # "openudid": "b8db9c78de7c82b5",
            # "device_id": "70837664152",
            # "resolution": "810*1440",
            "os_version": "6.0.1",
            # "language": "zh",
            # "device_brand": "Xiaomi",
            # "ac": "wifi",
            # "update_version_code": "2900",
            # "aid": "2329",
            "channel": "tengxun",
            # "_rticket": "1585487676509",
            # "as": "a111111111111111111111",
            # "cp": "a000000000000000000000",
            # "mas": "",
        }
        return requests.get(url, params=params, headers=self.headers).json()

    def get_video_list(self):
        """
        获取播放视频的列表，每一个元素为 {"desc": "xxx", "play_addr": "xxx"}
        :return: 列表 [{"desc": "xxx", "play_addr": "xxx"}, ...]
        """
        aweme_list = self.get_info()["aweme_list"]
        video_list = []
        for aweme in aweme_list:
            item = {
                "desc": aweme["desc"],
                "play_addr": aweme["video"]["play_addr"]["url_list"][0],
            }
            video_list.append(item)
        return video_list

    def download_video_list(self, folder="douyin"):
        """
        从视频列表中下载视频
        :param video_list: 视频列表 [{"desc": "xxx", "play_addr": "xxx"}, ...]
        :param folder: 下载存放的位置, 默认为当前目录下的data文件夹
        :return:
        """
        video_list = self.get_video_list()
        # 1. 创建文件夹
        video_folder = "%s/%s" % (BASE_DIR, folder)
        if not os.path.exists(video_folder):
            os.mkdir(video_folder)
        # 2. 遍历视频列表下载文件
        for video in video_list:
            file_name = "%s/%s.mp4" % (video_folder, video["desc"])
            # 3. 当文件不存在的时候下载文件
            if not os.path.exists(file_name):
                self.downloader.download(video["play_addr"], file_name)


if __name__ == "__main__":
    d = DouYin()
    # print(json.dumps(d.get_info(), ensure_ascii=False))
    # print(d.get_video_list())
    for _ in range(10):
        d.download_video_list()