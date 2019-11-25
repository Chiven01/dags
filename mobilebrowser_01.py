#!/usr/bin/python
# -*- coding: utf-8 -*-

u"""
### 文档
这里可以写上此产品的长篇描述，
使用markdown语法书写哦~
"""

from airflow import DAG
from airflow import utils
from airflow.operators.bash_operator import BashOperator
from datetime import datetime,timedelta

default_args = {
    'owner': 'chenxianxin',
    'email': ['chenxianxin@sogou-inc.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'execution_timeout': timedelta(hours=23),
    'depends_on_past': True,
    'start_date': utils.dates.days_ago(0)
}

dag = DAG(
    'mobilebrowser_01',
    concurrency = 32,
    default_args = default_args,
    description = u'搜狗手机浏览器',
    schedule_interval = "@daily"
)
dag.doc_md = __doc__

env = {'HIVE_CONF_DIR':'mobilebrowser','HADOOP_CONF_DIR':'mobilebrowser'}

DecodeLogFlow_day = BashOperator(
dag = dag,
env = env,
task_id = 'DecodeLogFlow_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/DecodeLogFlow_day',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
run.sh,decode preday raw log
""")

SplitLogFiles = BashOperator(
dag = dag,
env = env,
task_id = 'SplitLogFiles',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/SplitFiles',
bash_command ='sleep 120',
schedule_interval = '24 1 * * *',
doc_md = u"""
rely on preday result of task DecodeLogFlow_day of this dag
result:android and ios ,sdk and others client log.
notice:coding is gbk, it's history problem
""")

SplitLogFiles_android = BashOperator(
dag = dag,
env = env,
task_id = 'SplitLogFiles_android',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/SplitFiles',
bash_command ='sleep 120',
schedule_interval = '24 1 * * *',
doc_md = u"""
rely on preday result of task DecodeLogFlow of dag mobilebrowser_hour.py
result:android and ios ,sdk and others client log.
notice:coding is gbk, it's history problem
""")

SplitLogFiles_ios = BashOperator(
dag = dag,
env = env,
task_id = 'SplitLogFiles_ios',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/SplitFiles',
bash_command ='sleep 120',
schedule_interval = '24 1 * * *',
doc_md = u"""
rely on preday result of task DecodeLogFlow of dag mobilebrowser_hour.py
result:android and ios ,sdk and others client log.
notice:coding is gbk, it's history problem
""")

SplitLogFiles_sdk = BashOperator(
dag = dag,
env = env,
task_id = 'SplitLogFiles_sdk',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/SplitFiles',
bash_command ='sleep 120',
schedule_interval = '24 1 * * *',
doc_md = u"""
rely on preday result of task DecodeLogFlow of dag mobilebrowser_hour.py
result:android and ios ,sdk and others client log.
notice:coding is gbk, it's history problem
""")

SplitLogFiles_others = BashOperator(
dag = dag,
env = env,
task_id = 'SplitLogFiles_others',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/SplitFiles',
bash_command ='sleep 120',
schedule_interval = '24 1 * * *',
doc_md = u"""
rely on preday result of task DecodeLogFlow of dag mobilebrowser_hour.py
result:android and ios ,sdk and others client log.
notice:coding is gbk, it's history problem
""")

dau_newer = BashOperator(
dag = dag,
env = env,
task_id = 'dau_newer',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/dau_newer',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
result:${DAU_PATH_NEW},${HISTORIER_NEW},${NEWER_PATH_NEW}
""")

MovePhp_UserStat = BashOperator(
dag = dag,
env = env,
task_id = 'MovePhp_UserStat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/allUserStat',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
产生老的日活文件和30天留存数据等
result:import/dau_old
mysql:android_versionUid_stat_new,android_channelUid_stat_new,android_firstChannelUid_stat_new,versionUid_stat_new,channelUid_stat_new
""")


mse_20161227_version_pv_uv_config = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161227_version_pv_uv_config',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/20161227_version_pv_uv_config',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
mysql:mse_version_pvuv_stat2_new
""")

mse_20190128_sysversion_pv_uv_config = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20190128_sysversion_pv_uv_config',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/20190128_sysversion_pv_uv_config',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
mysql:mse_sysversion_pvuv_stat2_new
""")

MovePhp_NewerRetainRate = BashOperator(
dag = dag,
env = env,
task_id = 'MovePhp_NewerRetainRate',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/userStatUpdate',
bash_command ='sleep 120',
schedule_interval = '0 2 * * *',
doc_md = u"""
update table (android_versionUid_stat_new,android_channelUid_stat_new,android_firstChannelUid_stat_new,versionUid_stat_new,channelUid_stat_new) some columns
result:${IMPORT_PATH}/semobnewretain/daily,${IMPORT_PATH}/semobnewretain/newerdaily
""")

mse_alltype_dauretain = BashOperator(
dag = dag,
env = env,
task_id = 'mse_alltype_dauretain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_alltype_dauretain',
bash_command ='sleep 120',
schedule_interval = '0 7 * * *',
doc_md = u"""
relay on DAU_PATH_NEW
dau retain
plat:ios and android;
type:version,sysversion,fchannel,channel
mysql:plat_alltype_survive_uid_dau
update plat_channel_stat_new,plat_version_stat_new set retain1,retain7,retain30 where plat='ios'
""")

adjustAllNewRetain_combine = BashOperator(
dag = dag,
env = env,
task_id = 'adjustAllNewRetain_combine',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/adjustAllNewRetain',
bash_command ='sleep 120',
schedule_interval = '0 2 * * *',
doc_md = u"""
mysql:plat_version_stat_new,plat_channel_stat_new,plat_fchannel_stat_new
and  UPDATE android_channelUid_stat_new a,plat_channel_alive_new b SET a.dayFirsInstallCount_final_history=b.install ...
""")

adjustAllNewRetain_alive = BashOperator(
dag = dag,
env = env,
task_id = 'adjustAllNewRetain_alive',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/adjustAllNewRetain',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
mysql:plat_version_alive_new,plat_fchannel_alive_new,plat_channel_alive_new
""")

adjustAllNewRetain_survive = BashOperator(
dag = dag,
env = env,
task_id = 'adjustAllNewRetain_survive',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/adjustAllNewRetain',
bash_command ='sleep 120',
schedule_interval = '15 2 * * *',
doc_md = u"""
mysql:plat_version_survive_new,plat_fchannel_survive_new,plat_channel_survive_new
""")


mse_novel_sdk_verratio = BashOperator(
dag = dag,
env = env,
task_id = 'mse_novel_sdk_verratio',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_novel_sdk_verratio',
bash_command ='sleep 120', 
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:novel_sdk_version_ratio
result:/user/mobilebrowser/import/novel_sdk_history
""")

mse_android_GetAndroidSdkMiniLog = BashOperator(
dag = dag,
env = env,
task_id = 'mse_android_GetAndroidSdkMiniLog',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/AndroidSdkMiniLog',
bash_command ='sleep 120',
schedule_interval = '50 0 * * *',
doc_md = u"""
android sdkmini log parse
result:${sdkmini}/sdkmini
""")

mse_sdk_allObjectPingBack2 = BashOperator(
dag = dag,
env = env,
task_id = 'mse_sdk_allObjectPingBack2',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_sdk_allObjectPingBack2',
bash_command ='sleep 120',
schedule_interval = '45 1 * * *',
doc_md = u"""
mysql:sdk_android_windows2_new,sdk_android_notshown_new
""")

mse_SdkPushDesktopClick = BashOperator(
dag = dag,
env = env,
task_id = 'mse_SdkPushDesktopClick',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_SdkPushDesktopClick',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
mysql:semob_all_tbl_push_desktop_total_new,semob_android_tbl_TipsSpread_adjust_new
""")

minibrowser = BashOperator(
dag = dag,
env = env,
task_id = 'minibrowser',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/minibrowser',
bash_command ='sleep 120',
schedule_interval = '40 0 * * *',
doc_md = u"""
生成mini浏览器的历史用户文件和新用户文件
result:mini_browser/history_user  and    mini_browser/new_user
""")

mse_minibasicdata = BashOperator(
dag = dag,
env = env,
task_id = 'mse_minibasicdata',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_minibasicdata',
bash_command ='sleep 120',
schedule_interval = '43 0 * * *',
doc_md = u"""
taurus表路径：商业业务>手机浏览器>手机浏览器 - 新Mini浏览器统计（输入法）>新mini浏览器H5页面-用户数统计
mysql:mse_minibasicdata_new
""")

mse_android_resolutionnwer_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_android_resolutionnwer_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20141218_mse_resolutionnwer_stat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器android版本新用户的分辨率统计，对应的绿皮为【手机浏览器 - android status统计】-【新增用户设备分辨率】；
mysql数据表为resolution_new_user
""")

mse_Movephp_allValuesPingBacksByChannel = BashOperator(
dag = dag,
env = env,
task_id = 'mse_Movephp_allValuesPingBacksByChannel',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/MovePhp/allValuesPingBacksByChannel',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器android与ios客户端数值型pingback参数按照渠道的统计，对应的绿皮为【手机浏览器 - 搜索推荐插件】
mysql数据库为：android_mse_channel_stat
""")

mse_newusers_deviceManagement = BashOperator(
dag = dag,
env = env,
task_id = 'mse_newusers_deviceManagement',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_newusers_deviceManagement',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
推广数据,功能统计
mysql:mse_deviceManagement
""")

mse_20161104_search_word_stats = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161104_search_word_stats',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20161104_search_word_stats',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
20161104_search_word_stats
mysql:mse_yuying_search_word
""")

mse_20161212_SDK_jiesuan = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161212_SDK_jiesuan',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20161212_SDK_jiesuan',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
20161212_SDK_jiesuan
手机浏览器SDK-结算页
mysql:mse_sdk_channel_install_stats
""")

mse_20161226_uuid_distribution = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161226_uuid_distribution',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/datasprite/20161226_uuid_distribution',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
绿皮 》 手机浏览器-Android Status统计 》  A/B Test 用户划分数据:http://grape.sogou-inc.com/analysisapply/showapplyinfo.do?id=9b57027466594b78a58c4e10058d9b0a
mysql:mse_uuid_distribution_stats
""")

mse_20161229_status_stats = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161229_status_stats',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/datasprite/20161229_status_stats',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
20161229_status_stats
手机浏览器-Android Stauts统计项目中 【新增用户】、【使用用户数】的定义
http://grape.sogou-inc.com/analysisapply/showapplyinfo.do?id=73404b300a3544ffad3b9a83d6046c2e
mysql:mse_status_stats
""")

mse_20170110_mse_abtest_1_7alive_stats = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20170110_mse_abtest_1_7alive_stats',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/datasprite/20170110_mse_abtest_1_7alive_stats',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器 - 资讯沉浸模式ABtest 基础统计报表 
mysql:mse_abtest_bases_stats
""")

mse_20161021_mse_1_30installretains = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161021_mse_1_30installretains',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/20161021_mse_1_30installretains',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_fchannel_reserved_install_survive
""")

mse_120_install_retains = BashOperator(
dag = dag,
env = env,
task_id = 'mse_120_install_retains',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_120_install_retains',
bash_command ='sleep 120',
schedule_interval = '0 9 * * *',
doc_md = u"""
mysql:mse_fchannel_reserved_install_survive_120
""")


mse_fchannel_retains_alert = BashOperator(
dag = dag,
env = env,
task_id = 'mse_fchannel_retains_alert',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170224_channelretains_alert',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_fchannel_retains_alert
""")

mse_lockscreen_retain_android = BashOperator(
dag = dag,
env = env,
task_id = 'mse_lockscreen_retain_android',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_lockscreen_retain_android',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
taurus表：商业业务>手机浏览器>手机浏览器 - 推送通知统计>锁屏消息对留存率影响统计（路径下所有表）
mysql表：mse_lockscreen_retain_android
依赖：日活文件
""")

mse_groupbysufuid_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'mse_groupbysufuid_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_groupbysufuid_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
taurus表：商业业务>手机浏览器>手机浏览器-信息流数据>按尾号分组的两张表
mysql：mse_groupbysufuid_pvuv
依赖：日活文件
""")

mse_timeconsuming_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'mse_timeconsuming_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_timeconsuming_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
taurus表：商业业务>手机浏览器>手机浏览器-信息流数据>耗时数据汇总-Android-v5.9.2
mysql表：mse_timeconsuming_pvuv
""")

mse_newsfeed_ver = BashOperator(
dag = dag,
env = env,
task_id = 'mse_newsfeed_ver',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_newsfeed_ver',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
taurus路径：商业业务>手机浏览器>手机浏览器-信息流数据>分版本数据-Android-v1.1  && 分版本数据-iOS-v1.1
mysql表：mse_newsfeed_ver
""")

mse_newsfeed_region = BashOperator(
dag = dag,
env = env,
task_id = 'mse_newsfeed_region',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_newsfeed_region',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
taurus报表：商业业务>手机浏览器>手机浏览器-信息流数据>分地域数据-Android  && 分地域数据-iOS
mysql：mse_newsfeed_region
""")

mse_newspush_uid_abtest = BashOperator(
dag = dag,
env = env,
task_id = 'mse_newspush_uid_abtest',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_newspush_uid_abtest',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
taurus表：商业业务>手机浏览器>手机浏览器-信息流数据>push实验数据>个性化push-ab实验（分组用户数据）
mysql表：mse_newspush_uid_abtest
""")

mse_zixunnews_c_fc = BashOperator(
dag = dag,
env = env,
task_id = 'mse_zixunnews_c_fc',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_zixunnews_c_fc',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
taurus表：商业业务>手机浏览器>手机浏览器-信息流数据>列表页展现点击数据Android-分原始渠道 && 列表页展现点击数据Android-分渠道
mysql表：mse_zixunnews_c_fc
""")

#mse_SdkPushDesktopClick1 = BashOperator(
#dag = dag,
#env = env,
#task_id = 'mse_SdkPushDesktopClick1',
#svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/mse-PushDesktopClick',
#bash_command ='sleep 120',
#schedule_interval = '40 6 * * *',
#doc_md = u"""
#description:是小p手浏日活的数据，和任务mse_SdkPushDesktopClick重复，迁移完成后应该被删除.
#sdk的关于手机搜狐、搜狗、腾讯的统计，相关绿皮为热词推广-手机搜狐、搜狗搜索、腾讯网。
#对应的数据表为semob_android_tbl_TipsSpread_adjust、semob_all_tbl_push_desktop_total
#""")

mse_Movephp_StatPingBacks = BashOperator(
dag = dag,
env = env,
task_id = 'mse_Movephp_StatPingBacks',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/MovePhp/allStatePingBacks',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
重构手浏统计中状态类PingBack的统计，包含安卓以及ios
mysql:android_tbl_AnecdoteContentVisitUrl,android_tbl_AnecdoteRecommendUrl,android_tbl_AnecdoteRecommendVisitCount,android_tbl_NewsSettingStatus,android_tbl_NotificationStatus,android_tbl_NovelSettingStatus,android_tbl_PingBackDeviceBrand,android_tbl_PingBackHardwareVersion,android_tbl_PingBackHomeNovelFoldStatus,android_tbl_PingbackInputUrl,android_tbl_PingBackKeyExpressSearchKey,android_tbl_PingBackKeyExpressSearchKeyKeyword,android_tbl_PingBackKeyQuickLaunchVisitUrl,android_tbl_PingBackKeySearchKeyword,android_tbl_PingBackMenuSlippageStatus,android_tbl_PingBackNaviTableVisitUrl,android_tbl_PingbackNetworkStatus,android_tbl_PingBackNewAddrBarSearchKeyword,android_tbl_PingbackNewAddrBarVisitUrl,android_tbl_PingBackNovelDetailVisualSettingColorStatus,android_tbl_PingBackNovelDetailVisualSettingFontStatus,android_tbl_PingBackPushNotificationGetID,android_tbl_PingBackQuickLaunchAddURL,android_tbl_PingBackScreenResolution,android_tbl_PingBackSettingAdblockStatus,android_tbl_PingBackSettingAutoFillFormStatus,android_tbl_PingBackSettingCookiesStatus,android_tbl_PingBackSettingDefaultBrowserStatus,android_tbl_PingBackSettingDownLoadAddrStatus,android_tbl_PingBackSettingExpressAddRemindStatus,android_tbl_PingBackSettingExpressRefreshStatus,android_tbl_PingBackSettingGeneralSniffStatus,android_tbl_PingBackSettingGestureStatus,android_tbl_PingBackSettingNetworkDownloadRemindStatus,android_tbl_PingBackSettingNewsRemindStatus,android_tbl_PingBackSettingParallelDownloadRemindStatus,android_tbl_PingBackSettingPlayerStatus,android_tbl_PingBackSettingRestoreTabStatus,android_tbl_PingBackSettingSearchEngineStatus,android_tbl_PingBackSettingSearchSuggestionStatus,android_tbl_PingBackSettingSlippageStatus,android_tbl_PingBackSettingStealthStatus,android_tbl_PingBackSettingUAStatus,android_tbl_PingBackSettingUserExperiencePlanstatus,android_tbl_PingBackShareUrlAndTarget,android_tbl_PingBackSystemVersion,android_tbl_seleted_theme,android_tbl_SettingCleanStatus,android_tbl_SettingMarketUpdateStatus,android_tbl_VitamioVersion,tbl_AnecdoteContentVisitUrl,tbl_PingBackAccountAutoFillFormSyncStatus,tbl_PingBackAccountBookmarkSyncStatus,tbl_PingBackAccountHistorySyncStatus,tbl_PingBackAccountNoteSyncStatus,tbl_PingBackAccountSyncModeStatus,tbl_PingBackFavouriteVisitUrl,tbl_PingBackHardwareVersion,tbl_PingBackHomeNovelFoldStatus,tbl_PingbackInputUrl,tbl_PingBackKeyInputAlertSelection,tbl_PingBackKeyQuickLaunchVisitUrl,tbl_PingBackKeySearchKeyword,tbl_PingBackMenuNoPictureStatus,tbl_PingBackNaviTableVisitUrl,tbl_PingbackNetworkStatus,tbl_PingBackNewAddrBarSearchKeyword,tbl_PingBackNovelDetailVisualSettingColorStatus,tbl_PingBackNovelDetailVisualSettingFontStatus,tbl_PingBackQuickLaunchSwitchCategoryStatus,tbl_PingBackReadCenterInformationDetailVisualSettingColorStatus,tbl_PingBackReadCenterInformationDetailVisualSettingFontStatus,tbl_PingBackScreenResolution,tbl_PingBackSettingAutoFillFormStatus,tbl_PingBackSettingCookiesStatus,tbl_PingBackSettingExpressAddRemindStatus,
tbl_PingBackSettingExpressRefreshStatus,tbl_PingBackSettingInputStatus,tbl_PingBackSettingNetworkDownloadRemindStatus,tbl_PingBackSettingParallelDownloadRemindStatus,tbl_PingBackSettingRestoreTabStatus,tbl_PingBackSettingSearchEngineStatus,tbl_PingBackSettingSearchSuggestionStatus,tbl_PingBackSettingStealthStatus,tbl_PingBackSettingUserExperiencePlanstatus,tbl_PingBackSettingWebNewsRemindStatus,tbl_PingBackSystemVersion,tbl_seleted_theme
""")

mse_20161220_version_abtest_top500 = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161220_version_abtest_top500',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/datasprite/20161220_version_abtest_top500',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
20161220_version_abtest_top500
URL点击统计新表（top500）
pingback：安卓端：InformChannelContentVisitNewClick   ios端：InformChannelContentVisitClick   （频道：name  标题：title  url：url）
mysql:mse_version_abtest_urltop500_stats
""")

'''
#xiaxian
mse_navitable_countandretain_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_navitable_countandretain_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20141010_chenggang_semob_navitable_stat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
网址大全各分类中按钮、内容、地址以及相关留存率的统计（android以及ios），对应绿皮中的【手机浏览器 - 网址大全统计】,
对应数据表为semob_all_tbl_navitable_stat
import_path:$IMPORT_PATH/semobnavi_retain/daily
""")
'''

mse_20161224_version_abtest_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161224_version_abtest_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/datasprite/20161224_version_abtest_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
20161224_version_abtest_pvuv
mysql:mse_version_abtest_pvuv_stats
""")

mse_new_version_fchannel_information = BashOperator(
dag = dag,
env = env,
task_id = 'mse_new_version_fchannel_information',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/datasprite/mse_new_version_fchannel_information',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mse_new_version_fchannel_information
按原始渠道号统计pingback的pv,uv
更新数据库表：mse_pages_fchannel_stat
""")

mse_pushflow_dis_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_pushflow_dis_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170502_pushflow_dis_stat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器android版本关于下发条数的分布，对应的绿皮为所有项目>商业业务>手机浏览器>手机浏览器 - 推送通知统计>新Android推送通知统计>展示通知条数的用户分布（5.3.1以上版本）,
对应的mysql数据表为：android_tbl_pings_dis_stat
""")

mse_translator_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'mse_translator_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_translate_pvuv_count',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
全文翻译的功能统计
mysql:mse_translate_pvuv_count
""")

mse_newsconsume_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'mse_newsconsume_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_newsconsume_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
taurus表：商业业务>手机浏览器>手机浏览器-信息流数据>消费数据汇总-Android--v1.1  &&  商业业务>手机浏览器>手机浏览器-信息流数据>消费数据汇总-iOS--v1.1
mysql表：mse_newsconsume_pvuv
""")

mse_iqiyicoopration_anroid = BashOperator(
dag = dag,
env = env,
task_id = 'mse_iqiyicoopration_anroid',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_iqiyicoopration_anroid',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
taurus表：爱奇艺合作评估数据
mysql：mse_iqiyicoopration_anroid
""")

mse_GetguanwangLog = BashOperator(
dag = dag,
env = env,
task_id = 'mse_GetguanwangLog',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/GetGuanwangLog',
bash_command ='sleep 120',
schedule_interval = '20 2 * * *',
doc_md = u"""
获取手机手机浏览器官网日志
result:${IMPORT_PATH}/novel/"$logDate"mseGuanwangLog
""")

mse_20161216_mse_reading_stats = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161216_mse_reading_stats',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/datasprite/20161216_mse_reading_stats',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mse_20161216_mse_reading_stats
一级页面统计，阅读数据
mysql:mse_reading_stats
""")

mse_novel_msesogoucom_total = BashOperator(
dag = dag,
env = env,
task_id = 'mse_novel_msesogoucom_total',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/mse_novel_msesogoucom_total',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mse.sogou.com官网访问的统计，绿皮显示为手机浏览器-小说中心统计，
对应的mysql数据库为guanwang_pl
""")

mse_novel_all_movenovel_visitUserStat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_novel_all_movenovel_visitUserStat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20141229_MoveNovelCenter/visitUserStat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
 手机浏览器android、ios版本小说中心、阅读页详细页的统计。对应绿皮为【手机浏览器 - 小说中心统计】-【总访问量统计，v3,v3】。对应mysql数据表为novel_total_access_count（v2,v3）
mysql:novel_total_access_count,novel_total_access_count_v3,novel_total_access_count_v2
""")

mse_novel_all_movenovel_valuesPagesStat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_novel_all_movenovel_valuesPagesStat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20141229_MoveNovelCenter/valuesPagesStat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器android、ios版本小说中心、阅读页详细页的统计。对应绿皮为【手机浏览器 - 小说中心统计】,多列数值的统计项
mysql:novel_homepage,novel_readpage,novel_banner_statistic,novel_channel_recommend1,novel_recom_more,novel_bottom_recom,novel_recommend
""")

mse_novel_all_movenovel_catePagesStat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_novel_all_movenovel_catePagesStat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20141229_MoveNovelCenter/catePagesStat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器android、ios版本小说中心、阅读页详细页的统计。对应绿皮为【手机浏览器 - 小说中心统计】,包含所有分类的统计
mysql:novel_cate_page_click,novel_discovery_page,novel_discovery_book_top50,novel_search_page,novel_top500query,novel_detail_page,novel_hot_top500
""")

mse_20160930_cooperation_guanwang_stats = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20160930_cooperation_guanwang_stats',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20160930_cooperation_guanwang_stats',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
官网服务器 各合作方访问数
mysql:mse_push_stats_guanwang_coop
""")

mse_novelgidcount_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'mse_novelgidcount_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_novelgidcount_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_novelgidcount_pvuv
""")

mse_sdk_20151215_mengwei_sdkfloat_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_sdk_20151215_mengwei_sdkfloat_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20151215_mengwei_sdkfloat_stat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器mini在图标展示、常驻通知栏、悬浮图标三种调起行为下对应的行为以及搜索词统计。对应的绿皮为[手机浏览器 - mini浏览器统计]、[手浏热词推广 - 常驻置顶通知栏]、[手浏热词推广 - 桌面悬浮图标]下【用户行为数据】>、【地址栏搜索词】
对应mysql表格为：sdkmini_orig_tbl_PingBackSDKAddrBarSearchKeyword、sdkmini_mse_stat_floating
""")

mse_sdkmini_calls_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_sdkmini_calls_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20160105_mengwei_mini_calls_stat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器sdkmini版本三种调起方式的统计，对应的绿皮为：【手机浏览器 - mini浏览器统计】-【mini浏览器主动日活统计】，
对应的mysql数据库为：sdkmini_mse_stat_mini_calls
""")

mse_SdkMiniStat_allValuesPingBacks = BashOperator(
dag = dag,
env = env,
task_id = 'mse_SdkMiniStat_allValuesPingBacks',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/SdkMiniStat/allValuesPingBacks',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器sdk-mini版本数值型参数统计，对应的绿皮为【手机浏览器 - mini浏览器统计】，
对应的mysql数据表格为：sdkmini_mse_stat
""")

sdk_uninstall_stat = BashOperator(
dag = dag,
env = env,
task_id = 'sdk_uninstall_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20140825_mengwei_uninstall_stat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
安卓按渠道卸载率统计
mysql:semob_android_tbl_uninstall
""")

semob_android_status_rate = BashOperator(
dag = dag,
env = env,
task_id = 'semob_android_status_rate',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/semob_android_status_rate',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
用户网络、硬件版本的比例统计
mysql:android_tbl_PingbackNetworkStatus,android_tbl_PingBackScreenResolution,android_tbl_PingBackHardwareVersion,android_tbl_PingBackSystemVersion,android_tbl_NotificationStatus,android_tbl_VitamioVersion. for these table's rate column.
""")

PingbackCompetingAppName_stat = BashOperator(
dag = dag,
env = env,
task_id = 'PingbackCompetingAppName_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/PingbackCompetingAppName',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
根据Pingback判断app名称（qq,uc等）的统计
mysql:semob_android_competing_app
""")

novel_center_user_stat = BashOperator(
dag = dag,
env = env,
task_id = 'novel_center_user_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/novel_center_user_stat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:novel_center_user_count
""")

mse_novel_retain_rate = BashOperator(
dag = dag,
env = env,
task_id = 'mse_novel_retain_rate',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/mse_novel_retention',
bash_command ='sleep 120',
schedule_interval = '50 9 * * *',
doc_md = u"""
计算小数中心总体以及阅读页的留存率统计，绿皮显示为手机浏览器-小说中心统计，对应的mysql数据库为novel_retention
""")

semob_all_tbl_novel_shelf_stat = BashOperator(
dag = dag,
env = env,
task_id = 'semob_all_tbl_novel_shelf_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20141015_linweiguo_novel_bookshelf_stat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:semob_all_tbl_novel_shelf_stat
""")

mse_android_wakeupqunicklunch_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_android_wakeupqunicklunch_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20141215_mse_wakeup_stat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器安卓版本的唤醒相关统计，以及同时访问快速访问与网址大全的统计。相应的绿皮为：【手机浏览器 - android用户数】- 外部调起人数次数、【手机浏览器 - android功能统计】- 同时访问快速访问与网址大全的统计；对应的
mysql:tbl_pingback_app_wakeup_count,quick_launch_web_all_inter
""")

mse_alll_CatesAll_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_alll_CatesAll_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20150610_linweiguo_CatesAll_retian',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器渠道分类汇总统计
mysql:android_firstchannelCate_stat,android_semob_channel_wxf,android_semob_channel_linhaisheng,android_semob_channel_huangyang,android_semob_channel_songlianzi,android_semob_channel_chenhao,android_semob_channel_lijingjing,android_mse_channel_stat_bds,android_channelUid_wxfpay_stat
""")

mse_mininavi_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_mininavi_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20150803_mengwei_mininavi_stat',
bash_command ='sleep 120',
schedule_interval = '59 8 * * *',
doc_md = u"""
mini浏览器页面导航统计，对应的数据库表名为sdkmini_tbl_NaviUrl
""")

mse_SdkMiniStat_allUserStat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_SdkMiniStat_allUserStat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/SdkMiniStat/allUserStat',
bash_command ='sleep 120',
schedule_interval = '14 8 * * *',
doc_md = u"""
""")

mse_all_appsdownload_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_all_appsdownload_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20150428_liubo_appsdownload',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器应用下载统计，对应的绿皮为【手机浏览器 - 应用下载】，对应mysql数据库为：mse_all_appsdownload_stat
""")

mse_20170116_mse_1_30aliveretains_chidongfang_huice = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20170116_mse_1_30aliveretains_chidongfang_huice',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/datasprite/20170116_mse_1_30aliveretains_chidongfang_huice',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_huice_alive_survive
""")

mse_ads_showclick_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_ads_showclick_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170313_ads_showclick_stat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_ads_showclicks_check
""")

mse_hijackdownloadappincome_android = BashOperator(
dag = dag,
env = env,
task_id = 'mse_hijackdownloadappincome_android',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_hijackdownloadappincome_android',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
统计劫持下载流量相关指标
mysql:mse_hijackdownloadappincome_android,app_price,mtool_download_jiechi
""")

mse_20160905_mse_1_30installretains = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20160905_mse_1_30installretains',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20160905_mse_1-30installretains',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
按原始渠道新增留存
mysql:mse_daily_channel_install_survive
""")

mse_20160905_mse_1_30aliveretains = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20160905_mse_1_30aliveretains',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20160905_mse_1-30aliveretains',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
活跃留存
mysql:mse_daily_channel_alive_survive
""")

mse_bds_channels_data = BashOperator(
dag = dag,
env = env,
task_id = 'mse_bds_channels_data',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170303_bds_channels_data',
bash_command ='sleep 120',
schedule_interval = '38 9 * * *',
doc_md = u"""
手机浏览器各商业业务部商务数据进行汇总，相应的数据从超级白皮获取。对应的绿皮为【手机浏览器 - android用户数】-【android手机浏览器渠道分类汇总】-【外购数据统计】
mysql:android_firstchannel_bds_stat,plat_fchannel_stat_jingjia
""")

mse_channel_class_stats = BashOperator(
dag = dag,
env = env,
task_id = 'mse_channel_class_stats',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_channel_class_stats',
bash_command ='sleep 120',
schedule_interval = '09 8 * * *',
doc_md = u"""
mysql:mse_channel_class_stats,mse_channel_class_stats_op_all,mse_channel_class_stats_op_class,mse_channel_class_stats_subchannel,mse_fchannel_type,mse_channel_bygroup
update:plat_fchannel_stat_new.type_name
""")

mse_channel_full_infos = BashOperator(
dag = dag,
env = env,
task_id = 'mse_channel_full_infos',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_channel_full_infos',
bash_command ='sleep 120',
schedule_interval = '00 2 * * *',
doc_md = u"""
mysql表:生成渠道相关信息，供其他任务使用mse_channel_full_infos
""")

#semob_android_chenjinabtest_fchannelneweretains = BashOperator(
#dag = dag,
#env = env,
#task_id = 'semob_android_chenjinabtest_fchannelneweretains',
#svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170511_chenjin_abtest_1-30newerretains',
#bash_command ='sleep 120',
#schedule_interval = '50 10 * * *',
#doc_md = u"""
#mysql:semob_android_chenjinabtest_fchannelneweretains
#""")

mse_channel_information_uvpv = BashOperator(
dag = dag,
env = env,
task_id = 'mse_channel_information_uvpv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_channel_information_uvpv',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_channel_uvpv_stat1
""")

mse_detailads_show_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_detailads_show_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170516_ads_show_stat',
bash_command ='sleep 120',
schedule_interval = '0 6 * * *',
doc_md = u"""
手机浏览器详情页广告展现与点击的统计，对应的绿皮统计表格为【商业业务>手机浏览器>手浏-运营数据-质量监控>新版-渠道质量分析】，对应的数据表为：mse_channel_uvpv_stat1，日志来源为客户端日志以及ping.hotspot.ie.sogou.com/zixun.gif的日志
mysql:mse_channel_uvpv_stat1, update this table
""")

mse_android_allchannels_newerlogoretains_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_android_allchannels_newerlogoretains_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20160121_mengwei_allchannels_logoretains',
bash_command ='sleep 120',
schedule_interval = '49 1 * * *',
doc_md = u"""
mysql:手机浏览器android版本按原始渠道号统计绝对新增7日点击图标主动留存,logo_retain of plat_fchannel_stat_new && android_firstChannelUid_stat_new
""")

mse_20161205_mse_1_60installretain = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161205_mse_1_60installretain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20161205_mse_1_60installretain',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_channel_class_op_survive_class
""")

mse_zixun_server_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_zixun_server_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170328_zixun_server_stat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_zixun_server_stat
""")

mse_20160125_taoge_1_30newerretains = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20160125_taoge_1_30newerretains',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20160125_taoge_1-30newerretains',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:semob_android_tbl_monthall_neweretains
""")

Semob_antiFakeSDKLog = BashOperator(
dag = dag,
env = env,
task_id = 'Semob_antiFakeSDKLog',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/anticheating_mobilebrowser/semobAntiFakeLog',
bash_command ='sleep 120',
schedule_interval = '00 2 * * *',
doc_md = u"""
semob，反作弊sdk log解析，json格式
result:$IMPORT_PATH/antifake_log
""")

semob_channelUvIp_jinchenxi = BashOperator(
dag = dag,
env = env,
task_id = 'semob_channelUvIp_jinchenxi',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/anticheating_mobilebrowser/semobChannelIp',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器渠道ip分布，用于手浏反作弊
mysql:mse_android_uvip
""")

mse_all_GetIosBrushlLog = BashOperator(
dag = dag,
env = env,
task_id = 'mse_all_GetIosBrushlLog',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/GetIosBrushlLog',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
result:${LOG_CLIENT}/iosbrush
rely on:/cloud/dt/pingback/ping/djt-pb-log/iosbrush
""")

mse_iosbrush_lanmao_retain = BashOperator(
dag = dag,
env = env,
task_id = 'mse_iosbrush_lanmao_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170203_ioslanmao_stat',
bash_command ='sleep 120',
schedule_interval = '30 1 * * *',
doc_md = u"""
mysql:semob_iosbrush_tbl_monthall_neweretains
""")

mse_ioslanmao_pings_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_ioslanmao_pings_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170213_ioslanmao_pings_stat',
bash_command ='sleep 120',
schedule_interval = '40 1 * * *',
doc_md = u"""
mysql:semob_iosbrush_pings_stat
result:${IMPORT_PATH}/lanmaoping/history,${IMPORT_PATH}/hotmobi/history
""")

mse_android_effectiveuser_channel = BashOperator(
dag = dag,
env = env,
task_id = 'mse_android_effectiveuser_channel',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/effective_user_channel_android',
bash_command ='sleep 120',
schedule_interval = '30 2 * * *',
doc_md = u"""
mysql:semob_android_effective_user
result:${IMPORT_PATH}/effectiveuser/tmp,${IMPORT_PATH}/effectiveuser/history
""")

mse_new_cost_zixun = BashOperator(
dag = dag,
env = env,
task_id = 'mse_new_cost_zixun',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_new_cost_zixun',
bash_command ='sleep 120',
schedule_interval = '50 8 * * *',
doc_md = u"""
产生mysql表mse_new_cost_zixun，替代任务mse_zixun_cash_stat，接口改为营销部门提供（约定为7点前提供），之前为奇点提供
relay on :crontab task salesData_rsync (everyday 8:00)
""")

mse_search_pids_cash_rpm = BashOperator(
dag = dag,
env = env,
task_id = 'mse_search_pids_cash_rpm',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170224_search_pid_cash',
bash_command ='sleep 120',
schedule_interval = '0 8 * * *',
doc_md = u"""
手机浏览器搜索收益的统计，通过向营销部门龙晨旭获取pv和消耗数据并导入绿皮。对应的绿皮项目为【手浏-运营数据-搜索收益】，对应的mysql数据表为【semob_all_search_rpm_pids】
""")

semob_dailyAntiCheats_jinchenxi = BashOperator(
dag = dag,
env = env,
task_id = 'semob_dailyAntiCheats_jinchenxi',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/anticheating_mobilebrowser/semobDailyAntiCheats',
bash_command ='sleep 120',
schedule_interval = '50 2 * * *',
doc_md = u"""
手浏实时反作弊任务，rom、imei、aid、分辨率特征一块处理，处理结果放入手浏绿皮数据.
update android_channelUid_stat_new, set fakecount,fakenewer,effective_fakecount,dayFirstInstallCount_final_history_fake
""")

semob_SDKDailyAntiCheats_chemsjim = BashOperator(
dag = dag,
env = env,
task_id = 'semob_SDKDailyAntiCheats_chemsjim',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/anticheating_mobilebrowser/semobDailySdkAntiCheats',
bash_command ='sleep 120',
schedule_interval = '55 2 * * *',
doc_md = u"""
手机浏览器反作弊SDK实时反作弊任务。
""")

mobilebrowser_kpi_data_load_again = BashOperator(
dag = dag,
env = env,
task_id = 'mobilebrowser_kpi_data_load_again',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_ime/kpi_push',
bash_command ='sleep 120',
schedule_interval = '0 3 * * *',
doc_md = u"""
补传手机浏览器日激活量数据到小P
""")

plat_fchannel_stat = BashOperator(
dag = dag,
env = env,
task_id = 'plat_fchannel_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/plat_fchannel_stat',
bash_command ='sleep 120',
schedule_interval = '50 2 * * *',
doc_md = u"""
将表mseCheatStat4HistoryNewUser（桌面反作弊>手机浏览器>android手机浏览器作弊指标监控>新增作弊用户统计）的作弊用户数同步给表plat_fchannel_stat_new（商业业务>手机浏览器>手机浏览器-Android用户数>android手机浏览器-按历史用户去重新增>按原始渠道号用户数统计）；
mysql:plat_fchannel_stat_new.cheat_newer
""")

mse_all_import2SG = BashOperator(
dag = dag,
env = env,
task_id = 'mse_all_import2SG',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/20150923_chengna_import2SG',
bash_command ='sleep 120',
schedule_interval = '0 3 * * *',
doc_md = u"""
将老白皮的结算数据导入到超级白皮的任务
""")

mse_business_value_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_business_value_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170329_business_value_stat',
bash_command ='sleep 120',
schedule_interval = '0 9 * * *',
doc_md = u"""
手机浏览器android以及ios商业价值模型汇总，对应的数据库mse_bueiness_cash_detail，对应的新绿皮地址为：所有项目>商业业务>手机浏览器>手浏-运营数据-用户价值
mysql:mse_bueiness_cash_detail,mse_business_blackuser_stat,mse_fchannel_shangdian_adjust_stat
result:${IMPORT_PATH}/business/blackuserhis,${IMPORT_PATH}/business/cashummary/log
""")

semob_channelApplist_jinchenxi = BashOperator(
dag = dag,
env = env,
task_id = 'semob_channelApplist_jinchenxi',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/anticheating_mobilebrowser/semobChannelApplist',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器渠道applist分布   用于手浏反作弊工作。
""")

Semob_imeiCheck = BashOperator(
dag = dag,
env = env,
task_id = 'Semob_imeiCheck',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/anticheating_mobilebrowser/imeiCheck',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器IMEI格式检查
""")

Semob_sdkInstallStat = BashOperator(
dag = dag,
env = env,
task_id = 'Semob_sdkInstallStat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/anticheating_mobilebrowser/sdkInstallStat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
手机浏览器反作弊日志统计
""")

semob_modelCount_jinchenxi = BashOperator(
dag = dag,
env = env,
task_id = 'semob_modelCount_jinchenxi',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/anticheating_mobilebrowser/semobModelCount',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
水晶-android手机浏览器作弊指标监控-机型数
""")

semob_modelExceptionRate_jinchenxi = BashOperator(
dag = dag,
env = env,
task_id = 'semob_modelExceptionRate_jinchenxi',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/anticheating_mobilebrowser/modelExceptionRate',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
水晶-android手机浏览器作弊指标监控-机型异常数
""")

mse_20161222_mse_channel_alart = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161222_mse_channel_alart',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/datasprite/20161222_mse_channel_alart',
bash_command ='sleep 120',
schedule_interval = '50 9 * * *',
doc_md = u"""
20161222_mse_channel_alart
http://grape.sogou-inc.com/analysisapply/showapplyinfo.do?id=f15ba3986e184d9b9fe6d5fa28e40a45
mysql:mse_channel_alart
""")

mse_20160907_alart_sms = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20160907_alart_sms',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20160907_alart_sms',
bash_command ='sleep 120',
schedule_interval = '50 9 * * *',
doc_md = u"""
message for BD
""")

ios_iais_zhushou_daystat = BashOperator(
dag = dag,
env = env,
task_id = 'ios_iais_zhushou_daystat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/ios_iais_zhushou_daystat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:ios_iais_zhushou_daystat
result:idfa 历史库
""")

mse_20161220_version_pv_uv_config = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161220_version_pv_uv_config',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20161220_version_pv_uv_config',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_version_pvuv_stat1
rely on:SplitLogFiles
""")

mse_specialStat_weeklyStat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_specialStat_weeklyStat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/Mse_SpecialStat_WeeklyStat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
result:androidSeVerAlive.$date, upload to http server, for sales department.
""")

mb_android = BashOperator(
dag = dag,
env = env,
task_id = 'mb_android',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mb_android',
bash_command ='sleep 120',
schedule_interval = '45 1 * * *',
doc_md = u"""
hive table: android
""")

mb_ios = BashOperator(
dag = dag,
env = env,
task_id = 'mb_ios',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mb_ios',
bash_command ='sleep 120',
schedule_interval = '45 1 * * *',
doc_md = u"""
hive table: ios
""")

mse_20170518_except_user_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20170518_except_user_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170518_except_user_stat',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
result:${IMPORT_PATH}/business/exceptuserhis,两类用户并集（NewsAdClick的pv>10 || 取NewsAdShow的日志中小时的add到set()，len(set)>15.即超过15小时的用户）
用异常用户的统计，对应的需求为用户 预警系统
""")

imei_to_sunbo = BashOperator(
dag = dag,
env = env,
task_id = 'imei_to_sunbo',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/imei_to_sunbo',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
result:${IMPORT_PATH}/imei_to_sunbo/newimei/${logDate}, load data(new imei) to sunbo
""")

channelinfos = BashOperator(
dag = dag,
env = env,
task_id = 'channelinfos',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/channelinfos',
bash_command ='sleep 120',
schedule_interval = '10 0 * * *',
doc_md = u"""
mysql:channelinfos,channelinfo_utf8
""")

MovePhp_ValuePingBack_Stat = BashOperator(
dag = dag,
env = env,
task_id = 'MovePhp_ValuePingBack_Stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/zhouliwu/MovePhp/allValuesPingBacks',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
本地php重构之统计数值型PingBack的任务，包含android以及ios。统计指标为uv,pv，比例，统计维度为软件版本，含有all汇总
mysql:android_mse_stat,android_mse_stat1,android_mse_stat2,android_mse_stat3,android_mse_stat4,android_mse_stat6,android_infoReader_stat,mse_stat,mse_stat1,mse_stat2,mse_stat3,mse_stat4,infoReader_stat
rely on:SplitLogFiles
""")

mse_20161019_daufunction = BashOperator(
dag = dag,
env = env,
task_id = 'mse_20161019_daufunction',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/datasprite/20161019_daufunction',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_yunying_dau_stat
rely on:SplitLogFiles
""")

mse_android_branduserinfo = BashOperator(
dag = dag,
env = env,
task_id = 'mse_android_branduserinfo',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_android_branduserinfo',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
hive task
mysql:mse_android_branduserinfo
""")

mse_zixun_server_new = BashOperator(
dag = dag,
env = env,
task_id = 'mse_zixun_server_new',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_zixun_server_new',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
hive task
hive:mse_zixun_server_new
mysql:mse_zixun_server_new,mse_zixun_server_new_bycode,mse_zixun_server_new_byurl
""")

newabtest_mars = BashOperator(
dag = dag,
env = env,
task_id = 'newabtest_mars',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/newabtest_mars',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
hive task
mysql:mse_newabtest_base_fchannel,mse_newabtest_yunyingkuailian_fchannel,mse_newabtest_base,mse_newabtest_delurl,mse_newabtest_yunyingkuailian
""")

pushmsg = BashOperator(
dag = dag,
env = env,
task_id = 'pushmsg',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/pushmsg',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
hive task
mysql:mse_android_push,mse_android_push_hardware,mse_android_push_system,mse_android_pushmsg_channel
""")

topadv = BashOperator(
dag = dag,
env = env,
task_id = 'topadv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/topadv',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
hive task
mysql:mse_android_bannerurl_adv,mse_ios_bannerurl_adv,mse_android_topadv,mse_ios_topadv
""")

zixundetailcomment = BashOperator(
dag = dag,
env = env,
task_id = 'zixundetailcomment',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/zixundetailcomment',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
hive task
mysql:mse_zixun_detail_comment
""")

kaiping = BashOperator(
dag = dag,
env = env,
task_id = 'kaiping',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/kaiping',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
hive task
mysql:mse_kaiping_android_adid,mse_kaiping_android,mse_kaiping_ios,mse_kaiping_ios_adid
""")

'''
#mobilebrowser_04.py
hive_mse_novel_uid_address_search = BashOperator(
dag = dag,
env = env,
task_id = 'hive_mse_novel_uid_address_search',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_mse_novel_uid_address_search',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
hive task
mysql:mse_novel_uid_address_search
""")
'''

'''
#mobilebrowser_04.py
hive_mse_novel_uid_user_statis = BashOperator(
dag = dag,
env = env,
task_id = 'hive_mse_novel_uid_user_statis',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_mse_novel_uid_user_statis',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
hive task
mysql:mse_novel_uid_user_statis
""")
'''

hive_mse_sdk = BashOperator(
dag = dag,
env = env,
task_id = 'hive_mse_sdk',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_mse_sdk',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
hive table:mse_sdk,mse_blackuser,mse_exceptuser
rely on:${IMPORT_PATH}/antifake_log
""")

mse_prewarning = BashOperator(
dag = dag,
env = env,
task_id = 'mse_prewarning',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_prewarning',
bash_command ='sleep 120',
schedule_interval = '50 9 * * *',
doc_md = u"""
mysql:mse_prewarning_qidonguser_merge
email:title(手机浏览器－渠道预警...)
""")

mse_prewarning_newuser = BashOperator(
dag = dag,
env = env,
task_id = 'mse_prewarning_newuser',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_prewarning',
bash_command ='sleep 120',
schedule_interval = '50 9 * * *',
doc_md = u"""
mysql:mse_prewarning_newuser_merge
email:title(手机浏览器－渠道预警...)
""")

mse_prewarning_search_android = BashOperator(
dag = dag,
env = env,
task_id = 'mse_prewarning_search_android',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_prewarning',
bash_command ='sleep 120',
schedule_interval = '50 9 * * *',
doc_md = u"""
mysql:mse_prewarning_search_android
email:title(手机浏览器－渠道预警...))
""")

mse_prewarning_add_fcstatus = BashOperator(
dag = dag,
env = env,
task_id = 'mse_prewarning_add_fcstatus',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_prewarning',
bash_command ='sleep 120',
schedule_interval = '50 9 * * *',
doc_md = u"""
mysql:update mse_prewarning_newuser_merge,mse_prewarning_qidonguser_merge set fc_status
email:title(手机浏览器－渠道预警...))
""")


mse_prewarning_dau = BashOperator(
dag = dag,
env = env,
task_id = 'mse_prewarning_dau',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_prewarning_dau',
bash_command ='sleep 120',
schedule_interval = '50 9 * * *',
doc_md = u"""
mse_prewarning_qidonguser_merge_dau,
email:title(手机浏览器－渠道预警...)
""")

oem_ch_fc_data = BashOperator(
dag = dag,
env = env,
task_id = 'oem_ch_fc_data',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/oem_ch_fc_data',
bash_command ='sleep 120',
schedule_interval = '50 1 * * *',
doc_md = u"""
mysql:oem_fc_data,oem_ch_data
""")

mse_daily_province_dis = BashOperator(
dag = dag,
env = env,
task_id = 'mse_daily_province_dis',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170308_user_province_dis',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_daily_province_dis
""")

'''
#mobilebrowser_04.py
hive_urlredirect_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'hive_urlredirect_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_urlredirect_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_urlredirect_pvuv
""")
'''

'''
#mobilebrowser_04.py
hive_novelstation_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'hive_novelstation_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_novelstation_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_novelstation_pvuv
""")
'''

'''
#mobilebrowser_04.py
hive_pb_count = BashOperator(
dag = dag,
env = env,
task_id = 'hive_pb_count',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_pb_count',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_pb_count
""")
'''

'''
#mobilebrowser_04.py
hive_novelstation_fullurl = BashOperator(
dag = dag,
env = env,
task_id = 'hive_novelstation_fullurl',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_novelstation_fullurl',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_novelstation_fullurl
""")
'''

'''
# mobilebrowser_04.py
hive_novelregister_count = BashOperator(
dag = dag,
env = env,
task_id = 'hive_novelregister_count',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_novelregister_count',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_novelregister_count
""")
'''

'''
#mobilebrowser_04.py
hive_homeweather_count = BashOperator(
dag = dag,
env = env,
task_id = 'hive_homeweather_count',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_homeweather_count',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_homeweather_count
""")
'''

'''
#mobilebrowser_04.py
hive_weather_backcode = BashOperator(
dag = dag,
env = env,
task_id = 'hive_weather_backcode',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_weather_backcode',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_weather_backcode
""")
'''

'''
#mobilebrowser_04.py
hive_verksite_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'hive_verksite_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_verksite_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_verksite_pvuv
""")
'''

'''
#mobilebrowser_04.py
hive_lockScreen_reasons = BashOperator(
dag = dag,
env = env,
task_id = 'hive_lockScreen_reasons',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_lockScreen_reasons',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_lockScreen_reasons
""")
'''

searchDepData = BashOperator(
dag = dag,
env = env,
task_id = 'searchDepData',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/searchDepData',
bash_command ='sleep 120',
schedule_interval = '0 9 * * *',
doc_md = u"""
mysql:searchDepData
data source: rsync -avz 10.142.102.175::tuisong/document/wap_sogoubrowser/new20190504.txt
""")

ipadbase = BashOperator(
dag = dag,
env = env,
task_id = 'ipadbase',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/ipadbase',
bash_command ='sleep 120',
schedule_interval = '50 0 * * *',
doc_md = u"""
ipad log parse.
result:${LOG_CLIENT}/ipad/ipad$logDate,${IMPORT_PATH}/ipad/dau/dau$logDate,${IMPORT_PATH}/ipad/his/his$logDate,${IMPORT_PATH}/ipad/new/new$logDate
""")

ipadkpichannel = BashOperator(
dag = dag,
env = env,
task_id = 'ipadkpichannel',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/ipadkpichannel',
bash_command ='sleep 120',
schedule_interval = '50 0 * * *',
doc_md = u"""
mysql:ipadkpichannel
""")

ipadkpiver = BashOperator(
dag = dag,
env = env,
task_id = 'ipadkpiver',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/ipadkpiver',
bash_command ='sleep 120',
schedule_interval = '50 0 * * *',
doc_md = u"""
mysql:ipadkpiver
""")

'''
#mobilebrowser_04.py
hive_webvideoplay_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'hive_webvideoplay_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_webvideoplay_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_webvideoplay_pvuv
""")
'''

'''
#mobilebrowser_androidid.py
androidIDBase = BashOperator(
dag = dag,
env = env,
task_id = 'androidIDBase',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/androidIDBase',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
result:${IMPORT_PATH}/androidid/dau/$logDate, ${IMPORT_PATH}/androidid/new/$logDate, ${IMPORT_PATH}/androidid/his/$logDate
""")
'''

hisUidIos_Redis = BashOperator(
dag = dag,
env = env,
task_id = 'hisUidIos_Redis',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hisUidIos_Redis',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
result: load ios historyUids to redis. redis info[host=b.redis.sogou, port=2623, passward=mobilebrowser]
""")

hisUidAndroid_Redis = BashOperator(
dag = dag,
env = env,
task_id = 'hisUidAndroid_Redis',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hisUidAndroid_Redis',
bash_command ='sleep 120',
schedule_interval = '0 2 * * *',
doc_md = u"""
result: load android historyUids to redis. redis info[host=j.redis.sogou, port=2860, passward=mobilebrowserAndroid]
""")

'''
#mobilebrowser_04.py
hive_menu_android = BashOperator(
dag = dag,
env = env,
task_id = 'hive_menu_android',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_menu_android',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_menu_android
""")
'''

ios_kc_newer = BashOperator(
dag = dag,
env = env,
task_id = 'ios_kc_newer',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/ios_kc_newer',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
result:${IMPORT_PATH}/ios_kc/dau/dau$logDate, ${IMPORT_PATH}/ios_kc/new_first/new$logDate,
${IMPORT_PATH}/ios_kc/newer/new$logDate, ${IMPORT_PATH}/ios_kc/his/his$logDate
""")

iosPromotionNwewerCount = BashOperator(
dag = dag,
env = env,
task_id = 'iosPromotionNwewerCount',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/iosPromotionNwewerCount',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:iosPromotionNwewerCount
update semob_iosbrush_pings_stat.newer_kc
""")

'''
#mobilebrowser_04.py
hive_firstPage_newfeed = BashOperator(
dag = dag,
env = env,
task_id = 'hive_firstPage_newfeed',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_firstPage_newfeed',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_firstPage_newfeed
""")
'''

'''
#mobilebrowser_04.py
hive_addressBar_hotword = BashOperator(
dag = dag,
env = env,
task_id = 'hive_addressBar_hotword',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_addressBar_hotword',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_addressBar_hotword
""")
'''

'''
#mobilebrowser_04.py
hive_webpage_module = BashOperator(
dag = dag,
env = env,
task_id = 'hive_webpage_module',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_webpage_module',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_webpage_module
""")
'''

'''
#mobilebrowser_04.py
hive_webReader_errorPage = BashOperator(
dag = dag,
env = env,
task_id = 'hive_webReader_errorPage',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_webReader_errorPage',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_webReader_errorPage
""")
'''

shangsong_email = BashOperator(
dag = dag,
env = env,
task_id = 'shangsong_email',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/shangsong_email',
bash_command ='sleep 120',
schedule_interval = '0 6 * * *',
doc_md = u"""
result:send email to shangsong@sogou-inc.com;yuanheng@sogou-inc.com;chenxianxin@sogou-inc.com;
email:title(手机浏览器－按历史用户去重统计)
""")

'''
#mobilebrowser_04.py
hive_errorPage_infos = BashOperator(
dag = dag,
env = env,
task_id = 'hive_errorPage_infos',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_errorPage_infos',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_errorPage_infos
""")
'''

'''
#mobilebrowser_04.py
hive_ios_url_keyword = BashOperator(
dag = dag,
env = env,
task_id = 'hive_ios_url_keyword',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_ios_url_keyword',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_ios_url_keyword
""")
'''

'''
#mobilebrowser_04.py
hive_vr_popup_andSoOn = BashOperator(
dag = dag,
env = env,
task_id = 'hive_vr_popup_andSoOn',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_vr_popup_andSoOn',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_vr_popup_andSoOn
""")
'''

'''
#mobilebrowser_04.py
hive_ChangeSiteClick_statusShow = BashOperator(
dag = dag,
env = env,
task_id = 'hive_ChangeSiteClick_statusShow',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_ChangeSiteClick_statusShow',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_ChangeSiteClick_statusShow
""")
'''

mse_iosversion_pings_stat = BashOperator(
dag = dag,
env = env,
task_id = 'mse_iosversion_pings_stat',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/20170518_renweiling_iosversion_pings_stat',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
ios版本用户质量的统计，对应的绿皮项目为【手浏-ios-分渠道统计>分版本质量统计】，对应的数据表为：semob_iosversion_pings_stat
rely on:SplitLogFiles
""")

iosKC_newerByVer = BashOperator(
dag = dag,
env = env,
task_id = 'iosKC_newerByVer',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/iosKC_newerByVer',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:iosKC_newerByVer
update:semob_iosversion_pings_stat.kc_newer
""")

mse_channeltopversioncount_android = BashOperator(
dag = dag,
env = env,
task_id = 'mse_channeltopversioncount_android',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser/mse_channeltopversioncount_android',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_channeltopversioncount_android
rely on:channelinfos
""")

'''
#mobilebrowser_04.py
hive_channelwarning_android_active = BashOperator(
dag = dag,
env = env,
task_id = 'hive_channelwarning_android_active',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_channelwarning_android_active',
bash_command ='sleep 120',
schedule_interval = '0 6 * * *',
doc_md = u"""
mysql:hive_channelwarning_android_active
rely on:mb_android
""")
'''

'''
#mobilebrowser_04.py
hive_channelwarning_android_newuser = BashOperator(
dag = dag,
env = env,
task_id = 'hive_channelwarning_android_newuser',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_channelwarning_android_newuser',
bash_command ='sleep 120',
schedule_interval = '0 6 * * *',
doc_md = u"""
mysql:hive_channelwarning_android_newuser
rely on:mb_android
""")
'''

'''
#mobilebrowser_04.py
hive_DesktopShortcutIcon_android = BashOperator(
dag = dag,
env = env,
task_id = 'hive_DesktopShortcutIcon_android',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_DesktopShortcutIcon_android',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_DesktopShortcutIcon_android
""")
'''

'''
#mobilebrowser_04.py
hive_mse_reading_false_url_pvuv_new = BashOperator(
dag = dag,
env = env,
task_id = 'hive_mse_reading_false_url_pvuv_new',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_mse_reading_false_url_pvuv_new',
bash_command ='sleep 120',
schedule_interval = '0 9 * * *',
doc_md = u"""
mysql:mse_reading_false_url_pvuv_new 
rely on:mb_android
""") 
'''

'''
#mobilebrowser_04.py
hive_WebpageReader_ErrorInfo_android = BashOperator(
dag = dag,
env = env,
task_id = 'hive_WebpageReader_ErrorInfo_android',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_WebpageReader_ErrorInfo_android',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_WebpageReader_ErrorInfo_android
""")
'''

mse_anecdote = BashOperator(
dag = dag,
env = env,
task_id = 'mse_anecdote',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_anecdote',
bash_command ='sleep 120',
schedule_interval = '0 1 * * *',
doc_md = u"""
hive:mse_anecdote
""")

'''
# mobilebrowser_04.py
hive_newAdTitles_android = BashOperator(
dag = dag,
env = env,
task_id = 'hive_newAdTitles_android',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_newAdTitles_android',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_newAdTitles_android
""")
'''

hive_newAdTitles_ios = BashOperator(
dag = dag,
env = env,
task_id = 'hive_newAdTitles_ios',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_newAdTitles_ios',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:hive_newAdTitles_ios
""")

channelstay_ios_count = BashOperator(
dag = dag,
env = env,
task_id = 'channelstay_ios_count',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/channelstay_ios_count',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:channelstay_ios_count
""")

mse_informationflow_browse_monitor = BashOperator(
dag = dag,
env = env,
task_id = 'mse_informationflow_browse_monitor',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_informationflow_browse_monitor',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
mysql:mse_informationflow_browse_monitor
""")

mse_informationflow_novel_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'mse_informationflow_novel_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_informationflow_novel_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 6 * * *',
doc_md = u"""
mysql:mse_informationflow_novel_pvuv
""")

mse_noveluidversion_count_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'mse_noveluidversion_count_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_noveluidversion_count_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 6 * * *',
doc_md = u"""
mysql:mse_noveluidversion_count_pvuv
""")

mse_informationflow_zixun_uid = BashOperator(
dag = dag,
env = env,
task_id = 'mse_informationflow_zixun_uid',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_informationflow_zixun_uid',
bash_command ='sleep 120',
schedule_interval = '0 6 * * *',
doc_md = u"""
mysql:mse_informationflow_zixun_uid
""")

hive_newer_imei_androidID= BashOperator(
dag = dag,
env = env,
task_id = 'hive_newer_imei_androidID',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_newer_imei_androidID',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
imei and android, uid of dau
result:/user/mobilebrowser/outputdata/dau_imei_androidID/
""")

'''
#mobilebrowser_04.py
hive_mse_zixunSDK_influence_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'hive_mse_zixunSDK_influence_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_mse_zixunSDK_influence_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 8 * * *',
doc_md = u"""
mysql:hive_mse_zixunSDK_influence_pvuv
""")
'''

hive_imei_mseAndIme= BashOperator(
dag = dag,
env = env,
task_id = 'hive_imei_mseAndIme',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_imei_mseAndIme',
bash_command ='sleep 120',
schedule_interval = '0 10 * * *',
doc_md = u"""
task hive_newer_imei_androidID提供dau用户的imei和androidid,uid给输入法柳彤，然后柳彤对比输入法近一个月数据，将重合的标记为1.输出到路径viewfs://marsX/user/imeda/outputdata/BrowerAndInput
此任务使用上述路径得到每个渠道对应匹配的用户数
hive table:hive_imei_mseAndIme
mysql:update android_channelUid_stat_new.mseAndIme_new,android_channelUid_stat_new.mseAndIme_dau
""")

'''
#mobilebrowser_04.py
hive_mse_android_push_jiguangtouchuan = BashOperator(
dag = dag,
env = env,
task_id = 'hive_mse_android_push_jiguangtouchuan',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_mse_android_push_jiguangtouchuan',
bash_command ='sleep 120',
schedule_interval = '40 9 * * *',
doc_md = u"""
mysql:hive_mse_android_push_jiguangtouchuan
""")
'''

mse_prewarning_ios = BashOperator(
dag = dag,
env = env,
task_id = 'mse_prewarning_ios',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_prewarning_ios',
bash_command ='sleep 120',
schedule_interval = '0 8 * * *',
doc_md = u"""
mysql:mse_prewarning_ios_qidonguser_merge
""")

mse_ios_channels_uuid = BashOperator(
dag = dag,
env = env,
task_id = 'mse_ios_channels_uuid',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_ios_channels_uuid',
bash_command ='sleep 120',
schedule_interval = '30 8 * * *',
doc_md = u"""
hive:ios_channels_uuid;
export:/user/mobilebrowser/outputdata/mb_iosname/
rely on:dau_newer,mse_ioslanmao_pings_stat,ios_kc_newer
""")

mse_voice_zixun_android = BashOperator(
dag = dag,
env = env,
task_id = 'mse_voice_zixun_android',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_voice_zixun_android',
bash_command ='sleep 120',
schedule_interval = '50 8 * * *',
doc_md = u"""
mysql:mse_voice_zixun_android
""")

hive_mse_voice_zixun_recordvoice_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'hive_mse_voice_zixun_recordvoice_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_mse_voice_zixun_recordvoice_pvuv',
bash_command ='sleep 120',
schedule_interval = '10 9 * * *',
doc_md = u"""
mysql:hive_mse_voice_zixun_recordvoice_pvuv
""")

mse_voice_zixun_voicebank_active = BashOperator(
dag = dag,
env = env,
task_id = 'mse_voice_zixun_voicebank_active',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_voice_zixun_voicebank_active',
bash_command ='sleep 120',
schedule_interval = '10 9 * * *',
doc_md = u"""
mysql:mse_voice_zixun_voicebank_active
""")

mse_newuserappnames_android = BashOperator(
dag = dag,
env = env,
task_id = 'mse_newuserappnames_android',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_newuserappnames_android',
bash_command ='sleep 120',
schedule_interval = '1 7 * * *',
doc_md = u"""
result:/user/mobilebrowser/outputdata/mse_newuserappnames_android/
""")


salesData_rsync_1 = BashOperator(
dag = dag,
env = env,
task_id = 'salesData_rsync_1',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/salesData_rsync',
bash_command ='sleep 120',
schedule_interval = '0 8 * * *',
doc_md = u"""
result:${IMPORT_PATH}/sales_data
""")

salesData_rsync_2 = BashOperator(
dag = dag,
env = env,
task_id = 'salesData_rsync_2',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/salesData_rsync',
bash_command ='sleep 120',
schedule_interval = '0 8 * * *',
doc_md = u"""
result:${IMPORT_PATH}/search_data
""")

accounting_api = BashOperator(
dag = dag,
env = env,
task_id = 'accounting_api',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/accounting_api',
bash_command ='sleep 120',
schedule_interval = '0 9 * * *',
doc_md = u"""
rsync 10.142.95.188::odin/search/nginx/html/se;10.143.23.202::odin/search/nginx/html/se;
result:http://da.sogou-inc.com/se/jiesuan_data1_20190227.txt
""")

mse_user_province_gps_ip = BashOperator(
dag = dag,
env = env,
task_id = 'mse_user_province_gps_ip',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_user_province_gps_ip',
bash_command ='sleep 120',
schedule_interval = '0 9 * * *',
doc_md = u"""
mysql:mse_user_province_gps_ip
""")

hive_mse_android_firstinstall = BashOperator(
dag = dag,
env = env,
task_id = 'hive_mse_android_firstinstall',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_mse_android_firstinstall',
bash_command ='sleep 120',
schedule_interval = '30 9 * * *',
doc_md = u"""
update:mse_channel_class_stats_subchannel.pingbackkeyfirstinstalluv,mse_channel_bygroup.pingbackkeyfirstinstalluv,mse_channel_class_stats_op_all.pingbackkeyfirstinstalluv,mse_channel_class_stats_op_class.pingbackkeyfirstinstalluv
""")

hive_mse_android_daufunction = BashOperator(
dag = dag,
env = env,
task_id = 'hive_mse_android_daufunction',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_mse_android_daufunction',
bash_command ='sleep 120',
schedule_interval = '30 9 * * *',
doc_md = u"""
update:mse_channel_class_stats_subchannel.dauf_newuser_1day_survive,mse_channel_class_stats_subchannel.dauf_newuser_7day_survive,mse_channel_bygroup.dauf_newuser_1day_survive,mse_channel_bygroup.dauf_newuser_7day_survive
""")

mse_prewarning_email = BashOperator(
dag = dag,
env = env,
task_id = 'mse_prewarning_email',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_prewarning_email',
bash_command ='sleep 120',
schedule_interval = '0 11 * * *',
doc_md = u"""
result:send email to litingting216856@sogou-inc.com;gaosai@sogou-inc.com;zhaopei@sogou-inc.com;hongyancai@sogou-inc.com;
title:手机浏览器－渠道预警-新
""")

hive_mse_android_clicklogowakeupcount_pvuv = BashOperator(
dag = dag,
env = env,
task_id = 'hive_mse_android_clicklogowakeupcount_pvuv',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_mse_android_clicklogowakeupcount_pvuv',
bash_command ='sleep 120',
schedule_interval = '0 8 * * *',
doc_md = u"""
mysql:hive_mse_android_clicklogowakeupcount_pvuv,update oem_fc_data,oem_ch_data,plat_fchannel_stat_new,plat_channel_stat_new set PingBackClickLogoWakeUpCount_uv
""")

dau_firstinstall = BashOperator(
dag = dag,
env = env,
task_id = 'dau_firstinstall',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/dau_firstinstall',
bash_command ='sleep 120',
schedule_interval = '0 7 * * *',
doc_md = u"""
result:/user/mobilebrowser/import/firstinstall/$logDate
""")

mse_120_firstinstall_retains = BashOperator(
dag = dag,
env = env,
task_id = 'mse_120_firstinstall_retains',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_120_firstinstall_retains',
bash_command ='sleep 120',
schedule_interval = '30 7 * * *',
doc_md = u"""
mysql:mse_fchannel_reserved_firstinstall_survive_120
""")

hive_mse_ios_syshardwarever_bychannel = BashOperator(
dag = dag,
env = env,
task_id = 'hive_mse_ios_syshardwarever_bychannel',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/hive_mse_ios_syshardwarever_bychannel',
bash_command ='sleep 120',
schedule_interval = '20 7 * * *',
doc_md = u"""
mysql:hive_mse_ios_syshardwarever_bychannel
""")

adjustAllNewRetain_redpacket = BashOperator(
dag = dag,
env = env,
task_id = 'adjustAllNewRetain_redpacket',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/adjustAllNewRetain_redpacket',
bash_command ='sleep 120',
schedule_interval = '30 7 * * *',
doc_md = u"""
mysql:plat_version_stat_new_redpacket,plat_fchannel_stat_new_redpacket
""")

mse_allchannels_logoretains_redpacket = BashOperator(
dag = dag,
env = env,
task_id = 'mse_allchannels_logoretains_redpacket',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/mse_allchannels_logoretains_redpacket',
bash_command ='sleep 120',
schedule_interval = '0 8 * * *',
doc_md = u"""
update plat_fchannel_stat_new_redpacket.logo_retain
""")

'''
#9 lines
 = BashOperator(
dag = dag,
env = env,
task_id = '',
svn_url = '',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
""")
'''

#######################<<timer.schedule>>#######################
fourClock = BashOperator(
dag = dag,
env = env,
task_id = 'fourClock',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/timer_schedule',
bash_command ='sleep 120',
schedule_interval = '0 4 * * *',
doc_md = u"""
timer schedule, 4 o'clock
""")

adjustAllNewRetain_combine              >> fourClock
mse_minibasicdata                       >> fourClock
mse_SdkPushDesktopClick                 >> fourClock
mse_sdk_allObjectPingBack2              >> fourClock
ipadkpichannel                          >> fourClock
ipadkpiver                              >> fourClock

fourClock                               >> hive_imei_mseAndIme
fourClock                               >> hive_newer_imei_androidID
#fourClock                               >> hive_WebpageReader_ErrorInfo_android
#fourClock                               >> hive_DesktopShortcutIcon_android
fourClock                               >> iosKC_newerByVer
fourClock                               >> mse_channeltopversioncount_android
fourClock                               >> mse_iosversion_pings_stat
#fourClock                               >> hive_ChangeSiteClick_statusShow
#fourClock                               >> hive_vr_popup_andSoOn
#fourClock                               >> hive_ios_url_keyword
#fourClock                               >> hive_errorPage_infos
#fourClock                               >> hive_webReader_errorPage
#fourClock                               >> hive_addressBar_hotword
#fourClock                               >> hive_webpage_module
#fourClock                               >> hive_firstPage_newfeed
fourClock                               >> iosPromotionNwewerCount
#fourClock                               >> androidIDBase
#fourClock                               >> hive_menu_android
#fourClock                               >> hive_webvideoplay_pvuv
#fourClock                               >> hive_lockScreen_reasons
#fourClock                               >> hive_verksite_pvuv
#fourClock                               >> hive_homeweather_count
#fourClock                               >> hive_novelregister_count
fourClock                               >> mse_20160905_mse_1_30aliveretains
#fourClock                               >> hive_weather_backcode
fourClock                               >> mse_20160905_mse_1_30installretains
fourClock                               >> Semob_sdkInstallStat
fourClock                               >> mse_SdkMiniStat_allValuesPingBacks
fourClock                               >> mse_20161220_version_pv_uv_config
fourClock                               >> Semob_imeiCheck
fourClock                               >> mse_20161019_daufunction
fourClock                               >> mse_all_appsdownload_stat
fourClock                               >> semob_channelApplist_jinchenxi
fourClock                               >> mse_novel_msesogoucom_total
fourClock                               >> mse_channel_information_uvpv
fourClock                               >> ios_iais_zhushou_daystat
fourClock                               >> mse_20161021_mse_1_30installretains
fourClock                               >> MovePhp_ValuePingBack_Stat
fourClock                               >> mse_novel_sdk_verratio
fourClock                               >> mse_daily_province_dis
fourClock                               >> mse_20161104_search_word_stats
fourClock                               >> mse_20160125_taoge_1_30newerretains
fourClock                               >> mse_20161205_mse_1_60installretain
fourClock                               >> mse_20160930_cooperation_guanwang_stats
fourClock                               >> mse_android_wakeupqunicklunch_stat
fourClock                               >> mse_ads_showclick_stat
fourClock                               >> mse_20161216_mse_reading_stats
fourClock                               >> mse_20161229_status_stats
fourClock                               >> mse_20161220_version_abtest_top500
fourClock                               >> mse_20161224_version_abtest_pvuv
fourClock                               >> mse_pushflow_dis_stat
fourClock                               >> mse_alll_CatesAll_stat
fourClock                               >> mse_20170116_mse_1_30aliveretains_chidongfang_huice
fourClock                               >> mse_20170110_mse_abtest_1_7alive_stats
fourClock                               >> mse_20161226_uuid_distribution
#fourClock                               >> hive_novelstation_fullurl
#fourClock                               >> hive_pb_count
#fourClock                               >> hive_novelstation_pvuv
#fourClock                               >> hive_urlredirect_pvuv
#fourClock                               >> hive_mse_novel_uid_user_statis
#fourClock                               >> hive_mse_novel_uid_address_search
fourClock                               >> kaiping
fourClock                               >> zixundetailcomment
fourClock                               >> topadv
fourClock                               >> pushmsg
fourClock                               >> newabtest_mars
fourClock                               >> mse_android_branduserinfo
fourClock                               >> mse_specialStat_weeklyStat
fourClock                               >> semob_modelCount_jinchenxi
fourClock                               >> semob_modelExceptionRate_jinchenxi
fourClock                               >> semob_channelUvIp_jinchenxi
fourClock                               >> mse_zixun_server_stat
fourClock                               >> mse_hijackdownloadappincome_android
fourClock                               >> mse_mininavi_stat
fourClock                               >> semob_all_tbl_novel_shelf_stat
fourClock                               >> mse_novel_retain_rate
fourClock                               >> novel_center_user_stat
fourClock                               >> mse_lockscreen_retain_android
fourClock                               >> mse_groupbysufuid_pvuv
fourClock                               >> mse_Movephp_StatPingBacks
fourClock                               >> mse_iqiyicoopration_anroid
#fourClock                               >> mse_navitable_countandretain_stat
fourClock                               >> mse_newsconsume_pvuv
fourClock                               >> mse_newsfeed_region
fourClock                               >> mse_newsfeed_ver
fourClock                               >> mse_20161212_SDK_jiesuan
fourClock                               >> mse_android_resolutionnwer_stat
fourClock                               >> mse_Movephp_allValuesPingBacksByChannel
fourClock                               >> mse_newspush_uid_abtest
fourClock                               >> mse_newusers_deviceManagement
fourClock                               >> mse_new_version_fchannel_information
fourClock                               >> mse_novelgidcount_pvuv
fourClock                               >> mse_novel_all_movenovel_catePagesStat
fourClock                               >> mse_novel_all_movenovel_valuesPagesStat
fourClock                               >> mse_novel_all_movenovel_visitUserStat
fourClock                               >> mse_sdkmini_calls_stat
fourClock                               >> mse_sdk_20151215_mengwei_sdkfloat_stat
fourClock                               >> mse_timeconsuming_pvuv
fourClock                               >> mse_informationflow_browse_monitor
fourClock                               >> mse_translator_pvuv
fourClock                               >> mse_zixunnews_c_fc
fourClock                               >> mse_fchannel_retains_alert
fourClock                               >> PingbackCompetingAppName_stat
fourClock                               >> sdk_uninstall_stat
fourClock                               >> semob_android_status_rate
fourClock                               >> channelstay_ios_count

sixClock = BashOperator(
dag = dag,
env = env,
task_id = 'sixClock',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/mobile_browser_new/timer_schedule',
bash_command ='sleep 120',
schedule_interval = '0 6 * * *',
doc_md = u"""
timer schedule, 6 o'clock
""")
fourClock                       >> sixClock

sixClock                        >> searchDepData
sixClock                        >> mse_20160907_alart_sms
sixClock                        >> mse_20161222_mse_channel_alart
sixClock                        >> mse_search_pids_cash_rpm
sixClock                        >> mse_new_cost_zixun
sixClock                        >> mse_detailads_show_stat
#sixClock                        >> semob_android_chenjinabtest_fchannelneweretains
sixClock                        >> mse_channel_class_stats
sixClock                        >> mse_bds_channels_data
sixClock                        >> mse_SdkMiniStat_allUserStat
sixClock                        >> shangsong_email
#sixClock                        >> hive_channelwarning_android_active
#sixClock                        >> hive_channelwarning_android_newuser
#sixClock                        >> hive_mse_reading_false_url_pvuv_new
#sixClock                        >> hive_newAdTitles_android
sixClock                        >> hive_newAdTitles_ios
sixClock                        >> mse_informationflow_novel_pvuv
sixClock                        >> mse_noveluidversion_count_pvuv
sixClock                        >> mse_informationflow_zixun_uid
#sixClock                        >> hive_mse_zixunSDK_influence_pvuv
#sixClock                        >> hive_mse_android_push_jiguangtouchuan
sixClock                        >> mse_prewarning_ios
sixClock                        >> mse_ios_channels_uuid
sixClock                        >> mse_voice_zixun_android
sixClock                        >> hive_mse_voice_zixun_recordvoice_pvuv
sixClock                        >> mse_voice_zixun_voicebank_active
sixClock                        >> mse_newuserappnames_android
sixClock                        >> salesData_rsync_1
sixClock                        >> salesData_rsync_2
sixClock                        >> mse_user_province_gps_ip
sixClock                        >> hive_mse_android_clicklogowakeupcount_pvuv
sixClock                        >> mse_120_install_retains
sixClock                        >> dau_firstinstall
sixClock                        >> mse_120_firstinstall_retains
sixClock                        >> hive_mse_ios_syshardwarever_bychannel
sixClock                        >> adjustAllNewRetain_redpacket
sixClock                        >> mse_allchannels_logoretains_redpacket
#######################<<timer.schedule>>#######################


#######################<<tasks dependency relationship>>#######################

DecodeLogFlow_day                                   >> SplitLogFiles_android
DecodeLogFlow_day                                   >> SplitLogFiles_ios
DecodeLogFlow_day                                   >> SplitLogFiles_sdk
DecodeLogFlow_day                                   >> SplitLogFiles_others
SplitLogFiles_android                               >> SplitLogFiles
SplitLogFiles_ios                                   >> SplitLogFiles
SplitLogFiles_sdk                                   >> SplitLogFiles
SplitLogFiles_others                                >> SplitLogFiles
SplitLogFiles                                       >> dau_newer
SplitLogFiles                                       >> MovePhp_UserStat
SplitLogFiles                                       >> mse_20161227_version_pv_uv_config
SplitLogFiles                                       >> mse_20190128_sysversion_pv_uv_config
SplitLogFiles                                       >> mse_SdkPushDesktopClick
#SplitLogFiles                                       >> mse_SdkPushDesktopClick1
SplitLogFiles                                       >> mse_Movephp_StatPingBacks
#SplitLogFiles                                       >> mse_navitable_countandretain_stat
SplitLogFiles                                       >> mse_20161224_version_abtest_pvuv
SplitLogFiles                                       >> mse_new_version_fchannel_information
SplitLogFiles                                       >> mse_pushflow_dis_stat
SplitLogFiles                                       >> mse_translator_pvuv
SplitLogFiles                                       >> mse_newsconsume_pvuv
SplitLogFiles                                       >> mse_iqiyicoopration_anroid
SplitLogFiles                                       >> mse_20161220_version_abtest_top500
dau_newer                                           >> adjustAllNewRetain_alive
dau_newer                                           >> adjustAllNewRetain_survive
dau_newer                                           >> mse_novel_sdk_verratio
MovePhp_UserStat                                    >> MovePhp_NewerRetainRate
adjustAllNewRetain_alive                            >> adjustAllNewRetain_combine
adjustAllNewRetain_survive                          >> adjustAllNewRetain_combine
mse_20161227_version_pv_uv_config                   >> adjustAllNewRetain_combine
mse_20190128_sysversion_pv_uv_config                >> adjustAllNewRetain_combine
MovePhp_NewerRetainRate                             >> adjustAllNewRetain_combine
SplitLogFiles                                       >> mse_sdk_allObjectPingBack2
mse_android_GetAndroidSdkMiniLog                    >> mse_sdk_allObjectPingBack2
minibrowser                                         >> mse_minibasicdata
MovePhp_UserStat                                    >> mse_Movephp_allValuesPingBacksByChannel
adjustAllNewRetain_combine                          >> mse_20161104_search_word_stats
adjustAllNewRetain_combine                          >> mse_20161212_SDK_jiesuan
dau_newer                                           >> mse_20161226_uuid_distribution
dau_newer                                           >> mse_20161229_status_stats
dau_newer                                           >> mse_20170110_mse_abtest_1_7alive_stats
dau_newer                                           >> mse_newusers_deviceManagement
dau_newer                                           >> mse_20161021_mse_1_30installretains
dau_newer                                           >> mse_120_install_retains
mse_20161021_mse_1_30installretains                 >> mse_fchannel_retains_alert
MovePhp_NewerRetainRate                             >> mse_android_resolutionnwer_stat
dau_newer                                           >> mse_lockscreen_retain_android
dau_newer                                           >> mse_groupbysufuid_pvuv
dau_newer                                           >> mse_timeconsuming_pvuv
dau_newer                                           >> mse_informationflow_browse_monitor
dau_newer                                           >> mse_noveluidversion_count_pvuv
dau_newer                                           >> mse_newsfeed_ver
dau_newer                                           >> mse_newsfeed_region
dau_newer                                           >> mse_newspush_uid_abtest
dau_newer                                           >> mse_zixunnews_c_fc
mse_GetguanwangLog                                  >> mse_20161216_mse_reading_stats
SplitLogFiles                                       >> mse_20161216_mse_reading_stats
mse_GetguanwangLog                                  >> mse_novel_msesogoucom_total
mse_GetguanwangLog                                  >> mse_novel_all_movenovel_visitUserStat
mse_GetguanwangLog                                  >> mse_novel_all_movenovel_valuesPagesStat
mse_GetguanwangLog                                  >> mse_novel_all_movenovel_catePagesStat
mse_GetguanwangLog                                  >> mse_20160930_cooperation_guanwang_stats
mse_GetguanwangLog                                  >> mse_novelgidcount_pvuv
SplitLogFiles                                       >> mse_sdk_20151215_mengwei_sdkfloat_stat
mse_GetguanwangLog                                  >> mse_sdk_20151215_mengwei_sdkfloat_stat
SplitLogFiles                                       >> mse_sdkmini_calls_stat
mse_GetguanwangLog                                  >> mse_sdkmini_calls_stat
SplitLogFiles                                       >> mse_SdkMiniStat_allValuesPingBacks
mse_GetguanwangLog                                  >> mse_SdkMiniStat_allValuesPingBacks
mse_GetguanwangLog                                  >> sdk_uninstall_stat
adjustAllNewRetain_combine                          >> semob_android_status_rate
adjustAllNewRetain_combine                          >> PingbackCompetingAppName_stat
mse_GetguanwangLog                                  >> novel_center_user_stat
mse_GetguanwangLog                                  >> mse_novel_retain_rate
adjustAllNewRetain_combine                          >> semob_all_tbl_novel_shelf_stat
adjustAllNewRetain_combine                          >> mse_android_wakeupqunicklunch_stat
adjustAllNewRetain_combine                          >> mse_alll_CatesAll_stat
mse_GetguanwangLog                                  >> mse_mininavi_stat
SplitLogFiles                                       >> mse_SdkMiniStat_allUserStat
mse_android_GetAndroidSdkMiniLog                    >> mse_SdkMiniStat_allUserStat
mse_SdkMiniStat_allValuesPingBacks                  >> mse_SdkMiniStat_allUserStat
mse_GetguanwangLog                                  >> mse_all_appsdownload_stat
dau_newer                                           >> mse_20170116_mse_1_30aliveretains_chidongfang_huice
adjustAllNewRetain_combine                          >> mse_ads_showclick_stat
MovePhp_UserStat                                    >> mse_hijackdownloadappincome_android
dau_newer                                           >> mse_20160905_mse_1_30installretains
dau_newer                                           >> mse_20160905_mse_1_30aliveretains
adjustAllNewRetain_combine                          >> mse_bds_channels_data
mse_20160905_mse_1_30aliveretains                   >> mse_bds_channels_data
mse_business_value_stat                             >> mse_bds_channels_data
adjustAllNewRetain_combine                          >> mse_channel_class_stats
mse_20160905_mse_1_30aliveretains                   >> mse_channel_class_stats
mse_20160905_mse_1_30installretains                 >> mse_channel_class_stats
adjustAllNewRetain_combine                          >> mse_channel_full_infos
#dau_newer                                           >> semob_android_chenjinabtest_fchannelneweretains
adjustAllNewRetain_combine                          >> mse_channel_information_uvpv
mse_channel_information_uvpv                        >> mse_detailads_show_stat
adjustAllNewRetain_combine                          >> mse_android_allchannels_newerlogoretains_stat
dau_newer                                           >> mse_20161205_mse_1_60installretain
mse_GetguanwangLog                                  >> mse_zixun_server_stat
MovePhp_UserStat                                    >> mse_20160125_taoge_1_30newerretains
SplitLogFiles                                       >> semob_channelUvIp_jinchenxi
mse_all_GetIosBrushlLog                             >> mse_iosbrush_lanmao_retain
dau_newer                                           >> mse_iosbrush_lanmao_retain
mse_all_GetIosBrushlLog                             >> mse_ioslanmao_pings_stat
mse_iosbrush_lanmao_retain                          >> mse_ioslanmao_pings_stat
adjustAllNewRetain_combine                          >> mse_android_effectiveuser_channel
dau_newer                                           >> mse_new_cost_zixun
salesData_rsync_1                                   >> mse_new_cost_zixun
SplitLogFiles                                       >> mse_search_pids_cash_rpm
salesData_rsync_2                                   >> mse_search_pids_cash_rpm
MovePhp_NewerRetainRate                             >> semob_dailyAntiCheats_jinchenxi
adjustAllNewRetain_combine                          >> semob_dailyAntiCheats_jinchenxi
Semob_antiFakeSDKLog                                >> semob_dailyAntiCheats_jinchenxi
mse_android_effectiveuser_channel                   >> semob_dailyAntiCheats_jinchenxi
semob_dailyAntiCheats_jinchenxi                     >> semob_SDKDailyAntiCheats_chemsjim
semob_SDKDailyAntiCheats_chemsjim                   >> mobilebrowser_kpi_data_load_again
semob_dailyAntiCheats_jinchenxi                     >> plat_fchannel_stat
adjustAllNewRetain_combine                          >> plat_fchannel_stat
mse_android_effectiveuser_channel                   >> mse_all_import2SG
semob_SDKDailyAntiCheats_chemsjim                   >> mse_all_import2SG
adjustAllNewRetain_combine                          >> mse_business_value_stat
mse_ioslanmao_pings_stat                            >> mse_business_value_stat
semob_dailyAntiCheats_jinchenxi                     >> mse_business_value_stat
mse_android_effectiveuser_channel                   >> mse_business_value_stat
mse_search_pids_cash_rpm                            >> mse_business_value_stat
mse_new_cost_zixun                                  >> mse_business_value_stat
SplitLogFiles                                       >> semob_channelApplist_jinchenxi
SplitLogFiles                                       >> Semob_imeiCheck
Semob_antiFakeSDKLog                                >> Semob_sdkInstallStat
Semob_sdkInstallStat                                >> semob_modelCount_jinchenxi
Semob_sdkInstallStat                                >> semob_modelExceptionRate_jinchenxi
semob_modelExceptionRate_jinchenxi                  >> mse_20161222_mse_channel_alart
adjustAllNewRetain_combine                          >> mse_20161222_mse_channel_alart
Semob_imeiCheck                                     >> mse_20161222_mse_channel_alart
semob_channelApplist_jinchenxi                      >> mse_20161222_mse_channel_alart
plat_fchannel_stat                                  >> mse_20160907_alart_sms
mse_sdk_allObjectPingBack2                          >> mse_20160907_alart_sms
mse_SdkPushDesktopClick                             >> mse_20160907_alart_sms
mse_minibasicdata                                   >> mse_20160907_alart_sms
mse_ioslanmao_pings_stat                            >> mse_20160907_alart_sms
mse_channel_class_stats                             >> mse_20160907_alart_sms
mse_all_GetIosBrushlLog                             >> ios_iais_zhushou_daystat
dau_newer                                           >> ios_iais_zhushou_daystat
SplitLogFiles                                       >> mse_20161220_version_pv_uv_config
mse_20161220_version_pv_uv_config                   >> mse_specialStat_weeklyStat
adjustAllNewRetain_combine                          >> mse_specialStat_weeklyStat
dau_newer                                           >> mb_android
dau_newer                                           >> mb_ios
SplitLogFiles                                       >> mse_20170518_except_user_stat
SplitLogFiles                                       >> imei_to_sunbo
adjustAllNewRetain_combine                          >> MovePhp_ValuePingBack_Stat
SplitLogFiles                                       >> mse_20161019_daufunction
mb_android                                          >> mse_20161019_daufunction
mb_android                                          >> mse_android_branduserinfo
mse_GetguanwangLog                                  >> mse_zixun_server_new
mb_android                                          >> newabtest_mars
mb_android                                          >> pushmsg
mb_android                                          >> topadv
mb_ios                                              >> topadv
mb_android                                          >> zixundetailcomment
mb_android                                          >> kaiping
mb_ios                                              >> kaiping
#mb_android                                          >> hive_mse_novel_uid_address_search
#mb_android                                          >> hive_mse_novel_uid_user_statis
Semob_antiFakeSDKLog                                >> hive_mse_sdk
mse_business_value_stat                             >> hive_mse_sdk
mse_20170518_except_user_stat                       >> hive_mse_sdk
mb_android                                          >> mse_prewarning
hive_mse_sdk                                        >> mse_prewarning
mb_android                                          >> mse_prewarning_dau
hive_mse_sdk                                        >> mse_prewarning_dau
mb_android                                          >> mse_prewarning_newuser
hive_mse_sdk                                        >> mse_prewarning_newuser
mse_prewarning                                      >> mse_prewarning_search_android
mse_prewarning_newuser                              >> mse_prewarning_search_android
mse_prewarning_search_android                       >> mse_prewarning_email
hive_imei_mseAndIme                                 >> mse_prewarning_email
mse_prewarning                                      >> mse_prewarning_add_fcstatus
mse_prewarning_newuser                              >> mse_prewarning_add_fcstatus
adjustAllNewRetain_combine                          >> oem_ch_fc_data
mse_android_allchannels_newerlogoretains_stat       >> oem_ch_fc_data
plat_fchannel_stat                                  >> oem_ch_fc_data
mse_channel_class_stats                             >> oem_ch_fc_data
dau_newer                                           >> mse_daily_province_dis
#mb_android                                          >> hive_urlredirect_pvuv
#mb_android                                          >> hive_novelstation_pvuv
#mb_android                                          >> hive_pb_count
#mb_android                                          >> hive_novelstation_fullurl
#mb_android                                          >> hive_novelregister_count
#mb_android                                          >> hive_homeweather_count
#mb_android                                          >> hive_weather_backcode
#mb_android                                          >> hive_verksite_pvuv
#mb_android                                          >> hive_lockScreen_reasons
ipadbase                                            >> ipadkpichannel
ipadbase                                            >> ipadkpiver
#mb_android                                          >> hive_webvideoplay_pvuv
#SplitLogFiles                                       >> androidIDBase
ios_kc_newer                                        >> hisUidIos_Redis
#mb_android                                          >> hive_menu_android
dau_newer                                           >> ios_kc_newer
dau_newer                                           >> mse_iosversion_pings_stat
mse_iosversion_pings_stat                           >> iosKC_newerByVer
ios_kc_newer                                        >> iosKC_newerByVer
ios_kc_newer                                        >> iosPromotionNwewerCount
mse_ioslanmao_pings_stat                            >> iosPromotionNwewerCount
#mb_android                                          >> hive_firstPage_newfeed
#mb_android                                          >> hive_addressBar_hotword
#mb_android                                          >> hive_webpage_module
#mb_android                                          >> hive_webReader_errorPage
adjustAllNewRetain_combine                          >> shangsong_email
mse_channel_class_stats                             >> shangsong_email
mse_android_allchannels_newerlogoretains_stat       >> shangsong_email
plat_fchannel_stat                                  >> shangsong_email
#mb_android                                          >> hive_errorPage_infos
#mb_android                                          >> hive_ios_url_keyword
#mb_android                                          >> hive_vr_popup_andSoOn
#mb_android                                          >> hive_ChangeSiteClick_statusShow
channelinfos                                        >> mse_channeltopversioncount_android
dau_newer                                           >> mse_channeltopversioncount_android
#mb_android                                          >> hive_channelwarning_android_active
#mb_android                                          >> hive_channelwarning_android_newuser
#mb_android                                          >> hive_DesktopShortcutIcon_android
#mb_android                                          >> hive_mse_reading_false_url_pvuv_new
#mb_android                                          >> hive_WebpageReader_ErrorInfo_android
#mb_android                                          >> hive_newAdTitles_android
mse_anecdote					    >> hive_newAdTitles_ios
dau_newer                                           >> mse_anecdote
iosPromotionNwewerCount                             >> channelstay_ios_count
SplitLogFiles                                       >> mse_informationflow_novel_pvuv
dau_newer                                           >> mse_informationflow_zixun_uid
mb_android                                          >> hive_newer_imei_androidID
#mb_android                                          >> hive_mse_zixunSDK_influence_pvuv
mb_android                                          >> hive_imei_mseAndIme
hive_newer_imei_androidID                           >> hive_imei_mseAndIme
MovePhp_UserStat                           	    >> hive_imei_mseAndIme
#mb_android                                          >> hive_mse_android_push_jiguangtouchuan
iosPromotionNwewerCount                             >> mse_prewarning_ios
mb_ios                                              >> mse_prewarning_ios
mse_anecdote                                        >> mse_prewarning_ios 
dau_newer                                           >> mse_ios_channels_uuid
mse_ioslanmao_pings_stat                            >> mse_ios_channels_uuid
ios_kc_newer                                        >> mse_ios_channels_uuid
SplitLogFiles                                       >> mse_voice_zixun_android
mb_android                                          >> hive_mse_voice_zixun_recordvoice_pvuv
mse_voice_zixun_android                             >> hive_mse_voice_zixun_recordvoice_pvuv
SplitLogFiles                                       >> mse_voice_zixun_voicebank_active
dau_newer                                           >> mse_newuserappnames_android
mse_business_value_stat                             >> accounting_api
dau_newer                                           >> mse_user_province_gps_ip
mb_android                                          >> hive_mse_android_firstinstall
mse_channel_class_stats                             >> hive_mse_android_firstinstall
mb_android                                          >> hive_mse_android_daufunction
mse_channel_class_stats                             >> hive_mse_android_daufunction
dau_newer                                           >> hisUidAndroid_Redis
mb_android                                          >> hive_mse_android_clicklogowakeupcount_pvuv
oem_ch_fc_data                                      >> hive_mse_android_clicklogowakeupcount_pvuv
dau_newer                                           >> dau_firstinstall
dau_firstinstall                                    >> mse_120_firstinstall_retains
mse_ios_channels_uuid                               >> hive_mse_ios_syshardwarever_bychannel
iosPromotionNwewerCount                             >> hive_mse_ios_syshardwarever_bychannel
mse_channel_class_stats                             >> adjustAllNewRetain_redpacket
adjustAllNewRetain_redpacket                        >> mse_allchannels_logoretains_redpacket
adjustAllNewRetain_combine                          >> mse_alltype_dauretain
#######################<<tasks dependency relationship>>#######################
