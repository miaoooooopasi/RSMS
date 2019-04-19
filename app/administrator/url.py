# coding:utf-8
from app.administrator import administrator
from flask_restful import Resource, Api
from app.administrator.view import administratorView

api = Api(administrator)

# 注册路由
api.add_resource(administratorView, '/administrator')
# api.add_resource(Server, '/servers/<_id>')
