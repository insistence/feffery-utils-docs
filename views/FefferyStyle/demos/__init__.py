from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='FefferyStyle')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': '通过参数`rawStyle`令指定的**css**代码片段生效。',
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
