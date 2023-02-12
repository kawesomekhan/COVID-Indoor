from dash import html

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

Dutch

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"

# Header
header = html.Div([
    html.H1(children='COVID-19 Veiligheidsrichtlijn gesloten ruimtes'),
    html.Div([
        html.Div([html.Span(html.A(href="https://www.linkedin.com/in/kasim-k-a92620b1/",
                                   children="Kasim Khan",
                                   target='_blank')),
                  ", ",
                  html.Span(html.A(href="https://math.mit.edu/~bush/",
                                   children="John W. M. Bush",
                                   target='_blank')),
                  ", en ",
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
language_dd = "Taal: "

# Unit systems
units_dd = "Eenheden: "
unit_settings = [
    {'label': "Brits", 'value': "british"},
    {'label': "Metrisch", 'value': "metric"},
]

# Modes
mode_dd = "Modus: "
app_modes = [
    {'label': "Basis", 'value': "basic"},
    {'label': "Geavanceerd", 'value': "advanced"},
]

error_list = {
    "floor_area": "Fout: vloeroppervlak moet groter zijn dan 0.",
    "ceiling_height": "Fout: plafondhoogte moet groter zijn dan 0.",
    "recirc_rate": "Fout: recirculatiesnelheid moet groter zijn dan 0.",
    "aerosol_radius": "Fout: aerosolradius moet groeter zijn dan 0.",
    "viral_deact_rate": "Fout: de mate van deactivering van virussen moet groeter zijn dan 0.",
    "n_max_input": "Fout: aantal personen mag niet minder zijn dan 2.",
    "exp_time_input": "Fout: de belichtingstijd moet groter zijn dan 0.",
    "air_exchange_rate": "Fout: ventilatiesnelheid (ACH) moet groter zijn dan 0.",
    "merv": "Fout: Kies een type filtersysteem (MERV)."
}

# Main Panel Text
curr_room_header = "Type ruimte: "
presets = [
    {'label': "Vrij te kiezen", 'value': 'custom'},
    {'label': "Vrijstaand huis", 'value': 'house'},
    {'label': "Restaurant", 'value': 'restaurant'},
    {'label': "Rustig kantoor", 'value': 'office'},
    {'label': "Schoolklas of lesruimte", 'value': 'classroom'},
    {'label': "Metro-stel / treinstel", 'value': 'subway'},
    {'label': "Boeing 737", 'value': 'airplane'},
    {'label': "Kerk", 'value': 'church'},
]

main_panel_s1 = "Op basis van dit model zou het in deze ruimte veilig* moeten zijn voor: "

units_hr = 'uur lang'
units_min = 'minuten'
units_days = 'dagen lang'

units_hr_one = 'uur lang'
units_min_one = 'minuten'
units_day_one = 'dagen lang'

is_past_recovery_base_string = '{n_val} mensen, >{val:.0f} dagen lang,'
model_output_base_string = '{n_val} mensen, '

main_panel_six_ft_1 = "Nota: de afstandsrichtlijn van twee meter zou betekenen dat maximaal "
main_panel_six_ft_2 = " in deze ruimte mogen zijn, en dan voor onbepaalde tijd."

six_ft_base_string = ' {} mensen'
six_ft_base_string_one = ' {} mensen'

graph_title = "Bezettingsgraad t.o.v. blootstellingstijd"
graph_xtitle = "Maximale belichtingstijd \u03C4 (uur)"
graph_ytitle = "Maximale bezettingsgraad N"
transient_text = "Tijdsafhankelijk"
steady_state_text = "Tijdsonafhankelijk"

main_airb_trans_only_disc = html.Div(["*Deze richtlijn is gebaseerd op ",
                                      html.Span(html.A(href='https://www.nature.com/articles/d41586-020-02058-1',
                                                       children="overdracht via de lucht",
                                                       target='_blank'), ),
                                      html.Span(''', vanwege een enkele besmette persoon, gedurende de vermelde 
                                      cumulatieve blootstellingstijd.''')], className='airborne-text')

airb_trans_only_disc = html.Div('''Deze richtlijn is gebaseerd op overdracht via de lucht , vanwege een enkele 
besmette persoon, gedurende de vermelde cumulatieve blootstellingstijd.''', className='airborne-text')

# Bottom panels text
n_input_text_1 = "Als er in deze ruimte "
n_max_base_string = ' {:.0f} mensen'
n_input_text_2 = " mensen zijn, zouden de bewoners "
n_input_text_3 = " veilig moeten zijn."

t_input_text_1 = "Als de personen hier ongeveer "
t_input_text_2 = " uur doorbrengen, moet de bezetting worden beperkt tot "
t_input_text_3 = "."

# About
about_header = "Over"
about = html.Div([
    html.H6("Over", style={'margin': '0'}),
    html.Div('''To mitigate the spread of COVID-19, official public health guidelines have recommended limits on: 
    person-to-person distance (6 feet / 2 meters), occupancy time (15 minutes), maximum occupancy (25 people), 
    or minimum ventilation (6 air changes per hour).'''),
    html.Br(),
    html.Div([html.Span('''There is growing '''),
              html.A(children="scientific evidence",
                     href=link_docs,
                     target='_blank'),
              html.Span(''' for airborne transmission of COVID-19, which occurs when 
    infectious aerosol droplets are exchanged by breathing shared indoor air. While public health organizations are 
    beginning to acknowledge airborne transmission, they have yet to provide a safety guideline that incorporates all 
    the relevant variables.''')]),
    html.Br(),
    html.Div([html.Span('''This app, developed by Kasim Khan in collaboration with Martin Z. Bazant and John W. M. Bush, 
    uses a '''),
              html.A(children="theoretical model",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' to calculate safe exposure times and occupancy levels for indoor spaces.  By adjusting 
    room specifications, ventilation and filtration rates, face-mask usage, respiratory activities, 
    and risk tolerance (in the other tabs), you can see how to mitigate indoor COVID-19 transmission in different 
    indoor spaces.''')]),
])

# Room Specifications
room_header = "Room Specifications"

floor_area_text = "Total floor area (sq. ft.): "
floor_area_text_metric = "Total floor area (m²): "
ceiling_height_text = "Average ceiling height (ft.): "
ceiling_height_text_metric = "Average ceiling height (m): "

ventilation_text = "Ventilation System: "
vent_type_output_base = "{:.0f} ACH"
ventilation_text_adv = "Ventilation System (ACH): "
ventilation_types = [
    {'label': "Closed windows", 'value': 0.3},
    {'label': "Open windows", 'value': 2},
    {'label': "Mechanical Ventilation", 'value': 3},
    {'label': "Open windows with fans", 'value': 6},
    {'label': "Better Mechanical Ventilation", 'value': 8},
    {'label': "Laboratory, Restaurant", 'value': 9},
    {'label': "Bar", 'value': 15},
    {'label': "Hospital/Subway Car", 'value': 18},
    {'label': "Toxic Laboratory/Airplane", 'value': 24},
]

filtration_text = "Filtration System: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "Filtration System (MERV): "
filter_types = [
    {'label': "None", 'value': 0},
    {'label': "Residential Window AC", 'value': 2},
    {'label': "Residential/Commercial/Industrial", 'value': 6},
    {'label': "Residential/Commercial/Hospital", 'value': 10},
    {'label': "Hospital & General Surgery", 'value': 14},
    {'label': "HEPA", 'value': 17}
]

recirc_text = "Recirculation Rate: "
recirc_type_output_base = "{:.1f} recirculation ACH"
recirc_text_adv = "Recirculation Rate (recirculation ACH): "
recirc_types = [
    {'label': "None", 'value': 0},
    {'label': "Slow", 'value': 0.3},
    {'label': "Moderate", 'value': 1},
    {'label': "Fast", 'value': 10},
    {'label': "Airplane", 'value': 24},
    {'label': "Subway Car", 'value': 54},
]

humidity_text = "Relative Humidity: "
humidity_marks = {
    0: {'label': '0%: Very Dry', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: Airplane', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Dry'},
    0.6: {'label': '60%: Average'},
    0.99: {'label': '99%: Very Humid'},
}

need_more_ctrl_text = '''Need more control over your inputs? Switch to Advanced Mode using the dropdown at the top of 
                         the page.'''

human_header = "Human Behavior"
# Human Behavior
exertion_text = "Exertion Level: "
exertion_types = [
    {'label': "Resting", 'value': 0.49},
    {'label': "Standing", 'value': 0.54},
    {'label': "Light Exercise", 'value': 1.38},
    {'label': "Moderate Exercise", 'value': 2.35},
    {'label': "Heavy Exercise", 'value': 3.30},
]

breathing_text = "Respiratory Activity: "
expiratory_types = [
    {'label': "Breathing (light)", 'value': 1.1},
    {'label': "Breathing (normal)", 'value': 4.2},
    {'label': "Breathing (heavy)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Talking (whisper)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Talking (normal)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Talking (loud)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Singing", 'value': 970},
]

mask_type_text = "Mask Type/Efficiency: "
mask_type_marks = {
    0: {'label': "0% (none, face shield)", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (coarse cotton)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (silk, flannel, chiffon)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (surgical, cotton)", 'style': {'max-width': '50px'}},
    0.95: {'label': "95% (N95 respirator)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "None, Face Shield", 'value': 0},
    {'label': "Coarse Cotton", 'value': 0.1},
    {'label': "Silk, Flannel, Chiffon", 'value': 0.5},
    {'label': "Surgical, Cotton", 'value': 0.9},
    {'label': "N95 Respirator", 'value': 0.95},
]

mask_fit_text = "Mask Fit/Compliance: "
mask_fit_marks = {
    0: {'label': '0%: None', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Poor'},
    0.95: {'label': '95%: Good'}
}

risk_tolerance_text = "Risk Tolerance: "
risk_tol_desc = html.Div('''More vulnerable populations such as the elderly or those with preexisting medical 
conditions require a lower risk tolerance (~0.01). A higher risk tolerance will mean more expected 
transmissions during the expected occupancy period (see FAQ for details).''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})
risk_tol_marks = {
    0.01: {'label': '0.01: Safer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Safe', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Unsafe'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Frequently Asked Questions"
other_io = "Other Inputs & Outputs"

faq_top = html.Div([
    html.H6("Frequently Asked Questions"),
    html.H5("Why isn't 6 feet/2 meter spacing enough?"),
    html.Div([
        html.Div([html.Span('''6 feet/2 meter spacing protects you from large drops ejected by an infected person coughing, 
        as do face masks; however, it doesn’t protect against '''),
                  html.A(children="airborne transmission",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' by infectious aerosols that are 
        suspended in the air and can be mixed throughout a room. Indoors, people are no safer from airborne 
        transmission at 6 feet than 60 feet. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Are there other modes of transmission?"),
    html.Div([
        html.Div([html.A(children="Airborne transmission",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' is thought to be dominant for COVID-19, but other modes are possible, such as `fomite’ 
                  transmission through direct contact with infectious residues on surfaces, `large-droplet' 
                  transmission via coughing or sneezing, and `short-range aerosol' transmission from the respiratory 
                  jet of an infected person over a prolonged period. While the latter two modes may be significant, 
                  they are largely eliminated when face masks or shields are worn; however, the risk of airborne 
                  transmission remains.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Can we really assume a well-mixed room?"),
    html.Div([
        html.Div([html.Span('''There are many contributors to mixing in indoor spaces, including buoyancy-driven 
        flows (from heaters, air conditioners or windows), forced convection from vents and fans, and human motion 
        and respiration. While there are exceptions, as discussed in the '''),
                  html.A(children="paper",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', the assumption of well-mixedness is widely used in the theoretical modeling of 
                  airborne disease transmission.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Does the guideline hold for very large spaces?"),
    html.Div([
        html.Div([html.Span('''In concert halls, stadiums, or other large, ventilated spaces with large numbers of 
        people, the risk of airborne transmission is significant and properly captured by the guideline.  However, 
        when masks or face shields are not worn, there is an additional risk of short-range transmission through 
        respiratory jets, estimated in the '''),
                  html.A(children="paper",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Why does ceiling height matter?"),
    html.Div([
        '''Ceiling height influences the total room volume, which is required for estimating the concentration of 
        infectious aerosols (# of aerosols per unit volume). This concentration is needed to estimate the room’s 
        COVID-19 transmission risk.'''
    ], className='faq-answer'),
    html.Br(),
    html.H5("I know my ACH/MERV numbers. Where can I enter them?"),
    html.Div('''
        If you need more control over your inputs, switch to Advanced Mode using the dropdown at the top of
        the webpage.
    ''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Are there any hidden parameters in Basic Mode?"),
    html.Div([html.Span('''All of the relevant physical parameters are detailed in the '''),
              html.A(children="paper",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. In Basic Mode, the app assumes a default effective aerosol radius of 2 μm (at 60% 
              humidity) and a maximum viral deactivation rate of 0.6 /hr (at ~100% humidity), both of which increase 
              with relative humidity (RH). Estimates for the viral deactivation rate err on the conservative side of 
              slower deactivation.  The viral deactivation rate can be increased by ultraviolet radiation (UV-C) or 
              chemical disinfectants (e.g. hydrogen peroxide, ozone). The app also estimates the key disease 
              parameter, the infectiousness of exhaled air, C'''),
              html.Sub("q"),
              html.Span(''' (infection quanta per unit volume), from the specified 
              respiratory activity, using tabulated values in Figure 2 of the '''),
              html.A(children="paper",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. You define these parameters yourself in Advanced Mode.''')],
             className='faq-answer'),
])

aerosol_radius_text = "Effective Aerosol Radius (at RH = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Maximum Viral Deactivation Rate (at RH = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

values_interest_header = "Calculated Values of Interest: "
values_interest_desc = html.Div([
    html.H5("What exactly is this app calculating?"),
    html.Div([
        html.Div([html.Span('''Given a risk tolerance for airborne transmission, the app calculates the maximum 
        allowable cumulative exposure time, the product of room occupancy and time in the presence of an infected 
        person.  The app also calculates related quantities, defined in the '''),
                  html.A(children="paper",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', that may be of interest:''')]),
    ], className='faq-answer'),
])
outdoor_air_frac_label = html.Span(["Outdoor air fraction Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Aerosol filtration efficiency p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Breathing flow rate Q", html.Sub('b'), ": "])
cq_label = html.Span(["Infectiousness of exhaled air C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Mask passage probability p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Room volume V: "])
vent_rate_Label = html.Span(["Ventilation (outdoor) flow rate Q: "])
recirc_rate_label = html.Span(["Return (recirculation) flow rate Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Air filtration rate (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Humidity-adjusted aerosol radius r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Humidity-adjusted viral deactivation rate \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Effective aerosol settling speed v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Concentration relaxation rate \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Airborne transmission rate \u03B2\u2090: "])

graph_output_header = "Graph Output: "
faq_graphs_text = html.Div([
    html.H5("Graph Output: "),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Does this model account for the prevalence of infection in the local population?"),
    html.Div(['''No. The model calculates the risk of transmission from a single infected person. It thus implicitly 
    assumes that the prevalence of infection in the population is relatively low.  In this limit, the risk of 
    transmission increases with the expected number of infected persons in the room, specifically the product of the 
    occupancy and the prevalence in the population.  The tolerance should be lowered in proportion to this number if 
    it exceeds one.  Conversely, when the expected number of infected persons in the room approaches zero, 
    the tolerance could be proportionally increased until the recommended restrictions are deemed unnecessary. '''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("More Questions?"),
    html.Div([html.Span('''For more detailed explanations and references, see "'''),
              html.A(children="Beyond 6 Feet",
                     href=link_paper,
                     target='_blank'),
              html.Span('''" and other links posted at the top of the webpage.''')]),
])

footer = html.Div([
    html.Div([html.Span('''The COVID-19 Indoor Safety Guideline is an evolving tool intended to familiarize the 
    interested user with the factors influencing the risk of indoor airborne transmission of COVID-19, and to assist 
    in the quantitative assessment of risk in various settings. We note that uncertainty in and intrinsic variability 
    of model parameters may lead to errors as large as an order of magnitude, which may be compensated for by 
    choosing a sufficiently small risk tolerance. Our guideline does not take into account short-range transmission 
    through respiratory jets, which may substantially elevate risk when face masks are not being worn, in a manner 
    discussed in the '''),
              html.A(children="accompanying manuscript",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' (Bazant & Bush, 2020). Use of the COVID-19 Indoor Safety Guideline is the sole 
              responsibility of the user. It is being made available without guarantee or warranty of any kind. The 
              authors do not accept any liability from its use.''')]),
    html.Br(),
    html.Div("Special thanks to: ")
], className='footer-small-text')
