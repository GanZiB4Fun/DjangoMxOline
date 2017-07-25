# _*_ coding: utf-8 _*_
# @Time    : 2017/7/24 19:31
# @Author  : GanZiB
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm

# class CourseAdmin(object):
# 	name = models.CharField(max_length=50, verbose_name=u'课程名')
# 	desc = models.CharField(max_length=300, verbose_name=u'课程描述')
# 	detail = models.TextField(verbose_name=u'课程详情')
# 	degree = models.CharField(choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), max_length=2, verbose_name=u'难度')
# 	learn_time = models.IntegerField(default=0, verbose_name=u'学习市场(分钟数)')
# 	students = models.IntegerField(default=0, verbose_name=u'学习人数')
# 	fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
# 	image = models.ImageField(upload_to='course/%Y/%m', verbose_name=u'封面图', max_length=100)
# 	click_num = models.IntegerField(default=0, verbose_name=u'点击数')
# 	add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
#
# 	list_display = ['code', 'email', 'send_type', 'send_time']
# 	search_fields = ['code', 'email', 'send_type']
# 	list_filter = ['code', 'email', 'send_type', 'send_time']
