#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imp
from airflow import DAG
import six

mod_name='temp01'
filepath='temp01.py'
m = imp.load_source(mod_name, filepath)
#print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n%s<<<<<<<<" % m)
#print (type(m))
#print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n%s<<<<<<<<" % m.__dict__)

mvs = list(m.__dict__.values())
#print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n%s<<<<<<<<" % mvs)

for dag in mvs:
    if isinstance(dag, DAG):
        print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n%s<<<<<<<<" % dag)
        print (dag.dag_id)
        tasks = six.itervalues(dag.task_dict)
        print (tasks)
        for task in tasks:
            print (task)
            #print (type(task))
            #print (task.__dict__)
            print (task.upstream_list)
