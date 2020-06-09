# _*_coding:utf-8_*_
# 作者       ：${刘林豪} 
# 创建时间   ：下午 22:24
# 文件       ：llh.py
# IDE        ：PyCharm
from django import template
# from django.utils.safestring import mark_safe

register=template.Library()

@register.simple_tag
def hello(a):
    return 123