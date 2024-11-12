import feffery_antd_components as fac
from dash.dependencies import Component

# 国际化
from i18n import translator


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {'title': translator.t('拖拽交互')},
                {'title': translator.t('FefferyDraggable 可拖拽')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyDraggable 可拖拽'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('快捷实现可拖拽功能。')),
    ]
