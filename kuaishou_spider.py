# coding=utf-8
from settings import BASE_DIR
from utils import download, name_manager

import requests
import os
import json


class KuaiShou(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "kwai-android aegon/1.10.2-curl",
            "Host": "apissl.gifshow.com",
            "Cookie": "region_ticket=RT_B5890E16417BC4E5595F7EDB6E188572806692681C8F352D1488433228783",
            "X-REQUESTID": "158562636964822384",
        }
        self.downloader = download.MyDownloader(bar_symbol="c")

    def get_info(self):
        """
        根据接口，获取所有的详细信息
        :return:
        """
        url = "https://apissl.gifshow.com/rest/n/feed/hot"
        params = {
            "mod": "vivo(vivo X9Plus)",
            "lon": "121.492379",
            "country_code": "cn",
            "extId": "bc70d48c39d1f18a8713e4cb3f8a800c",
            "kpn": "KUAISHOU",
            "oc": "360APP,1",
            "egid": "DFP058657B907ED8C6D9F0E270AAD8E19C6DF413211D9C0E53D8F775812D4F1F",
            "hotfix_ver": "",
            "sh": "1920",
            "appver": "7.2.2.12969",
            "socName": "UNKNOWN",
            "max_memory": "192",
            "isp": "CMCC",
            "kcv": "188",
            "browseType": "1",
            "kpf": "ANDROID_PHONE",
            "did": "ANDROID_c50c87e4562bf3f9",
            "net": "WIFI",
            "app": "0",
            "ud": "0",
            "c": "360APP,1",
            "sys": "ANDROID_5.1.1",
            "sw": "1080",
            "ftt": "",
            "ll": "CTTVk/lHPz9AES6PNSODX15A",
            "language": "zh-cn",
            "iuid": "",
            "lat": "31.247192",
            "did_gt": "1585622393761",
            "ver": "7.2",
        }
        form = {
            "type": "7",
            "page": "2",
            "coldStart": "false",
            "count": "20",
            "pv": "false",
            "id": "13",
            "refreshTimes": "1",
            "pcursor": "1",
            "source": "1",
            "extInfo": "TXURYODnxuqz8vLON/bBsj+X/NITG1FIT5ubnS+Bf39hSC0TLguH3XERnIrzRNPlxqxQcdIb58jND7AJFA6LgYnjjyDXznlJwi/wK8LxROT5tDiTQleU9pi/0VobR39E552kiUZ/aIMYbudUt7J/UQ==",
            "needInterestTag": "false",
            "seid": "f40304fb-d089-498a-91ad-ee6031186711",
            "volume": "0.27",
            "backRefresh": "false",
            "pageCount": "2",
            "adChannel": '{"type":1,"data":""}',
            "passThrough": "0",
            "thanosSpring": "false",
            "newUserRefreshTimes": "15",
            "newUserAction": '{"click":[5189835650000717127,5243315891402845228],"follow":[],"like":[]}',
            "cellList": '[{"ci":53185,"lac":6311,"mcc":460,"mnc":0,"radio":"gsm","rssi":0}]',
            "__NS_sig3": "2202972399d8693c1e9e2b081d7e7f5bc60c03c6dc",
            "client_key": "3c2cd3f3",
            "os": "android",
            "sig": "d695f07ae9d37816fdf4de698e659ab6",
        }
        return requests.post(url, params=params, data=form, headers=self.headers).json()

    def get_video_list(self):
        """
        获取视频列表
        :return: 列表 [{"caption": "xxx", "url": "xxx"}, ...]
        """
        data_list = self.get_info()["feeds"]
        video_list = []
        for data in data_list:
            if data.get("main_mv_urls"):  # 有的没有视频链接
                item = {
                    "caption": data["caption"],
                    "url": data["main_mv_urls"][0]["url"],
                }
                video_list.append(item)
        return video_list

    def download_video_list(self, folder="kuaishou"):
        """
        下载视频列表
        :param folder: 下载存放的文件夹
        :return:
        """
        # 1. 创建文件夹
        video_folder = "%s/%s" % (BASE_DIR, folder)
        if not os.path.exists(video_folder):
            os.mkdir(video_folder)
        # 2. 遍历视频列表，下载视频
        video_list = self.get_video_list()
        for video in video_list:
            file_name = "%s/%s.mp4" % (video_folder, video["caption"])
            file_name = name_manager.filter_name(file_name)
            # 3. 如果视频文件不存在则下载视频
            if not os.path.exists(file_name):
                self.downloader.download(video["url"], file_name)


if __name__ == '__main__':
    k = KuaiShou()
    # print(json.dumps(k.get_info(), ensure_ascii=False))
    # print(k.get_video_list())
    k.download_video_list()
