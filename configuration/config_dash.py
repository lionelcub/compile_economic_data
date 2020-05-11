

import holoviews as hv
import panel as pn
from datetime import datetime
from bokeh.models import HoverTool

# Personal module. 
from configuration.config import ecoGroup


# ----------------------------------------------------------------------
# Style Customisation. 
# ---------------------------------------------------------------------- 

height, width = (300,550)
xlim = (datetime(1980,1,1), datetime(datetime.today().year, 12, 1))


# ----------------------------------------------------------------------
# Financial trouble / recession / crisis. 
# ---------------------------------------------------------------------- 

debtCrisis_2008 = hv.VSpan(datetime(2007,12,1), datetime(2009,6,1)).opts(line_width=1, color='lightgray')
dotCom_2001 = hv.VSpan(datetime(2001,3,1), datetime(2001,11,1)).opts(line_width=1, color='lightgray')
trouble_1990 = hv.VSpan(datetime(1990,7,1), datetime(1991,3,1)).opts(line_width=1, color='lightgray')
trouble_1982 = hv.VSpan(datetime(1981,11,1), datetime(1982,7,1)).opts(line_width=1, color='lightgray')
trouble_1980 = hv.VSpan(datetime(1980,1,1), datetime(1980,7,1)).opts(line_width=1, color='lightgray')
trouble_1974 = hv.VSpan(datetime(1973,11,1), datetime(1975,3,1)).opts(line_width=1, color='lightgray')
trouble_1970 = hv.VSpan(datetime(1969,12,1), datetime(1970,11,1)).opts(line_width=1, color='lightgray')
trouble_1960 = hv.VSpan(datetime(1960,4,1), datetime(1961,2,1)).opts(line_width=1, color='lightgray')
trouble_1957 = hv.VSpan(datetime(1957,8,1), datetime(1958,4,1)).opts(line_width=1, color='lightgray')
trouble_1953 = hv.VSpan(datetime(1953,7,1), datetime(1954,5,1)).opts(line_width=1, color='lightgray')
trouble_1949 = hv.VSpan(datetime(1948,11,1), datetime(1949,10,1)).opts(line_width=1, color='lightgray')

# Combine the span. 
vSpan_ecoRecess = debtCrisis_2008 * dotCom_2001 * trouble_1990 * trouble_1982 * trouble_1980


# ----------------------------------------------------------------------
# Elements. 
# ---------------------------------------------------------------------- 

# Hover.
hover = HoverTool(
    tooltips=[('date','@date{%F}'),('value','@{value}{0.2f}')],
    formatters={'@date': 'datetime'}, mode='vline'
)
tools = [hover, 'crosshair']


# ----------------------------------------------------------------------
# Widgets.
# ---------------------------------------------------------------------- 

# Eco options. 
selectEcoOption = pn.widgets.Select(name='Eco Option', options=list(ecoGroup.keys()), 
                                    value='employment', height=50)
widgetsEcoOption = pn.WidgetBox(selectEcoOption, height=70, width=130, sizing_mode='stretch_width')

# This is for selecting economic data to plot. 
# There are six slots available for plotting. 
selector1 = None
selector2 = None
selector3 = None
selector4 = None
selector5 = None
selector6 = None

selectors = [selector1, selector2, selector3, selector4, selector5, selector6]

# This is for displaying the recession period. 
toggler1 = None
toggler2 = None
toggler3 = None
toggler4 = None
toggler5 = None
toggler6 = None

togglers = [toggler1, toggler2, toggler3, toggler4, toggler5, toggler6]