# -*- coding: UTF-8 -*-

from flask import Blueprint

from app.models import Permission

main = Blueprint('main', __name__)

from . import controller


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
