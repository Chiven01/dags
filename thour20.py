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
    'start_date': utils.dates.days_ago(3)
}

dag = DAG(
    'thour20',
    default_args = default_args,
    description = u'信息流业务统计',
    schedule_interval = "@hourly"
)
dag.doc_md = __doc__

env = {'HIVE_CONF_DIR':'daohang','HADOOP_CONF_DIR':'daohang'}

lens = [40,5,5,2,2]

temps = []
for n in range(lens[0]):
    temp = 'temp_%s' % n
    temp = BashOperator(
    dag = dag,
    env = env,
    task_id = temp,
    svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/temp',
    bash_command ='sleep 120',
    schedule_interval = '1 * * * *',
    doc_md = u"""""")
    temps.append(temp)

taemps = []
for n in range(lens[1]):
    taemp = 'taemp_%s' % n
    taemp = BashOperator(
    dag = dag,
    env = env,
    task_id = taemp,
    svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/taemp',
    bash_command ='sleep 120',
    schedule_interval = '1 * * * *',
    doc_md = u"""""")
    taemps.append(taemp)

tbemps = []
for n in range(lens[2]):
    tbemp = 'tbemp_%s' % n
    tbemp = BashOperator(
    dag = dag,
    env = env,
    task_id = tbemp,
    svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/tbemp',
    bash_command ='sleep 120',
    schedule_interval = '1 * * * *',
    doc_md = u"""""")
    tbemps.append(tbemp)

tcemps = []
for n in range(lens[3]):
    tcemp = 'tcemp_%s' % n
    tcemp = BashOperator(
    dag = dag,
    env = env,
    task_id = tcemp,
    svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/tcemp',
    bash_command ='sleep 120',
    schedule_interval = '1 * * * *',
    doc_md = u"""""")
    tcemps.append(tcemp)

tdemps = []
for n in range(lens[4]):
    tdemp = 'tdemp_%s' % n
    tdemp = BashOperator(
    dag = dag,
    env = env,
    task_id = tdemp,
    svn_url = 'http://svn.sogou-inc.com/svn/sogouime/DataAnalysis/platform_java/imedaapptask/newsfeed/tdemp',
    bash_command ='sleep 120',
    schedule_interval = '1 * * * *',
    doc_md = u"""""")
    tdemps.append(tdemp)

for te in temps:
    for ta in taemps:
        for tb in tbemps:
            for tc in tcemps:
                for td in tdemps:
                    ta >> te
                    tb >> ta
                    tc >> tb
                    td >> tc

#for te in temps:
#    for ta in taemps:
#        ta >> te

