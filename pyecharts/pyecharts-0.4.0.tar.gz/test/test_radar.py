#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Radar


def test_radar_default_schema():
    schema = [
        ("销售", 6500), ("管理", 16000), ("信息技术", 30000),
        ("客服", 38000), ("研发", 52000), ("市场", 25000)
    ]
    v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
    v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
    radar = Radar("雷达图示例")
    radar.config(schema)
    radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
    radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False,
              legend_selectedmode='single')
    radar.render()


value_bj = [
    [55, 9, 56, 0.46, 18, 6, 1],
    [25, 11, 21, 0.65, 34, 9, 2],
    [56, 7, 63, 0.3, 14, 5, 3],
    [33, 7, 29, 0.33, 16, 6, 4],
    [42, 24, 44, 0.76, 40, 16, 5],
    [82, 58, 90, 1.77, 68, 33, 6],
    [74, 49, 77, 1.46, 48, 27, 7],
    [78, 55, 80, 1.29, 59, 29, 8],
    [267, 216, 280, 4.8, 108, 64, 9],
    [185, 127, 216, 2.52, 61, 27, 10],
    [39, 19, 38, 0.57, 31, 15, 11],
    [41, 11, 40, 0.43, 21, 7, 12],
    [64, 38, 74, 1.04, 46, 22, 13],
    [108, 79, 120, 1.7, 75, 41, 14],
    [108, 63, 116, 1.48, 44, 26, 15],
    [33, 6, 29, 0.34, 13, 5, 16],
    [94, 66, 110, 1.54, 62, 31, 17],
    [186, 142, 192, 3.88, 93, 79, 18],
    [57, 31, 54, 0.96, 32, 14, 19],
    [22, 8, 17, 0.48, 23, 10, 20],
    [39, 15, 36, 0.61, 29, 13, 21],
    [94, 69, 114, 2.08, 73, 39, 22],
    [99, 73, 110, 2.43, 76, 48, 23],
    [31, 12, 30, 0.5, 32, 16, 24],
    [42, 27, 43, 1, 53, 22, 25],
    [154, 117, 157, 3.05, 92, 58, 26],
    [234, 185, 230, 4.09, 123, 69, 27],
    [160, 120, 186, 2.77, 91, 50, 28],
    [134, 96, 165, 2.76, 83, 41, 29],
    [52, 24, 60, 1.03, 50, 21, 30],
    [46, 5, 49, 0.28, 10, 6, 31]
    ]

value_sh = [
    [91, 45, 125, 0.82, 34, 23, 1],
    [65, 27, 78, 0.86, 45, 29, 2],
    [83, 60, 84, 1.09, 73, 27, 3],
    [109, 81, 121, 1.28, 68, 51, 4],
    [106, 77, 114, 1.07, 55, 51, 5],
    [109, 81, 121, 1.28, 68, 51, 6],
    [106, 77, 114, 1.07, 55, 51, 7],
    [89, 65, 78, 0.86, 51, 26, 8],
    [53, 33, 47, 0.64, 50, 17, 9],
    [80, 55, 80, 1.01, 75, 24, 10],
    [117, 81, 124, 1.03, 45, 24, 11],
    [99, 71, 142, 1.1, 62, 42, 12],
    [95, 69, 130, 1.28, 74, 50, 13],
    [116, 87, 131, 1.47, 84, 40, 14],
    [108, 80, 121, 1.3, 85, 37, 15],
    [134, 83, 167, 1.16, 57, 43, 16],
    [79, 43, 107, 1.05, 59, 37, 17],
    [71, 46, 89, 0.86, 64, 25, 18],
    [97, 71, 113, 1.17, 88, 31, 19],
    [84, 57, 91, 0.85, 55, 31, 20],
    [87, 63, 101, 0.9, 56, 41, 21],
    [104, 77, 119, 1.09, 73, 48, 22],
    [87, 62, 100, 1, 72, 28, 23],
    [168, 128, 172, 1.49, 97, 56, 24],
    [65, 45, 51, 0.74, 39, 17, 25],
    [39, 24, 38, 0.61, 47, 17, 26],
    [39, 24, 39, 0.59, 50, 19, 27],
    [93, 68, 96, 1.05, 79, 29, 28],
    [188, 143, 197, 1.66, 99, 51, 29],
    [174, 131, 174, 1.55, 108, 50, 30],
    [187, 143, 201, 1.39, 89, 53, 31]
    ]

c_schema = [
    {"name": "AQI", "max": 300, "min": 5},
    {"name": "PM2.5", "max": 250, "min": 20},
    {"name": "PM10", "max": 300, "min": 5},
    {"name": "CO", "max": 5},
    {"name": "NO2", "max": 200},
    {"name": "SO2", "max": 100}
    ]


def test_radar_user_define_schema_single():
    radar = Radar("雷达图示例")
    radar.config(c_schema=c_schema, shape='circle')
    radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
    radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None,
              legend_selectedmode='single')
    html_content = radar._repr_html_()
    assert 'single' in html_content
    assert 'multiple' not in html_content


def test_radar_user_define_schema_multiple():
    radar = Radar("雷达图示例")
    radar.config(c_schema=c_schema, shape='circle')
    radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
    radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None)
    html_content = radar._repr_html_()
    assert 'multiple' in html_content
    assert 'single' not in html_content
