# -*- coding: UTF-8 -*-

from flask import render_template
from . import errors


# 区别于在hello_orignal.py中写的errorhandler方法，这里用app_errorhandler
# 区别：errorhandler用于截获本文件中的错误
# app_errorhandler用于截获app中的全局错误

@errors.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


@errors.app_errorhandler(403)
def forbidden_error(e):
    return render_template('errors/403.html'), 403
