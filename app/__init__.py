# -*- coding:UTF-8 -*-

from flask_login import LoginManager
from flask_pagedown import PageDown
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
pagedown = PageDown()

# 登录状态记录
login_manager = LoginManager()
# 设为strong会记录客户端IP和浏览器的用户代理信息，发现异常就登出
login_manager.session_protection = 'strong'
# 设置登录页面的端点 - auth.这个是定义了路由的蓝本的名字
login_manager.login_view = 'auth.login'


# 实现工厂函数，创建app实例
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    login_manager.init_app(app)
    pagedown.init_app(app)

    # 使用蓝本定义路由 - 蓝本描述了路由和错误处理
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 注册用户蓝本
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    return app
