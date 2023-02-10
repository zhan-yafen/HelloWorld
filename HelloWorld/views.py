#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:
# @Desc: { 模块描述 }
# @Date: 2023/02/10 15:40


from django.shortcuts import render


def runoob(request):
    views_name = "菜鸟教程"
    return render(request, "runoob.html", {"name": views_name})
