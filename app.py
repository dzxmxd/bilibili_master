import os
from flask import Flask,render_template
from pyecharts.charts import Bar, Grid, Line, Pie
from pyecharts.charts import Funnel
from pyecharts.charts import Graph
import copy
from pyecharts.charts import Tree
from pyecharts import options as opts

app = Flask(__name__, static_folder="static")

# 格式解析，[0-当前排名，1-视频标题，2-播放数目，3-弹幕数量，4-综合得分，5-作者，6-视频地址，7-时长，8-评论数，9-收藏数，10-投币数，11-分享数，12-点赞数]

# 数据处理
with open('./bilibili.txt', 'r+',encoding='utf-8') as f:
    lst=[]
    for line in f.readlines():
        lst.append(line.split(','))

# 视频时长与播放完成度
def time_finish() -> Grid:
    """趋势不明显，但大致视频越短，播放完成度越高"""

    from pyecharts import options as opts
    from pyecharts.charts import Bar, Grid, Line

    Line_Bar_Grid = []
    for i in lst[0:10:]:
        Line_Bar_Grid.append(int(i[7]))

    x_data = ["第{}名".format(i) for i in range(1, 11)]
    bar = (
        Bar()
            .add_xaxis(x_data)
            .add_yaxis(
            "视频时长",
            [i for i in Line_Bar_Grid],
            yaxis_index=0,
            color="#d14a61", )
            .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=True, pos_left='30%', ),
            yaxis_opts=opts.AxisOpts(
                name="视频时长",
                position="right",
                axisline_opts=opts.AxisLineOpts(

                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}s"),
            ), )

    )
    line = (
        Line()
            .add_xaxis(x_data)
            .add_yaxis(
            "播放完成度",
            [0.90, 0.95, 0.94, 0.92, 0.91, 0.91, 0.65, 0.71, 0.99, 0.85],
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_global_opts(legend_opts=opts.LegendOpts(is_show=True, pos_right='30%', ))
    )

    grid = (
        Grid()
            .add(bar, grid_opts=opts.GridOpts())
            .add(line, grid_opts=opts.GridOpts())
    )
    return grid
@app.route("/time_finish_Chart")
def get_time_finish_chart():
    c = time_finish()
    return c.dump_options_with_quotes()

# 综合得分与评论点赞投币收藏趋势
def score_like() -> Line:
    line_Thread = []
    for i in lst[0:80:10]:
        play = float(i[2].strip("万"))
        line_Thread.append(
            [int(i[4]), int(play * 10000), int(i[12]), int(i[8]), int(i[9]), int(i[10])])  # 综合得分，播放，点赞，评论，收藏，投币

    #print(line_Thread)
    #print([i[1] for i in line_Thread])
    c = (
        Line()
            .add_xaxis(['1', '10', '20', '30', '40', '50', '60', '70', ])

            # .add_yaxis("播放", [i[1] for i in line_Thread]) # 播放数目
            .add_yaxis("点赞", [i[2] for i in line_Thread])
            # .add_yaxis("评论", [i[3] for i in line_Thread]) # 评论数过少
            .add_yaxis("收藏", [i[4] for i in line_Thread])
            .add_yaxis("投币", [i[5] for i in line_Thread])
            .set_global_opts(#title_opts=opts.TitleOpts(title="综合得分与评论点赞投币收藏趋势"),
                             yaxis_opts=opts.AxisOpts(name="综合得分", name_location="center", name_gap=70),
                             xaxis_opts=opts.AxisOpts(name="排行榜名次", name_location="center"))
    )
    return c
@app.route("/score_like_Chart")
def get_score_like_chart():
    c = score_like()
    return c.dump_options_with_quotes()

# 游客画像
def visitor_image() -> Pie:
    c = (
        Pie()
            .add(
            "",
            [list(z) for z in zip(["Andrioid端", "H5端", "PC端", "站外端", "iPhone端"], [60, 0, 23, 0, 17])],
            center=["30%", "30%"],
            radius=['15%', '30%'],

        )
            .add(
            "",
            [list(z) for z in zip(["16-25岁", "0-16岁", "25-40岁", "40岁以上", ], [44, 23, 21, 13])],
            center=["70%", "30%"],
            radius=['15%', '30%'],

        )
            .add(
            "",
            [list(z) for z in zip(["男性观众", "女性观众"], [24, 76])],
            center=["30%", "75%"],
            radius=['15%', '30%'],

        )
            #.set_colors(["#8be09c", "#ffc573", "#5ddfff", "#ff9db5"])

            .set_global_opts(
            #title_opts=opts.TitleOpts(title="游客画像"),
            legend_opts=opts.LegendOpts(
                is_show=False
            ),
        )
    )
    return c
@app.route("/visitor_image_Chart")
def get_visitor_image_chart():
    c = visitor_image()
    return c.dump_options_with_quotes()

# 漏斗图
def funnel_top() -> Funnel:
    data_fun = [[i[5], int(i[4])] for i in lst[0:20]]
    # 创建 Funnel 对象
    funnel_demo = (
        Funnel(init_opts=opts.InitOpts(
            width='800px',
            height='700px',
            page_title='page',
        ))
            .add("", data_fun, sort_='descending')
            .set_global_opts(title_opts=opts.TitleOpts(title=""), legend_opts=opts.LegendOpts(is_show=False))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True,
                                                       position="right",
                                                       # font_size = 12,
                                                       ))
    )
    return funnel_demo
@app.route("/funnel_top_Chart")
def get_funnel_top_chart():
    c = funnel_top()
    return c.dump_options_with_quotes()

# 排行榜部分视频点赞投币白嫖占比
def pie_many() -> Pie:
    b_pie = []
    for i in lst[0:12]:
        play = float(i[2].strip("万"))
        like = int(i[12])
        coin = int(i[10])
        favorite = int(i[9])

        b_pie.append(
            [i[1], [("白嫖", play * 10000 - like - coin - favorite), ("点赞", like), ("投币", coin), ("收藏", favorite)]])

    x = 10
    y = 25
    pie_demo = (Pie())
    for i in b_pie:
        x_term = str(x) + '%'
        y_term = str(y) + '%'
        #print(x_term, y_term)
        pie_demo.add(i[0], i[1], center=[x_term, y_term], radius='16%', )
        x += 16
        if (x >= 100):
            x = 10
            y += 50
    # pie_demo.set_global_opts(title_opts=opts.TitleOpts(title="白嫖数量"))
    return pie_demo
@app.route("/pie_many_Chart")
def get_pie_many_chart():
    c = pie_many()
    return c.dump_options_with_quotes()

# 综合得分计算指标
def relation_like() -> Graph:
    """
    数据来源：贴吧
    1收藏：0.49
    分享：0.17
    1弹幕：0.17
    硬币：0.0375
    1点赞：0.0375
    1评论：0.0375
    点踩：0.0375
    1播放：0.02
    """
    # 扩大200倍，便于绘图
    nodes = [
        {"name": "弹幕", "symbolSize": 0.17 * 200},
        {"name": "收藏", "symbolSize": 0.49 * 200},
        {"name": "评论", "symbolSize": 0.0375 * 200},
        {"name": "点赞", "symbolSize": 0.0375 * 200},
        {"name": "播放", "symbolSize": 0.02 * 200},
        {"name": "分享", "symbolSize": 0.17 * 200},
        {"name": "硬币", "symbolSize": 0.0375 * 200},
        {"name": "点踩", "symbolSize": 0.0375 * 200},
        # {"name": "转发", "symbolSize": 40},
        # {"name": "时长", "symbolSize": 30},
        # {"name": "综合得分", "symbolSize": 20},
    ]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get("name"), "target": j.get("name")})
    c = (
        Graph()
            .add("", nodes, links, repulsion=8000)
        # .set_global_opts(title_opts=opts.TitleOpts(title="综合得分计算指标"))
    )
    return c
@app.route("/relation_like_Chart")
def get_relation_like_chart():
    c = relation_like()
    return c.dump_options_with_quotes()

# 视频时长与受欢迎程度
def time_like() -> Line:
    b_lst = []
    for line in lst:
        try:
            b_lst.append([int(line[7]), int(line[4])//1000])  # 视频时长与综合得分
        except:
            pass

    b_lst.pop()  # 多出一个哔哩哔哩创作中心，格式与up主不符合，去掉

    b_lst.sort(key=lambda x: x[0])  # 按照视频时长进行排序
    # 采取每10条视频取平均值方法以便于观察曲线趋势
    b_mean = [[sum(i[0] for i in b_lst[0:10]) // 10, sum(i[1] for i in b_lst[0:10]) // 10],
              [sum(i[0] for i in b_lst[10:20]) // 10, sum(i[1] for i in b_lst[10:20]) // 10],
              [sum(i[0] for i in b_lst[20:30]) // 10, sum(i[1] for i in b_lst[20:30]) // 10],
              [sum(i[0] for i in b_lst[30:40]) // 10, sum(i[1] for i in b_lst[30:40]) // 10],
              [sum(i[0] for i in b_lst[40:50]) // 10, sum(i[1] for i in b_lst[40:50]) // 10],
              [sum(i[0] for i in b_lst[50:60]) // 10, sum(i[1] for i in b_lst[50:60]) // 10],
              [sum(i[0] for i in b_lst[60:70]) // 10, sum(i[1] for i in b_lst[60:70]) // 10],
              [sum(i[0] for i in b_lst[70:80]) // 10, sum(i[1] for i in b_lst[70:80]) // 10],
              [sum(i[0] for i in b_lst[80:90]) // 10, sum(i[1] for i in b_lst[80:90]) // 10],
              [sum(i[0] for i in b_lst[90:99]) // 10, sum(i[1] for i in b_lst[90:99]) // 10],
              ]

    x_data = [i[0] for i in b_lst]
    y_data = [i[1] for i in b_mean]

    c = (
        Line(init_opts=opts.InitOpts(width='100px', height='400px'))
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                position="left",
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            # series_name="综合得分",
            series_name="",
            y_axis=y_data,
            symbol="emptyCircle",
            is_symbol_show=True,
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
    )
    return c
@app.route("/time_like_Chart")
def get_time_like_chart():
    c = time_like()
    return c.dump_options_with_quotes()

# 凑数的图
def tree_image() -> Tree:
    data = [
        {
            "children": [
                {"name": "收藏"},
                {
                    "children": [{"children": [{"name": "点赞"}], "name": "投币"}, {"name": "分享"}],
                    "name": "点赞",
                },
                {
                    "children": [
                        {"children": [{"name": "点踩"}, {"name": "举报"}], "name": "举报"},
                        {"name": "小黑屋"},
                    ],
                    "name": "点踩",
                },
            ],
            "name": "观看",
        }
    ]
    c = (
        Tree()
            .add("", data)
            .set_global_opts(title_opts=opts.TitleOpts(title=""))

    )
    return c
@app.route("/tree_image_Chart")
def tree_image_chart():
    c = tree_image()
    return c.dump_options_with_quotes()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port='5000')