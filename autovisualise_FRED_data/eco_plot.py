

# For data preprocessing. 
import pickle, pandas as pd

# For visualisation. 
import panel as pn
import holoviews as hv
import hvplot.pandas

hv.extension("bokeh", "matplotlib") 
pn.extension()

# Personal modules.
from configuration.config import * 
from configuration.config_dash import * 


# ----------------------------------------------------------------------
# Read file.
# ---------------------------------------------------------------------- 

try: 
    with open('dataset/storage/FRED_data.pickle', 'rb') as in_file:
        FRED_data = pickle.load(in_file)
except: 
    Exception("ERROR: 'dataset/storage/FRED_data.pickle' doesn't exist.") 


# ----------------------------------------------------------------------
# Function Wrapper. 
# ---------------------------------------------------------------------- 

# To perform combination for certain economic data plots. 
def deco_combinePlots(plotFunc):
    def wrapper(data, recession):
        
        # Try creating a plot to see if the data exist. 
        try:
            plot_main = plotFunc(data[0], recession)
            plot_add = None
            if recession:
                plot_main = plot_main * vSpan_ecoRecess 
        except: 
            return pn.pane.Pane('')
        
        # If more than one eco data is selected, creating additional plot. 
        if len(data) > 1: 
            plot_add = FRED_data[data[1]].hvplot(kind='line', y='value', label=data[1], 
                                                 width=width, xlim=xlim, shared_axes=False)
        # Return the plot. 
        if plot_add:
            return pn.Column((plot_main * plot_add).opts(legend_position='top'), tools=tools)
        else:
            return pn.Column(plot_main) 
        
    return wrapper


# ----------------------------------------------------------------------
# Plot.
# ---------------------------------------------------------------------- 

# Update Eco widgets based on the Eco option. 
@pn.depends(selectEcoOption.param.value)
def plotEcoData(ecoData):
    
    # ----------------------------------------
    # Create multiple selector widgets. 
    # ----------------------------------------
    
    for idx, selector in enumerate(selectors):
        if idx > len(ecoGroup[ecoData]) - 1:
            togglers[idx] = pn.widgets.Toggle(name="Display Recession", button_type='default', 
                                              value=False, margin=(0,10,0,10), sizing_mode='stretch_width')            
            selectors[idx] = pn.widgets.MultiChoice(name=f'EcoData {idx + 1}', value=[],
                                                    options=[], height=75, margin=(15,25,0,10), 
                                                    max_items=2, sizing_mode='stretch_width')
        else:
            togglers[idx] = pn.widgets.Toggle(name="Display Recession", button_type='default', 
                                              value=False, margin=(0,10,0,10), sizing_mode='stretch_width')
            selectors[idx] = pn.widgets.MultiChoice(name=f'EcoData {idx + 1}', 
                                                    value=[ecoGroup[ecoData][idx]],
                                                    options=ecoGroup[ecoData], height=75, 
                                                    margin=(15,25,0,10), max_items=2, 
                                                    sizing_mode='stretch_width')

    # ----------------------------------------
    # First row.
    # ----------------------------------------
    
    @pn.depends(selectors[0].param.value, togglers[0].param.value)
    @deco_combinePlots
    def plotEcoData1(data, recession):
        return FRED_data[data].hvplot(kind='line', y='value', label=data, width=width, 
                                      xlim=xlim, shared_axes=False, tools=tools)
    
    @pn.depends(selectors[1].param.value, togglers[1].param.value)
    @deco_combinePlots
    def plotEcoData2(data, recession):
        return FRED_data[data].hvplot(kind='line', y='value', label=data, width=width, 
                                      xlim=xlim, shared_axes=False, tools=tools)
    
    # ----------------------------------------
    # Second row.
    # ----------------------------------------
    
    @pn.depends(selectors[2].param.value, togglers[2].param.value)
    @deco_combinePlots
    def plotEcoData3(data, recession):
            return FRED_data[data].hvplot(kind='line', y='value', label=data, width=width, 
                                          xlim=xlim, shared_axes=False, tools=tools)
    
    @pn.depends(selectors[3].param.value, togglers[3].param.value)
    @deco_combinePlots
    def plotEcoData4(data, recession):
            return  FRED_data[data].hvplot(kind='line', y='value', label=data, width=width, 
                                           xlim=xlim, shared_axes=False, tools=tools)
    
    # ----------------------------------------
    # Third row.
    # ----------------------------------------
    
    @pn.depends(selectors[4].param.value, togglers[4].param.value)
    @deco_combinePlots
    def plotEcoData5(data, recession):
            return  FRED_data[data].hvplot(kind='line', y='value', label=data, width=width, 
                                           xlim=xlim, shared_axes=False, tools=tools)
    
    @pn.depends(selectors[5].param.value, togglers[5].param.value)
    @deco_combinePlots
    def plotEcoData6(data, recession):
            return  FRED_data[data].hvplot(kind='line', y='value', label=data, width=width, 
                                           xlim=xlim, shared_axes=False, tools=tools)
        
    # ----------------------------------------
    # Create the plots.
    # ----------------------------------------
        
    plot1 = pn.Column(plotEcoData1)
    plot2 = pn.Column(plotEcoData2)
    plot3 = pn.Column(plotEcoData3)
    plot4 = pn.Column(plotEcoData4)
    plot5 = pn.Column(plotEcoData5)
    plot6 = pn.Column(plotEcoData6)
    
    plotEcoRow1 = pn.Row(plot1, plot2)
    plotEcoRow2 = pn.Row(plot3, plot4)
    plotEcoRow3 = pn.Row(plot5, plot6)
    
    # ----------------------------------------
    # Compile into a dashboard. 
    # ----------------------------------------
    
    widgets = pn.Column(selectors[0], togglers[0], selectors[1], togglers[1], selectors[2], togglers[2], 
                        selectors[3], togglers[3], selectors[4], togglers[4], selectors[5], togglers[5], 
                        margin=(0,20,0,0), width=400)
    dash = pn.Column(plotEcoRow1, plotEcoRow2, plotEcoRow3)
    return pn.Row(widgets, dash)