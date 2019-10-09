#!/usr/bin/env python
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
    'execution_timeout': timedelta(hours=12),
    'depends_on_past': True,
    'start_date': utils.dates.days_ago(10)
}

dag = DAG(
    'feed',
    default_args = default_args,
    description = u'信息流业务统计',
    schedule_interval = "@daily"
)
dag.doc_md = __doc__

env = {'HIVE_CONF_DIR':'daohang','HADOOP_CONF_DIR':'daohang'}



#infoflow_coolsite = BashOperator(
#dag = dag,
#env = env,
#task_id = 'infoflow_coolsite',
#svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/infoFlow/',
#bash_command ='sh infoflow_coolsitefeed.sh {{ds_nodash}}',
#schedule_interval = '15 3 * * *',
#doc_md = u"""
#该任务依赖  dh_sehome_pb2
#其生成脚本:
#/search/datawash/dh/sehome/pb/monqua/day_start.sh（同上）
#/search/datawash/dh/sehome/pb/monqua/daohang_sehome2.sh
#http://grape.sogou-inc.com/task/tab3/detail/31b2d7a4dba5458fbf1380e962dee8ae 
#
#http://taurus.sogou-inc.com/tableGroup/17839
#mysql:infoflow_coolsitefeed_pvuv,infoflow_coolsitefeed_func,infoflow_coolsitefeed_url,infoflow_coolsitefeed_domain
#
#""")

distinct_yaokan_back = BashOperator(
dag = dag,
env = env,
task_id = 'distinct_yaokan_back',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/distinct_yaokan_back',
bash_command ='sleep 10',
schedule_interval = '0 5 * * *',
doc_md = u"""
对策略端日志根据seqo(sessionid的序列号，每条日志的编号，去重避免发重复了)去重
result:/user/daohang/wulian/abtest/distinct_yaokan_back_statics,
""")

dh_layber_byday = BashOperator(
dag = dag,
env = env,
task_id = 'dh_layber_byday',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/infoFlow/dh_layer_byday',
bash_command ='sleep 10',
schedule_interval = '20 7 * * *',
doc_md = u"""
导航abtest 
mysql:dh_abtest_layer_day,dh_abtest_layer_distributary_day,dh_abtest_layer_recallsource
"""
)

dh_monitor_byday = BashOperator(
dag = dag,
env = env,
task_id = 'dh_monitor_byday',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/infoFlow/dh_layer_byday',
bash_command ='sleep 10',
schedule_interval = '40 7 * * *',
doc_md = u"""
底部导航日常监测
mysql:dh_monitor_day
"""
)

dh_coolsite_monitor_byday = BashOperator(
dag = dag,
env = env,
task_id = 'dh_coolsite_monitor_byday',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/infoFlow/dh_layer_byday',
bash_command ='sleep 10',
schedule_interval = '40 7 * * *',
doc_md = u"""
酷站导航日常监测
mysql:dh_coolsite_day
"""
)


dh_coolsite_byday = BashOperator(
dag = dag,
env = env,
task_id = 'dh_coolsite_byday',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/infoFlow/dh_layer_byday',
bash_command ='sleep 10',
schedule_interval = '45 7 * * *',
doc_md = u"""
酷站信息流 abtest
mysql:dh_abtest_coolsite_day,dh_abtest_coolsite_recallsource,dh_abtest_coolsite_distributary
""")

coolsite_liucun = BashOperator(
dag = dag,
env = env,
task_id = 'coolsite_liucun',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/infoFlow/liucun',
bash_command ='sleep 10',
schedule_interval = '00 8 * * *',
doc_md = u"""
酷站信息流 全部用户留存情况
dh_coolsite_liucun_day
""")

coolsite_newuser_liucun = BashOperator(
dag = dag,
env = env,
task_id = 'coolsite_newuser_liucun',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/infoFlow/liucun',
bash_command ='sleep 10',
schedule_interval = '15 8 * * *',
doc_md = u"""
酷站信息流 新增用户留存情况
mysql:dh_coolsite_liucun_newuser_day
results_path:/user/daohang/newsfeed/important/coolsitehisuer, /user/daohang/newsfeed/important/coolsitenewer
""")


#page_h5_pvuv = BashOperator(
#dag = dag,
#env = env,
#task_id = 'page_h5_pvuv',
#svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/infoFlow/h5',
#bash_command ='sleep 10',
#schedule_interval = '00 9 * * *',
#doc_md = u"""
#H5信息流页面推广数据
#http://grape.sogou-inc.com/task/tab2/detail/49c5612fdccf431a9a39fe2b721db45b
#""")


dh_feed_channel = BashOperator(
dag = dag,
env = env,
task_id = 'dh_feed_channel',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/infoFlow/channel',
bash_command ='sleep 10',
schedule_interval = '10 9 * * *',
doc_md = u"""
底部导航信息流-频道统计表
mysql:dh_monitor_channel
http://grape.sogou-inc.com/task/tab2/detail/49c5612fdccf431a9a39fe2b721db45b
""")

dh_infoflow_liucun_day = BashOperator(
dag = dag,
env = env,
task_id = 'dh_infoflow_liucun_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/micro_protal_retain',
bash_command ='sleep 10',
schedule_interval = '40 7 * * *',
doc_md = u"""
mysql:dh_infoflow_liucun_day
""")

dh_infoflow_liucun_newuser_day= BashOperator(
dag = dag,
env = env,
task_id = 'dh_infoflow_liucun_newuser_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/dh_infoflow_liucun_newuser_day',
bash_command ='sleep 10',
schedule_interval = '50 7 * * *',
doc_md = u"""
mysql:dh_infoflow_liucun_newuser_day
results_path:/user/daohang/newsfeed/important/bottomhisuer,/user/daohang/newsfeed/important/bottomnewer
""")

microportal_abtest_layer_day= BashOperator(
dag = dag,
env = env,
task_id = 'microportal_abtest_layer_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/microPortal_abtest_day',
bash_command ='sleep 10',
schedule_interval = '30 7 * * *',
doc_md = u"""
mysql:microportal_abtest_layer_day
result:/user/daohang/wulian/microPortal/abtest/distinct_yaokan_back_statics/MicroPortalDistinct*
""")

microportal_abtest_layer_distributary_day= BashOperator(
dag = dag,
env = env,
task_id = 'microportal_abtest_layer_distributary_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/microPortal_abtest_day',
bash_command ='sleep 10',
schedule_interval = '30 7 * * *',
doc_md = u"""
mysql:microportal_abtest_layer_distributary_day
result:/user/daohang/wulian/microPortal/abtest/distinct_yaokan_back_statics/MicroPortalDistinct*
""")

microportal_abtest_layer_recallsource= BashOperator(
dag = dag,
env = env,
task_id = 'microportal_abtest_layer_recallsource',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/microPortal_abtest_day',
bash_command ='sleep 10',
schedule_interval = '30 7 * * *',
doc_md = u"""
mysql:microportal_abtest_layer_recallsource
result:/user/daohang/wulian/microPortal/abtest/distinct_yaokan_back_statics/MicroPortalDistinct*
""")

microportal_monitor_day= BashOperator(
dag = dag,
env = env,
task_id = 'microportal_monitor_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/microPortal_abtest_day',
bash_command ='sleep 10',
schedule_interval = '40 7 * * *',
doc_md = u"""
mysql:microportal_monitor_day
""")

haoqq_daily_monitor= BashOperator(
dag = dag,
env = env,
task_id = 'haoqq_daily_monitor',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/haoqq_daily_monitor',
bash_command ='sleep 10',
schedule_interval = '15 7 * * *',
doc_md = u"""
mysql:haoqq_daily_monitor
""")

haoqq_dividedLayer_all= BashOperator(
dag = dag,
env = env,
task_id = 'haoqq_dividedLayer_all',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/haoqq_dividedLayer_all',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:haoqq_dividedLayer_all
""")

haoqq_dividedTest_day= BashOperator(
dag = dag,
env = env,
task_id = 'haoqq_dividedTest_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/haoqq_dividedTest_day',
bash_command ='sleep 10',
schedule_interval = '20 7 * * *',
doc_md = u"""
mysql:haoqq_dividedTest_day
""")

haoqq_recallAna_day= BashOperator(
dag = dag,
env = env,
task_id = 'haoqq_recallAna_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/haoqq_recallAnalyze_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:haoqq_recallAna_day
""")

haoqq_daily_retain= BashOperator(
dag = dag,
env = env,
task_id = 'haoqq_daily_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/haoqq_daily_retain',
bash_command ='sleep 10',
schedule_interval = '0 6 * * *',
doc_md = u"""
mysql:haoqq_daily_retain
""")

haoqq_newer_his= BashOperator(
dag = dag,
env = env,
task_id = 'haoqq_newer_his',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/haoqq_newer_his',
bash_command ='sleep 10',
schedule_interval = '0 5 * * *',
doc_md = u"""
result:${IMPORT_PATH}/haoqqhisuser/his${logDate},${IMPORT_PATH}/haoqqnewer/new${logDate}
""")

haoqq_newer_retain= BashOperator(
dag = dag,
env = env,
task_id = 'haoqq_newer_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/haoqq_newer_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:haoqq_newer_retain
""")

dhqq_daily_monitor= BashOperator(
dag = dag,
env = env,
task_id = 'dhqq_daily_monitor',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/dhqq_daily_monitor',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:dhqq_daily_monitor
""")

dhqq_recallAnalyze_day= BashOperator(
dag = dag,
env = env,
task_id = 'dhqq_recallAnalyze_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/dhqq_recallAnalyze_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:dhqq_recallAna_day
""")

dhqq_dividedLayer_all= BashOperator(
dag = dag,
env = env,
task_id = 'dhqq_dividedLayer_all',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/dhqq_dividedLayer_all',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:dhqq_dividedLayer_all
""")

dhqq_dividedTest_day= BashOperator(
dag = dag,
env = env,
task_id = 'dhqq_dividedTest_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/dhqq_dividedTest_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:dhqq_dividedTest_day
""")

dhqq_daily_retain= BashOperator(
dag = dag,
env = env,
task_id = 'dhqq_daily_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/dhqq_daily_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:dhqq_daily_retain
""")

dhqq_newer_his= BashOperator(
dag = dag,
env = env,
task_id = 'dhqq_newer_his',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/dhqq_newer_his',
bash_command ='sleep 10',
schedule_interval = '0 5 * * *',
doc_md = u"""
result:/user/daohang/newsfeed/important/dhqqhisuser, /user/daohang/newsfeed/important/dhqqnewer
""")

dhqq_newer_retain= BashOperator(
dag = dag,
env = env,
task_id = 'dhqq_newer_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/dhqq_newer_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:dhqq_newer_retain
""")

hive_ybStatics= BashOperator(
dag = dag,
env = env,
task_id = 'hive_ybStatics',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/hive_ybStatics',
bash_command ='sleep 10',
schedule_interval = '0 3 * * *',
doc_md = u"""
hive: ybStatics
result:$IMPORT_PATH/hive/external_Data/ybStatics/
""")

hive_ybback_ids= BashOperator(
dag = dag,
env = env,
task_id = 'hive_ybback_ids',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/hive_ybback_ids',
bash_command ='sleep 10',
schedule_interval = '0 6 * * *',
doc_md = u"""
mysql:hive_ybback_ids
""")

bmwaigou_monitor_day= BashOperator(
dag = dag,
env = env,
task_id = 'bmwaigou_monitor_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/bmwaigou_monitor_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:bmwaigou_monitor_day
""")

bmwaigou_recallAna_day= BashOperator(
dag = dag,
env = env,
task_id = 'bmwaigou_recallAna_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/bmwaigou_recallAna_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:bmwaigou_recallAna_day
""")

bmwaigou_dividedLayer_all= BashOperator(
dag = dag,
env = env,
task_id = 'bmwaigou_dividedLayer_all',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/bmwaigou_dividedLayer_all',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:bmwaigou_dividedLayer_all
""")

bmwaigou_dividedTest_day= BashOperator(
dag = dag,
env = env,
task_id = 'bmwaigou_dividedTest_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/bmwaigou_dividedTest_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:bmwaigou_dividedTest_day
""")

bmwaigou_daily_retain= BashOperator(
dag = dag,
env = env,
task_id = 'bmwaigou_daily_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/bmwaigou_daily_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:bmwaigou_daily_retain
""")

bmwaigou_newer_his= BashOperator(
dag = dag,
env = env,
task_id = 'bmwaigou_newer_his',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/bmwaigou_newer_his',
bash_command ='sleep 10',
schedule_interval = '0 5 * * *',
doc_md = u"""
mysql:bmwaigou_newer_his
""")

bmwaigou_newerRetain= BashOperator(
dag = dag,
env = env,
task_id = 'bmwaigou_newerRetain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/bmwaigou_newer_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:bmwaigou_newer_retain
""")

mp_channel_count= BashOperator(
dag = dag,
env = env,
task_id = 'mp_channel_count',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/mp_channel_count',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:mp_channel_count
""")

#mp_monitorTest_Day= BashOperator(
#dag = dag,
#env = env,
#task_id = 'mp_monitorTest_Day',
#svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/mp_monitorTest_Day',
#bash_command ='sleep 10',
#schedule_interval = '0 7 * * *',
#doc_md = u"""
#mysql:mp_monitorTest_Day
#""")

bm_abtestChannel_day= BashOperator(
dag = dag,
env = env,
task_id = 'bm_abtestChannel_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/bm_abtestChannel_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:bm_abtestChannel_day
""")

mp_abtestChannel_day= BashOperator(
dag = dag,
env = env,
task_id = 'mp_abtestChannel_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/mp_abtestChannel_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:mp_abtestChannel_day
""")

bmwg_abtestChannel_day= BashOperator(
dag = dag,
env = env,
task_id = 'bmwg_abtestChannel_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/bmwg_abtestChannel_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:bmwg_abtestChannel_day
""")

dhqq_abtestChannel_day= BashOperator(
dag = dag,
env = env,
task_id = 'dhqq_abtestChannel_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/dhqq_abtestChannel_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:dhqq_abtestChannel_day
""")

haoqq_abtestChannel_day= BashOperator(
dag = dag,
env = env,
task_id = 'haoqq_abtestChannel_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/haoqq_abtestChannel_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:haoqq_abtestChannel_day
""")

nsp_monitor_day= BashOperator(
dag = dag,
env = env,
task_id = 'nsp_monitor_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/nsp_monitor_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:nsp_monitor_day
""")

nsp_recallAna_day= BashOperator(
dag = dag,
env = env,
task_id = 'nsp_recallAna_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/nsp_recallAna_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:nsp_recallAna_day
""")

nsp_dividedLayer_all= BashOperator(
dag = dag,
env = env,
task_id = 'nsp_dividedLayer_all',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/nsp_dividedLayer_all',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:nsp_dividedLayer_all
""")

nsp_dividedTest_day= BashOperator(
dag = dag,
env = env,
task_id = 'nsp_dividedTest_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/nsp_dividedTest_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:nsp_dividedTest_day
""")

nsp_daily_retain= BashOperator(
dag = dag,
env = env,
task_id = 'nsp_daily_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/nsp_daily_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:nsp_daily_retain
""")

nsp_newer_his= BashOperator(
dag = dag,
env = env,
task_id = 'nsp_newer_his',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/nsp_newer_his',
bash_command ='sleep 10',
schedule_interval = '0 5 * * *',
doc_md = u"""
result:${IMPORT_PATH}/nsphisuser/his${logDate}, ${IMPORT_PATH}/nspnewer/new${logDate}
""")

nsp_newer_retain= BashOperator(
dag = dag,
env = env,
task_id = 'nsp_newer_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/nsp_newer_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:nsp_newer_retain
""")

allNewsFeeds_click= BashOperator(
dag = dag,
env = env,
task_id = 'allNewsFeeds_click',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/allNewsFeeds_click',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:allNewsFeeds_click
""")

mp_daily_retain= BashOperator(
dag = dag,
env = env,
task_id = 'mp_daily_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/mp_daily_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:mp_daily_retain
""")

mp_testbynum_day= BashOperator(
dag = dag,
env = env,
task_id = 'mp_testbynum_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/mp_testbynum_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:mp_testbynum_day
""")

mp_newer_his= BashOperator(
dag = dag,
env = env,
task_id = 'mp_newer_his',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/mp_newer_his',
bash_command ='sleep 10',
schedule_interval = '0 5 * * *',
doc_md = u"""
mysql:mp_newer_his
""")

mp_newer_retain= BashOperator(
dag = dag,
env = env,
task_id = 'mp_newer_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/mp_newer_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:mp_newer_retain
""")

pcPopup_monitor_day= BashOperator(
dag = dag,
env = env,
task_id = 'pcPopup_monitor_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcPopup_monitor_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:pcPopup_monitor_day
""")

pcPopup_recallAna_day= BashOperator(
dag = dag,
env = env,
task_id = 'pcPopup_recallAna_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcPopup_recallAna_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:pcPopup_recallAna_day
""")

pcPopup_dividedLayer_all= BashOperator(
dag = dag,
env = env,
task_id = 'pcPopup_dividedLayer_all',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcPopup_dividedLayer_all',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:pcPopup_dividedLayer_all
""")

pcPopup_dividedTest_day= BashOperator(
dag = dag,
env = env,
task_id = 'pcPopup_dividedTest_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcPopup_dividedTest_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:pcPopup_dividedTest_day
""")

pcPopup_newer_his= BashOperator(
dag = dag,
env = env,
task_id = 'pcPopup_newer_his',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcPopup_newer_his',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
result:/user/daohang/newsfeed/important/pcpopuphisuser,/user/daohang/newsfeed/important/pcpopupnewer
""")

pcPopup_newer_retain= BashOperator(
dag = dag,
env = env,
task_id = 'pcPopup_newer_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcPopup_newer_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:pcPopup_newer_retain
""")

pcPopup_daily_retain= BashOperator(
dag = dag,
env = env,
task_id = 'pcPopup_daily_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcPopup_daily_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:pcPopup_daily_retain
""")

cs_monitorEndnum_day= BashOperator(
dag = dag,
env = env,
task_id = 'cs_monitorEndnum_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/cs_monitorEndnum_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:cs_monitorEndnum_day
""")

pcSidebar_module= BashOperator(
dag = dag,
env = env,
task_id = 'pcSidebar_module',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/common_modules_base',
bash_command ='sleep 10',
schedule_interval = '0 2 * * *',
doc_md = u"""
do nothing, use to clear special dag-tasks,pcSidebar
""")

pcSidebar_monitor_day= BashOperator(
dag = dag,
env = env,
task_id = 'pcSidebar_monitor_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcSidebar_monitor_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:pcSidebar_monitor_day
""")

pcSidebar_recallAna_day= BashOperator(
dag = dag,
env = env,
task_id = 'pcSidebar_recallAna_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcSidebar_recallAna_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:pcSidebar_recallAna_day
""")

pcSedebar_dividedTest_day= BashOperator(
dag = dag,
env = env,
task_id = 'pcSedebar_dividedTest_day',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcSedebar_dividedTest_day',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:pcSedebar_dividedTest_day
""")

pcSedebar_dividedLayer_all= BashOperator(
dag = dag,
env = env,
task_id = 'pcSedebar_dividedLayer_all',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcSedebar_dividedLayer_all',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:pcSedebar_dividedLayer_all
""")

pcSidebar_daily_retain= BashOperator(
dag = dag,
env = env,
task_id = 'pcSidebar_daily_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcSidebar_daily_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:pcSidebar_daily_retain
""")

pcSidebar_newer_his= BashOperator(
dag = dag,
env = env,
task_id = 'pcSidebar_newer_his',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcSidebar_newer_his',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
result:newsfeed/important/pcsidebarhisuser,newsfeed/important/pcsidebarnewer
""")

pcSidebar_newer_retain= BashOperator(
dag = dag,
env = env,
task_id = 'pcSidebar_newer_retain',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/pcSidebar_newer_retain',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:pcSidebar_newer_retain
""")

bmwaigou_module= BashOperator(
dag = dag,
env = env,
task_id = 'bmwaigou_module',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/common_modules_base',
bash_command ='sleep 10',
schedule_interval = '0 2 * * *',
doc_md = u"""
do nothing, use to clear special dag-tasks,bmwaigou
""")

coolsite_module= BashOperator(
dag = dag,
env = env,
task_id = 'coolsite_module',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/common_modules_base',
bash_command ='sleep 10',
schedule_interval = '0 2 * * *',
doc_md = u"""
do nothing, use to clear special dag-tasks,coolsite
""")

bottom_module= BashOperator(
dag = dag,
env = env,
task_id = 'bottom_module',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/common_modules_base',
bash_command ='sleep 10',
schedule_interval = '0 2 * * *',
doc_md = u"""
do nothing, use to clear special dag-tasks,bottom
""")

mp_module= BashOperator(
dag = dag,
env = env,
task_id = 'mp_module',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/common_modules_base',
bash_command ='sleep 10',
schedule_interval = '0 2 * * *',
doc_md = u"""
do nothing, use to clear special dag-tasks,mp_module
""")

nsp_module= BashOperator(
dag = dag,
env = env,
task_id = 'nsp_module',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/common_modules_base',
bash_command ='sleep 10',
schedule_interval = '0 2 * * *',
doc_md = u"""
do nothing, use to clear special dag-tasks,nsp_module
""")

haoqq_module= BashOperator(
dag = dag,
env = env,
task_id = 'haoqq_module',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/common_modules_base',
bash_command ='sleep 10',
schedule_interval = '0 2 * * *',
doc_md = u"""
do nothing, use to clear special dag-tasks,haoqq_module
""")

dhqq_module= BashOperator(
dag = dag,
env = env,
task_id = 'dhqq_module',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/common_modules_base',
bash_command ='sleep 10',
schedule_interval = '0 2 * * *',
doc_md = u"""
do nothing, use to clear special dag-tasks,dhqq_module
""")

pcPopup_module= BashOperator(
dag = dag,
env = env,
task_id = 'pcPopup_module',
svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/common_modules_base',
bash_command ='sleep 10',
schedule_interval = '0 2 * * *',
doc_md = u"""
do nothing, use to clear special dag-tasks,pcPopup_module
""")




'''
#11 lines
= BashOperator(
dag = dag,
env = env,
task_id = '',
svn_url = '',
bash_command ='sleep 10',
schedule_interval = '0 7 * * *',
doc_md = u"""
mysql:
results_path:
""")
'''

#############################>Dependency description<#############################
hive_ybStatics					>> hive_ybback_ids

#<pcPopup_module>
distinct_yaokan_back				>> pcPopup_recallAna_day
distinct_yaokan_back				>> pcPopup_dividedLayer_all
distinct_yaokan_back				>> pcPopup_dividedTest_day
pcPopup_newer_his				>> pcPopup_newer_retain
#module dependency
pcPopup_module					>> pcPopup_monitor_day
pcPopup_module					>> pcPopup_recallAna_day
pcPopup_module					>> pcPopup_dividedLayer_all
pcPopup_module					>> pcPopup_dividedTest_day
pcPopup_module					>> pcPopup_daily_retain
pcPopup_module					>> pcPopup_newer_his
pcPopup_module					>> pcPopup_newer_retain

#<pcSidebar_module>
distinct_yaokan_back				>> pcSidebar_recallAna_day
distinct_yaokan_back				>> pcSedebar_dividedTest_day
distinct_yaokan_back				>> pcSedebar_dividedLayer_all
pcSidebar_newer_his				>> pcSidebar_newer_retain
#module dependency
pcSidebar_module				>> pcSidebar_monitor_day
pcSidebar_module				>> pcSidebar_recallAna_day
pcSidebar_module				>> pcSedebar_dividedTest_day
pcSidebar_module				>> pcSedebar_dividedLayer_all
pcSidebar_module				>> pcSidebar_daily_retain
pcSidebar_module				>> pcSidebar_newer_his

#<bmwaigou_module>
distinct_yaokan_back				>> bmwaigou_recallAna_day
distinct_yaokan_back				>> bmwaigou_dividedLayer_all
distinct_yaokan_back				>> bmwaigou_dividedTest_day
distinct_yaokan_back				>> bmwg_abtestChannel_day
bmwaigou_newer_his				>> bmwaigou_newerRetain
#module dependency
bmwaigou_module					>> bmwaigou_monitor_day
bmwaigou_module					>> bmwaigou_recallAna_day
bmwaigou_module					>> bmwaigou_dividedTest_day
bmwaigou_module					>> bmwaigou_dividedLayer_all
bmwaigou_module					>> bmwaigou_newer_his
bmwaigou_module					>> bmwaigou_daily_retain
bmwaigou_module					>> bmwg_abtestChannel_day

#<coolsite_module>
distinct_yaokan_back				>> dh_coolsite_byday
#module dependency
coolsite_module					>> dh_coolsite_monitor_byday
coolsite_module					>> cs_monitorEndnum_day
coolsite_module					>> coolsite_liucun
coolsite_module					>> coolsite_newuser_liucun
coolsite_module					>> dh_coolsite_byday

#<bottom_module>
distinct_yaokan_back				>> dh_layber_byday
distinct_yaokan_back				>> bm_abtestChannel_day
#module dependency
bottom_module					>> dh_monitor_byday
bottom_module					>> dh_feed_channel
bottom_module					>> dh_infoflow_liucun_day
bottom_module					>> dh_infoflow_liucun_newuser_day
bottom_module                                   >> dh_layber_byday
bottom_module                                   >> bm_abtestChannel_day

#<mp_module>
distinct_yaokan_back				>> microportal_abtest_layer_day
distinct_yaokan_back				>> microportal_abtest_layer_distributary_day
distinct_yaokan_back				>> microportal_abtest_layer_recallsource
distinct_yaokan_back				>> mp_abtestChannel_day
mp_newer_his					>> mp_newer_retain
#module dependency
mp_module					>> microportal_monitor_day
mp_module					>> mp_daily_retain
mp_module					>> mp_newer_his
mp_module					>> mp_newer_retain
mp_module					>> mp_testbynum_day
mp_module					>> mp_abtestChannel_day
mp_module					>> mp_channel_count
mp_module					>> microportal_abtest_layer_day
mp_module					>> microportal_abtest_layer_distributary_day
mp_module					>> microportal_abtest_layer_recallsource

#<nsp_module>
distinct_yaokan_back				>> nsp_recallAna_day
distinct_yaokan_back				>> nsp_dividedLayer_all
distinct_yaokan_back				>> nsp_dividedTest_day
nsp_newer_his					>> nsp_newer_retain
#module dependency
nsp_module					>> nsp_monitor_day
nsp_module					>> nsp_daily_retain
nsp_module					>> nsp_newer_retain
nsp_module					>> nsp_newer_his
nsp_module					>> nsp_dividedTest_day
nsp_module					>> nsp_dividedLayer_all
nsp_module					>> nsp_recallAna_day

#<haoqq_module>
distinct_yaokan_back				>> haoqq_dividedTest_day
distinct_yaokan_back				>> haoqq_abtestChannel_day
distinct_yaokan_back				>> haoqq_dividedLayer_all
distinct_yaokan_back				>> haoqq_recallAna_day
haoqq_newer_his					>> haoqq_newer_retain
#module dependency
haoqq_module					>> haoqq_daily_monitor
haoqq_module					>> haoqq_daily_retain
haoqq_module					>> haoqq_newer_retain
haoqq_module					>> haoqq_newer_his
haoqq_module					>> haoqq_recallAna_day
haoqq_module					>> haoqq_dividedLayer_all
haoqq_module					>> haoqq_dividedTest_day
haoqq_module					>> haoqq_abtestChannel_day

#<dhqq_module>
distinct_yaokan_back				>> dhqq_recallAnalyze_day
distinct_yaokan_back				>> dhqq_abtestChannel_day
distinct_yaokan_back				>> dhqq_dividedLayer_all
distinct_yaokan_back				>> dhqq_dividedTest_day
dhqq_newer_his					>> dhqq_newer_retain
#module dependency
dhqq_module					>> dhqq_daily_monitor
dhqq_module					>> dhqq_daily_retain
dhqq_module					>> dhqq_newer_his
dhqq_module					>> dhqq_newer_retain
dhqq_module					>> dhqq_recallAnalyze_day
dhqq_module					>> dhqq_dividedLayer_all
dhqq_module					>> dhqq_dividedTest_day
dhqq_module					>> dhqq_abtestChannel_day
#############################>Dependency description<#############################


