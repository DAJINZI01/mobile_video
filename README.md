## 抖音

### 1. 获取播放`url`的`json`数据

1. 请求的`url`

`https://aweme-hl.snssdk.com/aweme/v1/feed/`

2. 请求的方式

`get`

2. `headers`

```python
headers = {
    "User-Agent": "okhttp/3.10.0.1",
}
```

3. `query string`

```python
params = {
    "type": "0",
    "max_cursor": "0",
    "min_cursor": "0",
    "count": "6",
    "aweme_id": "id",
    "volume": "0.7333333333333333",
    "pull_type": "0",
    "need_relieve_aweme": "0",
    "filter_warn": "0",
    "req_from": "enter_auto",
    "cached_item_num": "0",
    "last_ad_show_interval": "-1",
    "ts": "1585487675",
    "app_type": "lite",
    "os_api": "23",
    "device_type": "MI 5s",
    "device_platform": "android",
    "ssmix": "a",
    "iid": "104392158277",
    "manifest_version_code": "290",
    "dpi": "270",
    "uuid": "490000000085156",
    "version_code": "290",
    "app_name": "douyin_lite",
    "cdid": "b20c68ce-2e2f-4b3e-a3b8-74b2e490df41",
    "version_name": "2.9.0",
    "openudid": "b8db9c78de7c82b5",
    "device_id": "70837664152",
    "resolution": "810*1440",
    "os_version": "6.0.1",
    "language": "zh",
    "device_brand": "Xiaomi",
    "ac": "wifi",
    "update_version_code": "2900",
    "aid": "2329",
    "channel": "tengxun",
    "_rticket": "1585487676509",
    "as": "a111111111111111111111",
    "cp": "a000000000000000000000",
    "mas": "",
}
```

## 火山小视频

### 1. 获得了一个视频`url`的`json`请求

通过这个`url`只能得到一个视频的`url`.

1. 请求的`url`

`https://hotsoon-hl.snssdk.com/hotsoon/item/video/_get/`

2. 请求的方式

`get`

3. 请求头

```python
headers = {
	"User-Agent": "ttnet okhttp/3.10.0.2",
}
```

4. 请求的参数: 经过分析只需要三个参数

```python
params = {
    "item_id": "6800228635925171471",  # 请求的视频的id
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
```

### 2. 主页的视频数据请求接口

1. 请求的`url`

`https://hotsoon-hl.snssdk.com/hotsoon/feed、`

2. 请求的方式

`get`

3. 请求头

```python
headers = {
	"User-Agent": "ttnet okhttp/3.10.0.2",
}
```

4. 请求参数

```python
params = {
    "type": "video",
    "tab_id": "5",
    "front_ids": "6809869449601109263%2C6809893253329095944%2C6808726733139889421%2C6801421644104617216%2C1634668034797582%2C6800306668589698304%2C6799054861905317135%2C6806037711485553924",
    "last_ad_items": "%5B%7B%22id%22%3A6803159557326654724%2C%22show_time%22%3A1585565114%7D%2C%7B%22id%22%3A6800667492667772173%2C%22show_time%22%3A1585565114%7D%2C%7B%22id%22%3A1662299439581208%2C%22show_time%22%3A1585565114%7D%2C%7B%22id%22%3A4760%2C%22show_time%22%3A1585565114%7D%2C%7B%22id%22%3A6805071744987188480%2C%22show_time%22%3A1585565181%7D%2C%7B%22id%22%3A6805102455383280908%2C%22show_time%22%3A1585565181%7D%2C%7B%22id%22%3A6804693165258460424%2C%22show_time%22%3A1585565182%7D%2C%7B%22id%22%3A6804840893229714695%2C%22show_time%22%3A1585565182%7D%2C%7B%22id%22%3A1662462880442372%2C%22show_time%22%3A1585567006%7D%5D",
    "n_viewed": "0",
    "offset": "18",
    "diff_stream": "1",
    "ad_user_agent": "com.ss.android.ugc.live%2F827+%28Linux%3B+U%3B+Android+6.0.1%3B+zh_CN%3B+MI+5s%3B+Build%2FV417IR%3B+Chrome%29",
    "req_from": "feed_loadmore",
    "count": "10",
    "secs_video_watching": "1811",
    "n_skipped": "0",
    "minor_control_status": "0",
    "feed_video_gap": "140",
    "max_time": "1585565187347",
    "live_sdk_version": "827",
    "iid": "104447577985",
    "device_id": "70837664152",
    "ac": "wifi",
    "channel": "tengxun_new",
    "aid": "1112",
    "app_name": "live_stream",
    "version_code": "827",
    "version_name": "8.2.7",
    "device_platform": "android",
    "ssmix": "a",
    "device_type": "MI+5s",
    "device_brand": "Xiaomi",
    "language": "zh",
    "os_api": "23",
    "os_version": "6.0.1",
    "uuid": "490000000085156",
    "openudid": "b8db9c78de7c82b5",
    "manifest_version_code": "827",
    "resolution": "810*1440",
    "dpi": "270",
    "update_version_code": "8270",
    "_rticket": "1585567014625",
    "ab_version": "1413809%2C1244214%2C889330%2C1138752%2C1589082%2C1063522%2C1480776%2C1377092%2C1380327%2C1582436%2C1588775%2C1167795%2C1476946%2C1404472%2C1517651%2C1354483%2C1479194%2C1258912%2C1264664%2C1521584%2C955276%2C1589846%2C947985%2C1548003%2C1182061%2C1480948%2C1435640%2C1477984%2C929432%2C1490515%2C1432944%2C1555350%2C1590375%2C1541253%2C1540549%2C1428670%2C1048435%2C1168129%2C1396601%2C1582073%2C1549345%2C1396899%2C1096187%2C1104584%2C1478759%2C1419023%2C1538832%2C1548270%2C1565149%2C1496674%2C1550828%2C1568912%2C1574488%2C1581133%2C1580160%2C1320817%2C1133591%2C692223%2C1169771%2C956107%2C1247692%2C1019139%2C682009%2C1032070%2C1165214%2C1265052%2C1584527%2C1072545%2C1317441%2C1562047%2C1069233%2C1583612%2C1143559%2C1544623%2C1337822%2C1293405%2C1347260%2C1046183%2C1354701%2C1143672%2C1498072%2C1143730%2C1417290%2C1491283%2C1165209%2C1576837%2C1376626%2C1572549%2C1409058%2C1502675%2C1578552%2C1050089",
    "client_version_code": "827",
    "jssdk_version": "1.37.1.2",
    "mcc_mnc": "46005",
    "cdid": "64d624fa-4514-401c-99d5-95e8a05b0c83",
    "new_nav": "1",
    "ws_status": "CONNECTED",
    "settings_version": "19",
    "last_update_time": "1585565111754",
    "mac_address": "08%3A00%3A27%3A3E%3A23%3A0D",
    "ts": "1585567014",
}
```

## 快手

### 1. 获取播放`url`的`json`数据

1. 请求的`url`

`https://apissl.gifshow.com/rest/n/feed/hot`

2. 请求方式

`post`

3. 请求头

```python
headers = {
	"User-Agent": "kwai-android aegon/1.10.2-curl",
}
```

4. 请求的参数

```python
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
```

5. `post`参数

```python
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
```



