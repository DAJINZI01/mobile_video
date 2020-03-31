# coding=utf-8
from settings import BASE_DIR
from utils import download, name_manager

import requests
import json
import os


class HuoShan(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "ttnet okhttp/3.10.0.2",
        }
        self.downloader = download.MyDownloader(bar_symbol="■")

    def get_item_info(self):
        url = "https://hotsoon-hl.snssdk.com/hotsoon/item/video/_get/"
        params = {
            "item_id": "6800228635925171471",
            # "live_sdk_version": "827",
            # "iid": "104447577985",
            # "device_id": "70837664152",
            # "ac": "wifi",  # 连接类型
            # "channel": "tengxun_new",
            # "aid": "1112",
            "app_name": "live_stream",  # app 名字
            # "version_code": "827",  # 版本代码
            # "version_name": "8.2.7",  # 版本名字
            # "device_platform": "android",  # 设备平台
            # "ssmix": "a",
            "device_type": "MI+5s",  # 设备类型
            # "device_brand": "Xiaomi",  # 设备品牌
            # "language": "zh",  # 语言
            # "os_api": "23",  # 操作系统api
            # "os_version": "6.0.1",  # 操作系统版本
            # "uuid": "490000000085156",
            # "openudid": "b8db9c78de7c82b5",
            # "manifest_version_code": "827",  # 清单版本代码
            # "resolution": "810*1440",  # 像素比例
            # "dpi": "270",  # 图像分辨率
            # "update_version_code": "8270",  # 更新版本代码
            # "_rticket": "1585566002578", # 请求 ticket
            # "ab_version": "1413809%2C1244214%2C889330%2C1138752%2C1589082%2C1063522%2C1480776%2C1377092%2C1380327%2C1582436%2C1588775%2C1167795%2C1476946%2C1404472%2C1517651%2C1354483%2C1479194%2C1258912%2C1264664%2C1521584%2C955276%2C1589846%2C947985%2C1548003%2C1182061%2C1480948%2C1435640%2C1477984%2C929432%2C1490515%2C1432944%2C1555350%2C1590375%2C1541253%2C1540549%2C1428670%2C1048435%2C1168129%2C1396601%2C1582073%2C1549345%2C1396899%2C1096187%2C1104584%2C1478759%2C1419023%2C1538832%2C1548270%2C1565149%2C1496674%2C1550828%2C1568912%2C1574488%2C1581133%2C1580160%2C1320817%2C1133591%2C692223%2C1169771%2C956107%2C1247692%2C1019139%2C682009%2C1032070%2C1165214%2C1265052%2C1584527%2C1072545%2C1317441%2C1562047%2C1069233%2C1583612%2C1143559%2C1544623%2C1337822%2C1293405%2C1347260%2C1046183%2C1354701%2C1143672%2C1498072%2C1143730%2C1417290%2C1491283%2C1165209%2C1576837%2C1376626%2C1572549%2C1409058%2C1502675%2C1578552%2C1050089",  # 版本
            # "client_version_code": "827",
            # "jssdk_version": "1.37.1.2", # js sdk 版本
            # "mcc_mnc": "46005",
            # "cdid": "64d624fa-4514-401c-99d5-95e8a05b0c83",
            # "new_nav": "1",
            # "ws_status": "CONNECTED", # 状态
            # "settings_version": "19",  # 配置版本
            # "last_update_time": "1585565111754",  # 上一次的更新时间
            # "ts": "1585566002",  # 请求的时间
        }
        data = requests.get(url, params=params, headers=self.headers).json()
        print(json.dumps(data, ensure_ascii=False))

    def get_info(self):
        url = "https://hotsoon-hl.snssdk.com/hotsoon/feed/"
        params = {
            "type": "video",
            # "tab_id": "5",
            # "front_ids": "6809869449601109263%2C6809893253329095944%2C6808726733139889421%2C6801421644104617216%2C1634668034797582%2C6800306668589698304%2C6799054861905317135%2C6806037711485553924",
            # "last_ad_items": "%5B%7B%22id%22%3A6803159557326654724%2C%22show_time%22%3A1585565114%7D%2C%7B%22id%22%3A6800667492667772173%2C%22show_time%22%3A1585565114%7D%2C%7B%22id%22%3A1662299439581208%2C%22show_time%22%3A1585565114%7D%2C%7B%22id%22%3A4760%2C%22show_time%22%3A1585565114%7D%2C%7B%22id%22%3A6805071744987188480%2C%22show_time%22%3A1585565181%7D%2C%7B%22id%22%3A6805102455383280908%2C%22show_time%22%3A1585565181%7D%2C%7B%22id%22%3A6804693165258460424%2C%22show_time%22%3A1585565182%7D%2C%7B%22id%22%3A6804840893229714695%2C%22show_time%22%3A1585565182%7D%2C%7B%22id%22%3A1662462880442372%2C%22show_time%22%3A1585567006%7D%5D",
            # "n_viewed": "0",
            # "offset": "18",
            # "diff_stream": "1",
            # "ad_user_agent": "com.ss.android.ugc.live%2F827+%28Linux%3B+U%3B+Android+6.0.1%3B+zh_CN%3B+MI+5s%3B+Build%2FV417IR%3B+Chrome%29",  # 添加 user-agent
            # "req_from": "feed_loadmore",  # 请求来源
            # "count": "10",
            # "secs_video_watching": "1811",
            # "n_skipped": "0",  # 跳过的数量
            # "minor_control_status": "0",  # 控制状态
            # "feed_video_gap": "140",  # 输出视频间隔
            # "max_time": "1585565187347",
            # "live_sdk_version": "827",
            # "iid": "104447577985",
            # "device_id": "70837664152",
            # "ac": "wifi",
            # "channel": "tengxun_new",
            "aid": "1112",  # 这个参数似乎很重要
            # "app_name": "live_stream",
            # "version_code": "827",
            # "version_name": "8.2.7",
            # "device_platform": "android",  # 设备平台
            # "ssmix": "a",
            # "device_type": "MI+5s",  # 设备类型
            # "device_brand": "Xiaomi",  # 设备品牌
            # "language": "zh",  # 语言
            # "os_api": "23",
            # "os_version": "6.0.1",
            # "uuid": "490000000085156",
            # "openudid": "b8db9c78de7c82b5",
            # "manifest_version_code": "827",
            # "resolution": "810*1440",
            # "dpi": "270",
            # "update_version_code": "8270",
            # "_rticket": "1585567014625",
            # "ab_version": "1413809%2C1244214%2C889330%2C1138752%2C1589082%2C1063522%2C1480776%2C1377092%2C1380327%2C1582436%2C1588775%2C1167795%2C1476946%2C1404472%2C1517651%2C1354483%2C1479194%2C1258912%2C1264664%2C1521584%2C955276%2C1589846%2C947985%2C1548003%2C1182061%2C1480948%2C1435640%2C1477984%2C929432%2C1490515%2C1432944%2C1555350%2C1590375%2C1541253%2C1540549%2C1428670%2C1048435%2C1168129%2C1396601%2C1582073%2C1549345%2C1396899%2C1096187%2C1104584%2C1478759%2C1419023%2C1538832%2C1548270%2C1565149%2C1496674%2C1550828%2C1568912%2C1574488%2C1581133%2C1580160%2C1320817%2C1133591%2C692223%2C1169771%2C956107%2C1247692%2C1019139%2C682009%2C1032070%2C1165214%2C1265052%2C1584527%2C1072545%2C1317441%2C1562047%2C1069233%2C1583612%2C1143559%2C1544623%2C1337822%2C1293405%2C1347260%2C1046183%2C1354701%2C1143672%2C1498072%2C1143730%2C1417290%2C1491283%2C1165209%2C1576837%2C1376626%2C1572549%2C1409058%2C1502675%2C1578552%2C1050089",
            # "client_version_code": "827",
            # "jssdk_version": "1.37.1.2",
            # "mcc_mnc": "46005",
            # "cdid": "64d624fa-4514-401c-99d5-95e8a05b0c83",
            # "new_nav": "1",
            # "ws_status": "CONNECTED",
            # "settings_version": "19",
            # "last_update_time": "1585565111754",
            # "mac_address": "08%3A00%3A27%3A3E%3A23%3A0D",
            # "ts": "1585567014",
        }
        data = requests.get(url, params=params, headers=self.headers).json()
        return data

    def get_video_list(self):
        data_list = self.get_info()["data"]
        video_list = []
        for data in data_list:
            item = {
                "url": data["data"]["video"]["download_url"][0],
                "title": data["data"]["title"]
            }
            video_list.append(item)
        return video_list

    def download_video_list(self, folder="huoshan"):
        """
        下载视频列表
        :param folder: 存放的文件夹, 默认为 ./BASE_DIR/huoshan
        :return:
        """
        # 1. 判断文件夹是否存在，不存在则创建
        video_folder = "%s/%s" % (BASE_DIR, folder)
        if not os.path.exists(video_folder):
            os.mkdir(video_folder)
        video_list = self.get_video_list()
        for video in video_list:
            file_name = "%s/%s.mp4" % (video_folder, video["title"])
            # 过滤文件名中的无效字符
            file_name = name_manager.filter_name(file_name)
            # 当文件不存在的时候进行下载
            if not os.path.exists(file_name):
                self.downloader.download(video["url"], file_name)

if __name__ == '__main__':
    h = HuoShan()
    # h.get_item_info()
    # print(json.dumps(h.get_info(), ensure_ascii=False))
    # print(h.get_video_list())
    for _ in range(10):
        h.download_video_list()
