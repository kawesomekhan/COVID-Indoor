from dash import html
import descriptions_links as links

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

descriptions_zh: Simplified Chinese

"""

filt_type_output_base = "MERV {:.0f}"
recirc_type_output_base = "{:.1f} 再循环换气率"

# Default dropdown options shared between basic mode and advanced mode
humidity_marks = {
    0.01: {'label': '1%: 非常干', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: 飞机', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: 干'},
    0.6: {'label': '60%: 一般'},
    0.99: {'label': '99%: 非常湿润'},
}

exertion_types = [
    {'label': "休息", 'value': 0.49},
    {'label': "站立", 'value': 0.54},
    {'label': "唱歌", 'value': 1},
    {'label': "低强度运动", 'value': 1.38},
    {'label': "中等强度运动", 'value': 2.35},
    {'label': "高强度运动", 'value': 3.30},
]

expiratory_types = [
    {'label': "呼吸（轻）", 'value': 1.1},
    {'label': "呼吸（轻）", 'value': 4.2},
    {'label': "呼吸（重）", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "说话（耳语）", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "说话（正常）", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "说话（大声）", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "唱歌", 'value': 970},
]

mask_type_marks = {
    0: {'label': "0% (无，面罩)", 'style': {'max-width': '75px'}},
    0.5: {'label': "50% (棉布，毛绒)", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (多层棉质，丝质)", 'style': {'max-width': '75px'}},
    0.90: {'label': "90% (一次性手术口罩)", 'style': {'max-width': '75px'}},
    # 0.99: {'label': "99% (N95 resp-irator)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "无，面罩", 'value': 0},
    {'label': "棉布，毛绒", 'value': 0.5},
    {'label': "多层棉质，丝质", 'value': 0.7},
    {'label': "一次性手术口罩", 'value': 0.9},
    {'label': "N95呼吸器", 'value': 0.99},
]

mask_fit_marks = {
    0: {'label': '0%: 无', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: 差'},
    0.95: {'label': '95%: 好'}
}

risk_tol_marks = {
    0.01: {'label': '0.01: 更安全', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: 安全', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: 不安全'}
}

n_max_base_string = ' {:.0f} 人'
n_max_overflow_base_string = ' >{:.0f} 人'

ventilation_types = [
    {'label': "关闭窗户", 'value': 0.3},
    {'label': "打开窗户", 'value': 2},
    {'label': "机械通风", 'value': 3},
    {'label': "打开窗户，且有风扇", 'value': 6},
    {'label': "更好的机械通风", 'value': 8},
    {'label': "实验室，餐厅", 'value': 9},
    {'label': "酒吧", 'value': 15},
    {'label': "医院/地铁车", 'value': 18},
    {'label': "有毒实验室/飞机", 'value': 24},
]

filter_types = [
    {'label': "无", 'value': 0},
    {'label': "家用窗式空调", 'value': 2},
    {'label': "住宅/商业/工业", 'value': 6},
    {'label': "住宅/商业/医院", 'value': 10},
    {'label': "医院与普通外科", 'value': 14},
    {'label': "高效颗粒吸附器", 'value': 17}
]

recirc_types = [
    {'label': "无", 'value': 0},
    {'label': "慢", 'value': 0.3},
    {'label': "中等", 'value': 1},
    {'label': "快", 'value': 10},
    {'label': "飞机", 'value': 24},
    {'label': "地铁", 'value': 54},
]

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"

graph_title = "容纳人数 vs.暴露时间"
graph_xtitle = "最大暴露时间 t(小时)"
graph_ytitle = "最大容纳人数 N"
transient_text = "非稳态"
steady_state_text = "稳态"

six_ft_base_string = ' {} 个人'
six_ft_base_string_one = ' {} 个人'

units_hr = '小时'
units_min = '分钟'
units_days = '天'
units_months = '月'

units_hr_one = '小时'
units_min_one = '分钟'
units_day_one = '天'
units_month_one = '月'

is_past_recovery_base_string = '{n_val} 人，>{val:.0f} 天'
model_output_base_string = '{n_val} 人，'
nt_bridge_string = " 人， "
tn_bridge_string = " "

presets = [
    {'label': "自定义", 'value': 'custom'},
    {'label': "郊区的房子", 'value': 'house'},
    {'label': "餐馆", 'value': 'restaurant'},
    {'label': "办公室", 'value': 'office'},
    {'label': "课堂", 'value': 'classroom'},
    {'label': "客厅", 'value': 'living-room'},
    {'label': "地铁", 'value': 'subway'},
    {'label': "飞机", 'value': 'airplane'},
    {'label': "教堂", 'value': 'church'},
]

curr_human_header = "人的行为: "
presets_human = [
    {'label': "自定义", 'value': 'custom'},
    {'label': "戴口罩休息", 'value': 'masks-1'},
    {'label': "戴口罩讲话", 'value': 'masks-2'},
    {'label': "戴口罩运动", 'value': 'masks-3'},
    {'label': "不戴口罩休息", 'value': 'no-masks-1'},
    {'label': "不戴口罩讲话", 'value': 'no-masks-2'},
    {'label': "不戴口罩运动", 'value': 'no-masks-3'},
    {'label': "不戴口罩唱歌", 'value': 'singing-1'},
]

curr_risk_header = "风险承受能力: "
# presets_risk = [
#     {'label': "Low", 'value': 0.01},
#     {'label': "Medium", 'value': 0.1},
#     {'label': "High", 'value': 1},
# ]
risk_tol_marks = {
    # 0.01: {'label': '0.01: Safer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: 更安全', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: 不安全'}
}

# risk_tolerance_text = "Risk Tolerance: "
# risk_tol_desc = html.Div('''More vulnerable populations such as the elderly or those with preexisting medical
# conditions require a lower risk tolerance (~0.01). A higher risk tolerance will mean more expected
# transmissions during the expected occupancy period (see FAQ for details).''', style={'font-size': '13px',
#                                                                                      'margin-left': '20px'})

curr_age_header = "年龄阶层: "
presets_age = [
    {'label': "儿童（<15岁）", 'value': 0.23},
    {'label': "成人（15-64岁）", 'value': 0.68},
    {'label': "老年人（> 64岁）", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: 儿童（<15岁）', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: 成人（15-64岁）', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: 老年人（> 64岁）', 'style': {'width': '75px'}}
}

curr_strain_header = "病毒株: "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "SARS-CoV-2（武汉毒株）", 'value': 1},
    {'label': "SARS-CoV-2 - B.1.1.7（英国毒株）", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: 武汉', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: B.1.1.7 /英国'}
}

pim_header = "免疫率: "
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "如果感染者进入…"
risk_prevalence_desc = "在给定的感染率下..."
risk_personal_desc = "为了减少我的风险…"
risk_options = [
    {'label': risk_conditional_desc, 'value': 'conditional'},
    {'label': risk_prevalence_desc, 'value': 'prevalence'},
    {'label': risk_personal_desc, 'value': 'personal'},
]

error_list = {
    "floor_area": "错误：地板面积不能为空。",
    "ceiling_height": "错误：天花板高度不能为空。",
    "recirc_rate": "错误：再循环率不能为空。",
    "aerosol_radius": "错误：气溶胶液滴半径不能为空。",
    "viral_deact_rate": "错误：病毒失活速率不能为空。",
    "n_max_input": "错误：人数不能少于2。",
    "exp_time_input": "错误：暴露时间必须大于0。",
    "air_exchange_rate": "错误：通风率（ACH）必须大于0。",
    "merv": "错误：过滤系统（MERV）不能为空。",
    "prevalence": "错误：感染率（每十万人的感染人数）必须大于0且小于100,000。",
}

# Header
header = html.Div([
    html.H1(children='新冠肺炎室内安全指南'),
    html.Div([
        html.Div([html.Span(html.A(href="https://www.linkedin.com/in/kasim-k-a92620b1/",
                                   children="Kasim Khan",
                                   target='_blank')),
                  ", ",
                  html.Span(html.A(href="https://math.mit.edu/~bush/",
                                   children="John W. M. Bush",
                                   target='_blank')),
                  ", and ",
                  html.Span(html.A(href="https://www.mit.edu/~bazant/",
                                   children="Martin Z. Bazant",
                                   target='_blank')),
                  ""]),
        html.Div([html.Span(["Beyond Six Feet: A Guideline to Limit Indoor Airborne Transmission of COVID-19 ("]),
                  html.Span(html.A(href=link_paper,
                                   target='_blank',
                                   children='''Bazant & Bush, 2020''')),
                  html.Span(")")]),
        html.Div([
            html.A(href='http://web.mit.edu/bazant/www/COVID-19/',
                   children='''
                            http://web.mit.edu/bazant/www/COVID-19/
                        ''', target='_blank'),
        ]),
        html.Div([
            html.A(href='https://github.com/kawesomekhan/covid-indoor',
                   children=[
                       "https://github.com/kawesomekhan/covid-indoor"
                   ],
                   target='_blank'),
        ]),
    ], className='header-small-text')
])

# Menu dropdowns
language_dd = "语言: "
units_dd = "单位: "
mode_dd = "模式: "

# Unit systems
unit_settings = [
    {'label': "英制", 'value': "british"},
    {'label': "公制", 'value': "metric"},
]

# Modes
app_modes = [
    {'label': "基础", 'value': "basic"},
    {'label': "高级", 'value': "advanced"},
]

# Tabs
about_header = "关于"
room_header = "房间规格-详细信息:"
human_header = "人的行为-详细信息："
faq_header = "常见问题"
other_io = "其他参数"

# About
about = html.Div([
    html.H6("关于", style={'margin': '0'}),
    html.Div('''为抑制新冠肺炎的传播，官方公共卫生指南建议限制以下因素：人与人之间的距离（6英尺/ 2米），房间占用时间（15分钟），房间内最大人数
                （25人）或最小通风量（每小时换气6次）。'''),
    html.Br(),
    html.Div([html.Span('''越来越多的 '''),
              html.A(children="科学证据",
                     href=link_docs,
                     target='_blank'),
              html.Span('''表明，人们在室内可以通过呼吸而吸入有传染性的气溶胶，从而导致新冠肺炎可以通过空气传播。
                           尽管公共卫生组织开始认识到空气传播的重要性，但他们尚未提供包含所有相关变量的安全指南。''')]),
    html.Br(),
    html.Div([html.Span('''本应用程序是由Kasim Khan与Martin Z. Bazant，John W. M. Bush合作开发，用'''),
              html.A(children="理论模型",
                     href=link_paper,
                     target='_blank'),
              html.Span('''来计算室内空间的安全暴露时间和可容纳人数。通过调整房间规格，通风率和过滤率，使用口罩情况，呼吸活动和风险承受能力
                           （在其他选项卡中），您可以了解如何减轻室内新冠肺炎传播。''')]),
    html.Br(),
    html.Div([html.Span('''该应用程序背后的科学基础已上线edX上的慕课（MOOC, 免费且自定进度的大规模开放在线课堂）：'''),
              html.A(children="10.S95x 新冠肺炎传播的物理原理。",
                     href=links.link_mooc,
                     target='_blank')]),
])

# Room Specifications
floor_area_text = "总建筑面积（平方英尺）: "
floor_area_text_metric = "总建筑面积 (m²): "

ceiling_height_text = "平均天花板高度（英尺）："
ceiling_height_text_metric = "平均天花板高度 (m): "

ventilation_text = "通风系统: "
ventilation_text_adv = html.Span(["通风系统 (hr", html.Sup("-1"), ", 户外 ACH): "])
vent_type_output_base = "{:.1f} ACH"
vent_type_output_units = html.Span(["hr", html.Sup("-1"), " (户外 ACH)"])

filtration_text = "过滤系统: "
filtration_text_adv = "过滤系统 (MERV): "

recirc_text = "循环率: "
recirc_text_adv = "循环率 (再循环换气率): "

humidity_text = "相对湿度: "

need_more_ctrl_text = '''需要控制更多参数吗？使用页面顶部的下拉菜单切换到高级模式。'''

# Human Behavior
exertion_text = "呼吸率: "

breathing_text = "呼吸活动: "

mask_type_text = "口罩过滤效率（口罩类型）： "

mask_fit_text = "面罩贴合/合规性: "

risk_tolerance_text = "风险承受度: "

# FAQ/Other Inputs and Outputs
assumptions_layout = html.Div([
    html.H5("其他问题?"),
    html.Div([html.Span('''有关更多详细的说明和参考，请参阅'''),
              html.A(children="这篇文章",
                     href=link_paper,
                     target='_blank'),
              html.Span('''以及页面顶部发布的其他链接。''')]),
])

faq_top = html.Div([
    html.H6("常见问题"),
    html.H5("为什么6英尺/ 2米的间距不够？"),
    html.Div([
        html.Div([html.Span('''6英尺/ 2米的间距和口罩都可以防止接触到感染者咳嗽时喷出的大液滴。
        但是这不能防止悬浮在空气中并且可以在整个房间中扩散混合的具有传染性的气溶胶导致的'''),
                  html.A(children="空气传播",
                         href=link_docs,
                         target='_blank'),
                  html.Span('''。 在室内，6英尺和60英尺的社交距离没有太大的差别。''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("还有其他传播方式吗？"),
    html.Div([
        html.Div([html.A(children="空气传播",
                         href=link_docs,
                         target='_blank'),
                  html.Span('''被认为是新冠肺炎的主要传播途径，但其他方式也是可能的，例如通过直接接触表面上的传染性残留物进行传播，
                  通过咳嗽或打喷嚏的“大液滴”传播以及通过长时间吸入被感染人士呼出气体的“短距离气溶胶”传播。 
                  戴上口罩或面罩可以大大降低后两种传播模式； 但仍有空气传播的风险。''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("真的可以假设房间空气充分混合吗？"),
    html.Div([
        html.Div([html.Span('''室内空间空气混合的原因很多，包括浮力驱动的气流（来自加热器，空调或窗户），通风口和风扇的强制对流，
        以及人体运动和呼吸。 除了一些特殊情况（见这篇'''),
                  html.A(children="论文",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''的讨论），充分混合的假设广泛应用于空气传播疾病的理论模型。''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("该指南适用于非常大的空间吗？"),
    html.Div([
        html.Div([html.Span('''在音乐厅，体育馆或其他人口众多的大型通风场所中空气传播的风险较高，本指南对此有较好的估计。 
                            但是，如果不戴口罩或面罩，则还存在通过呼吸射流进行短距离传播的风险（见这篇'''),
                  html.A(children="论文",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''的估计）。''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("为什么要知道天花板高度？"),
    html.Div([
        '''天花板高度会影响总房间容积，这是估算传染性气溶胶浓度（每单位体积的气溶胶液滴数量）所必需的。 需要此浓度来估算房间的新冠肺炎传播风险。'''
    ], className='faq-answer'),
    html.Br(),
    html.H5("我知道我的ACH / MERV号码。 我在哪里可以输入？"),
    html.Div('''
        如果您需要输入更多选项，请使用网页顶部的下拉菜单切换到高级模式。
    ''', className='faq-answer'),
    html.Br(),
    html.H5("为什么N95呼吸器具有99％的效率？"),
    html.Div('''N95呼吸器对于0.3μm粒径的液滴具有至少95%的过滤效率。而新冠病毒空气传播中液滴大小大概是3μm。对于较大的液滴，N95呼吸器的过滤效率更高，接近100％的水平。''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("基本模式下是否有任何隐藏的参数？"),
    html.Div([html.Span(''''''),
              html.A(children="本文",
                     href=link_paper,
                     target='_blank'),
              html.Span('''详细介绍了所有相关的物理参数。 在基础模式下，该应用假定默认有效气溶胶液滴半径为2μm（在湿度为60％时），
              最大病毒失活速率为0.6 / hr（在湿度大约为100％时），两者均随相对湿度（RH）的增加而增加。 我们保守地低估病毒失活的速率。 
              病毒失活速率可因紫外线（UV-C）或化学消毒剂（例如过氧化氢，臭氧）增大。
              该应用程序用了'''),
              html.Span(''''''),
              html.A(children="该文章",
                     href=link_paper,
                     target='_blank'),
              html.Span('''图2中表格的数据以及指定的呼吸活动来估算关键参数，例如呼出空气的传染性Cq（每单位体积的感染量）。 
              您可以在“高级模式”中自行定义这些参数。''')],
             className='faq-answer'),
])
aerosol_radius_text = "有效气溶胶液滴半径（在RH = 60％时）， r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["最大病毒失活速率（在RH = 100％时）， \u03BB", html.Sub('vmax'), " (/小时): "])

pop_immunity_header = "人群免疫力: "
perc_immune_label = html.Span(["免疫率 p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["感染率 p", html.Sub('i'), " = "])
perc_vaccinated_label = html.Span(["疫苗接种率 p", html.Sub('v'), " ="])
perc_prev_infected_label = html.Span(["已感染率 p", html.Sub('ex'), " = "])
perc_susceptible_label = html.Span(["易感率 p", html.Sub('s'), " = 1 - (p", html.Sub('im'), " + p",
                                    html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''人群的感染性 p''', html.Sub('i'), ''' 是根据在”其他风险情景”选项卡中输入的感染率计算得出的（在......感染率下， 
为了限制我被感染的风险，应当…...）。通过计算人群的疫苗接种率加上人群中总发病率（忽略未发现的病例），可以对免疫率 p''', html.Sub('im'), ''' 做保守估计。用这两个值可以计算易感率 p''', html.Sub('s'), ''' 在”基本模式”和“首位风险”模式下（如果一个感染者进入…...），该值假定为100％。''']),
                              html.Br(),
                              html.Div(['''以下是一些关于 p''', html.Sub('i'), ''' 和 p''',
                                        html.Sub('im'), ''' 的链接：''',
                                        html.Span(html.A(href=links.link_cdc_dashboard,
                                                         children="CDC COVID-19 Data Tracker",
                                                         target='_blank')),
                                        html.Span(", "),
                                        html.Span(html.A(href=links.link_jhu_data,
                                                         children="JHU Coronavirus Resource Center",
                                                         target='_blank')),
                                        html.Span(", "),
                                        html.A(children="US Immunity Estimates",
                                               href=links.link_cdc_immunity,
                                               target='_blank'),
                                        html.Span(", "),
                                        html.A(children="International Immunity Estimates",
                                               href=links.link_jhu_vaccine,
                                               target='_blank'),
                                        ])
                              ])

values_interest_header = "相关量的计算值"
values_interest_desc = html.Div([
    html.H5("该应用程序究竟在计算什么？"),
    html.Div([
        html.Div([html.Span('''本应用程序会计算室内的最大允许累积暴露时间，即房间人数和时间的乘积。 这个限制是这样得到的：要求每个感染个体的预期传染人数（“室内再生数”）小于所选的风险承受能力。如果感兴趣，您可以参考本应用程序计算的相关量 '''),
                  html.A(children="（定义见文章）",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''': ''')]),
    ], className='faq-answer'),
])
relative_sus_label = html.Span(["相对易感性 s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["室外空气分数 Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Aerosol filtration efficiency p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Breathing flow rate Q", html.Sub('b'), ": "])
cq_label = html.Span(["Infectiousness of exhaled air C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Mask passage probability p", html.Sub('m'), ": "])
room_vol_label = html.Span(["总房间容积 V: "])
vent_rate_Label = html.Span(["Ventilation (outdoor) flow rate Q: "])
recirc_rate_label = html.Span(["Return (recirculation) flow rate Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["空气过滤率 (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["湿度修正后气溶胶半径 r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["湿度修正后病毒失活速率 \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["有效气溶胶沉降速度 v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["浓度松弛速率 \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["空气传播速率 \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("该模型是否考虑了当地人口的感染率?"),
    html.Div(['''可以在“高级模式”中考虑当地感染率的影响。在“高级模式”的“其他参数”选项卡中，您还可以评估人群免疫率的影响。人群免疫率可能会由于疫苗接种或先前感染而升高。'''],
             className='faq-answer'),
])

risk_tol_desc = html.Div('''对于老年人等较脆弱的人群或已有疾病的人群，需要设置较低的风险承受度。设置较高的风险承受度，
意味着在给定时间内预期会有更多传染事件（有关详细信息，请参阅常见问题解答）。''', style={'font-size': '13px',
                                                  'margin-left': '20px'})

# Main Panel Text
curr_room_header = "当前房间: "
main_panel_s1 = "根据本模型，当这个房间容纳不同的人数时，安全暴露时间为："
main_panel_six_ft_1 = "作为对比，六英尺（或两米）距离的指导方针会将使用人数限制在 "
main_panel_six_ft_2 = " 这会在 "
main_panel_six_ft_3 = " 之后违反本指南*"

main_panel_s1_b = html.Span([
    html.Span('''为了控制COVID-19在感染率1为每100,000中'''),
    html.Sup('''1'''),
    html.Span(''' ''')
])
main_panel_s2_b = ''' 人的人群中的传播*，该空间不得有超过：'''

main_panel_s1_c = html.Span([
    html.Span('''为了降低我在感染率为每100,000中'''),
    html.Sup('''1'''),
    html.Span(''' ''')
])
main_panel_s2_c = ''' 人的人群中感染COVID-19的可能性，此空间不得有超过：'''

main_airb_trans_only_disc = html.Div(["本指南将累计暴露时间内每个感染者通过空气传播感染他人的可能性限制在风险承受能力之下。",
                                      html.Span(html.A(href=links.link_docs,
                                                       children="",
                                                       target='_blank'), ),
                                      html.Span("")], className='airborne-text')
main_airb_trans_only_disc_basic = html.Div(["*本指南将累计暴露时间内每个感染者 ",
                                            html.Span(html.A(href=links.link_docs,
                                                             children="通过空气传染他人",
                                                             target='_blank'), ),
                                            html.Span(''' 的可能性限制在风险承受能力（10%）之下。''')], className='airborne-text')

other_risk_modes_desc = html.Div('''“高级模式”考虑了其他风险情景。具体来说，可以考虑人群中的感染率，通过疫苗接种或先前接触获得的免疫率，以及对特定个体的风险。''')

main_airb_trans_only_desc_b = html.Div(["本指南将将累计暴露时间内每个感染者通过空气传染他人的可能性限制在风险承受能力之下。",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="",
                                                         target='_blank'), ),
                                        html.Span('''''')], className='airborne-text')
main_airb_trans_only_desc_c = html.Div(["本指南将累积暴露时间内特定个体通过空中传播被感染的可能性限制在风险承受能力以下。",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="",
                                                         target='_blank'), ),
                                        html.Span('''''')], className='airborne-text')

# Bottom panels text
n_input_text_1 = "如果该房间有 "
n_input_text_2 = " 人，根据本指南则不可逗留超过 "
n_input_text_3 = "小时。"

t_input_text_1 = "如果人们在这里停留约 "
t_input_text_2 = " 个小时，则人数应限制为"
t_input_text_3 = "。"

airb_trans_only_disc = html.Div('''''', className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''为了估算您的本地感染率，这里有一些有用的资源：'''),
                                html.Span(html.A(href=links.link_cdc_dashboard,
                                                 children="美国疾控中心公布的新冠肺炎数据跟踪系统",
                                                 target='_blank')),
                                html.Span(", "),
                                html.Span(html.A(href=links.link_jhu_data,
                                                 children="约翰霍普金斯大学的冠状病毒资源中心",
                                                 target='_blank')),
                                html.Span(", "),
                                html.A(children="美国免疫预测分析",
                                       href=links.link_cdc_immunity,
                                       target='_blank'),
                                html.Span(", "),
                                html.A(children="国际免疫预测分析",
                                       href=links.link_jhu_vaccine,
                                       target='_blank'),
                                ], className='airborne-text')

footer = html.Div([
    html.Div([html.Span('''《MIT新冠肺炎室内安全指南》是一个正在被不断改进的工具，
    旨在使感兴趣的用户熟悉影响新冠肺炎在室内空气传播风险的因素，并帮助用户在各种情况下定量评估风险。我们注意到，
    该模型参数的不确定性和多变性可能导致高达一个数量级的误差。这种情况下可以通过选择足够小的风险承受度来对模型预测进行修正。
    我们的《指南》并未考虑通过呼吸喷出物的短距离传播，这可能会在未佩戴口罩的情况下大大提高风险（该方式在'''),
              html.A(children="Bazant＆Bush, 2020",
                     href=link_paper,
                     target='_blank'),
              html.Span('''手稿中进行了讨论）。用户自身须对使用该《 MIT新冠肺炎室内安全指南》负责。
              开发者不作任何形式的保证或担保，并对其使用不承担任何责任。''')]),
    html.Br(),
    html.Div("特别鸣谢")
], className='footer-small-text')
