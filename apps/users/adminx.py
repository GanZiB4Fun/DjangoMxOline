# _*_ coding: utf-8 _*_
# @Time    : 2017/7/24 18:17
# @Author  : GanZiB
# @Site    : 
# @File    : adminx.py

import xadmin

from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
	list_display = ['code', 'email', 'send_type', 'send_time']
	search_fields = ['code', 'email', 'send_type']
	list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
