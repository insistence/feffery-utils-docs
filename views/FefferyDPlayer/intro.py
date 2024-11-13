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
                {'title': translator.t('播放器')},
                {'title': translator.t('FefferyDPlayer 视频播放')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('FefferyDPlayer 视频播放'),
            level=2,
        ),
        fac.AntdParagraph(translator.t('提供丰富的视频播放功能。')),
    ]
