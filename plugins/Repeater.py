# A Simple Reapter

from pluginsinterface.PluginLoader import on_message, Session, on_preprocessor, on_plugloaded
from pluginsinterface.PluginLoader import PlugMsgReturn, plugRegistered, PlugMsgTypeEnum, PluginsManage
from pluginsinterface.PluginLoader import PlugArgFilter


import asyncio
import config
import random
from nonbot import Nonebot
from helper import logger
logger = getlogger(__name__)

"""
复读机插件：通过config中repeat_after字段进行复读条数控制：每(repeat_after)次群员复读后复读一次。

通过config中repeat_cool_time字段进行复读静默时间控制：(repeat_cool_time)秒内不检测复读。

默认：5条/10秒
"""

@plugRegistered('复读机', groupname='repeater')
def _():
    return{
        'plugmanagement': '1.0',
        'version': '1.0',
        'author': 'Cyame',
        'des': '复读机插件，会根据群员发言进行复读。'
    }


@on_plugloaded
def _(plug: PluginsManage):
    if plug:
        pass

@on_preprocessor
async def _(session: Session) -> PlugMsgReturn:
    return PlugMsgReturn.Allow

topic = ''
count = 0

@on_message(msgfilter='', des='复读', at_to_me=False)
async def _(session: Session):
    pass