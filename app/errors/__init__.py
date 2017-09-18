# coding: utf8

from flask import Blueprint

from app.models import Permission

errors = Blueprint('errors', __name__)

from . import views


#  使用上下文处理器，让模板可能检查权限
@errors.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
