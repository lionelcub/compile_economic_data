

from datetime import datetime


# -------------------------------------------------------
# API Parameters Reference. 
# -------------------------------------------------------

# Default = lin

# - lin = Levels (No transformation)
# - chg = Change
# - ch1 = Change from Year Ago
# - pch = Percent Change
# - pc1 = Percent Change from Year Ago
# - pca = Compounded Annual Rate of Change
# - cch = Continuously Compounded Rate of Change
# - cca = Continuously Compounded Annual Rate of Change
# - log = Natural Log

units_options = ['lin', 'chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log']

# Default = None

# - d = Daily
# - w = Weekly
# - bw = Biweekly
# - m = Monthly
# - q = Quarterly
# - sa = Semiannual
# - a = Annual

# - wef = Weekly, Ending Friday
# - weth = Weekly, Ending Thursday
# - wew = Weekly, Ending Wednesday
# - wetu = Weekly, Ending Tuesday
# - wem = Weekly, Ending Monday
# - wesu = Weekly, Ending Sunday
# - wesa = Weekly, Ending Saturday
# - bwew = Biweekly, Ending Wednesday
# - bwem = Biweekly, Ending Monday

freq_options = [
    'd', 'w', 'bw', 'm', 'q', 'sa', 'a', 
    'wef', 'weth', 'wew', 'wetu', 'wem', 
    'wesu', 'wesa', 'bwew', 'bwem'
]

# Default = avg

# - avg = Average
# - sum = Sum
# - eop = End of Period

aggregation_method = ['avg', 'sum', 'eop']


# -------------------------------------------------------
# FRED Data.
# -------------------------------------------------------

FRED_collection = {
    # Employment.
    'unemploy': {
        'series_id': 'UNRATE',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },
    'unemployNat': {
        'series_id': 'NROU',
        'units': 'lin',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },
    'participation': {
        'series_id': 'CIVPART',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },
    'popGrowth_YoY': {
        'series_id': 'POPTHM', 
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },
    
    # Household.
    'pDispIncome_YoY': {
        'series_id': 'DSPIC96', 
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },
    'pConsumeExp_YoY': {
        'series_id': 'PCE', 
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },
    'pConsumeExpReal_YoY': {
        'series_id': 'PCEC96', 
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },
    'pSaveRatio': {
        'series_id': 'PSAVERT', 
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },
    'houseDebt': {
        'series_id': 'TDSP', 
        'units': 'lin',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },
    'mortgageDebt': {
        'series_id': 'MDSP', 
        'units': 'lin',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },
    'consumeDebt': {
        'series_id': 'CDSP', 
        'units': 'lin',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },
    
    # Industrial & business. 
    'indusProduce': {
        'series_id': 'INDPRO', 
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    }, 
    'capacUtilise': {
        'series_id': 'TCU', 
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    }, 
    'manufactProduce': {
        'series_id': 'IPMAN',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'manufactNewOrderExDef': {
        'series_id': 'NEWORDER',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'manufactNewOrderExTrans': {
        'series_id': 'ADXTNO',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    }, 
    'onlineSales_YoY': {
        'series_id': 'ECOMSA',
        'units': 'pc1',
        'frequency': 'q',
        'aggregation_method': 'avg'
    }, 
    'onlineSalesRatio': {
        'series_id': 'ECOMPCTSA',
        'units': 'lin',
        'frequency': 'q',
        'aggregation_method': 'avg'
    }, 
    'retailSales_YoY': {
        'series_id': 'MRTSSM44X72USS',
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    }, 
    'retailSalesAdv_YoY': {
        'series_id': 'RSAFS',
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    }, 
    'vehicleSales_YoY': {
        'series_id': 'TOTALSA',
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    }, 
    'businessInventory_YoY': {
        'series_id': 'BUSINV',
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    }, 
    'businessInventorySalesRatio': {
        'series_id': 'ISRATIO',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    }, 
    'manufactInventorySalesRatio': {
        'series_id': 'MNFCTRIRSA',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    }, 
    'retailInventorySalesRatio': {
        'series_id': 'RETAILIRSA',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    }, 
    'houseStarts': {
        'series_id': 'HOUST',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    }, 
    'houseStarts_YoY': {
        'series_id': 'HOUST',
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },    
    'newHomeSales': {
        'series_id': 'HSN1F',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'newHomeSales_YoY': {
        'series_id': 'HSN1F',
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'existHomeSales': {
        'series_id': 'EXHOSLUSM495S',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'houseInventoryEst': {
        'series_id': 'EVACANTUSQ176N',
        'units': 'lin',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },  
    
    # Monetary policy.
    # Depreciated. 
    'govFiscalBudget': { 
        'series_id': 'M318501Q027NBEA',
        'units': 'lin',
        'frequency': 'a',
        'aggregation_method': 'avg'
    },  
    'usGDP_YoY': {
        'series_id': 'GDP',
        'units': 'pc1',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },  
    'usGDPReal_YoY': {
        'series_id': 'GDPC1',
        'units': 'pc1',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },  
    'govBudgetGDP': {
        'series_id': 'FYFSGDA188S',
        'units': 'lin',
        'frequency': 'a',
        'aggregation_method': 'avg'
    },  
    
    # Monetary policy.
    'fedFFR': {
        'series_id': 'FEDFUNDS',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'mortgageRate30Yr': {
        'series_id': 'MORTGAGE30US',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'mortgageRate15Yr': {
        'series_id': 'MORTGAGE15US',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'primeLoanRate': {
        'series_id': 'DPRIME',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'libor3mth': {
        'series_id': 'USD3MTD156N',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'excessReserveDepo': {
        'series_id': 'EXCSRESNW',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'liqM1_YoY': {
        'series_id': 'M1',
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'veloM1': {
        'series_id': 'M1V',
        'units': 'lin',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },  
    'liqM2_YoY': {
        'series_id': 'M2',
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'veloM2': {
        'series_id': 'M2V',
        'units': 'lin',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },  
    
    # Trade. 
    'tradeBalance': {
        'series_id': 'BOPGSTB',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'tradeIndexUSD': {
        'series_id': 'DTWEXEMEGS',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'forexUS_CHINA': {
        'series_id': 'DEXCHUS',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    
    # Price.
    'usGDP_deflator_YoY': {
        'series_id': 'GDPDEF',
        'units': 'pc1',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },  
    'pConsume_deflator_YoY': {
        'series_id': 'DPCERD3Q086SBEA',
        'units': 'pc1',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },  
    'producerPPI': {
        'series_id': 'PPIACO',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'producerPPI_YoY': {
        'series_id': 'PPIACO',
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'caseShillerHPI': {
        'series_id': 'CSUSHPINSA',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'caseShillerHPI_YoY': {
        'series_id': 'CSUSHPINSA',
        'units': 'pc1',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'nonFarm_unitLabour': {
        'series_id': 'ULCNFB',
        'units': 'lin',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },  
    'nonFarm_unitLabour_YoY': {
        'series_id': 'ULCNFB',
        'units': 'pc1',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },  
    'yield10Yr_minusFFR': {
        'series_id': 'T10YFF',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    'yield10Yr_minus2Yr': {
        'series_id': 'T10Y2Y',
        'units': 'lin',
        'frequency': 'm',
        'aggregation_method': 'avg'
    },  
    
    # Debt.
    'govDebt_GDP_ratio': {
        'series_id': 'GFDEGDQ188S',
        'units': 'lin',
        'frequency': 'q',
        'aggregation_method': 'avg'
    },  
    'houseDebt_GDP_ratio': {
        'series_id': 'HDTGPDUSQ163N',
        'units': 'lin',
        'frequency': 'q',
        'aggregation_method': 'avg'
    }, 
} 


# -------------------------------------------------------
# Data grouping. 
# -------------------------------------------------------

# Economic data grouping. 
ecoGroup = {
    'employment': [
        'unemploy', 'unemployNat', 'participation', 'popGrowth_YoY'
    ],
    'household': [
        'pDispIncome_YoY', 'pConsumeExp_YoY', 'pConsumeExpReal_YoY', 'pSaveRatio', 
        'mortgageDebt', 'consumeDebt'
    ],
    'manufactBusiness': [
        'indusProduce', 'capacUtilise', 'manufactProduce', 'manufactNewOrderExDef', 
        'manufactNewOrderExTrans', 'onlineSales_YoY', 'onlineSalesRatio', 'retailSales_YoY', 
        'retailSalesAdv_YoY', 'vehicleSales_YoY', 'businessInventory_YoY', 
        'businessInventorySalesRatio', 'manufactInventorySalesRatio', 'retailInventorySalesRatio'
    ],
    'housing': [
        'houseStarts', 'houseStarts_YoY', 'newHomeSales', 'newHomeSales_YoY', 'existHomeSales', 
        'houseInventoryEst'
    ],
    'govFiscal': [
        'govFiscalBudget', 'usGDP_YoY', 'usGDPReal_YoY', 'govBudgetGDP'
    ],
    'fedMonetary': [
        'fedFFR', 'mortgageRate30Yr', 'mortgageRate15Yr', 'primeLoanRate', 'libor3mth', 
        'excessReserveDepo', 'liqM1_YoY', 'veloM1', 'liqM2_YoY', 'veloM2'
    ],
    'forexTrade': [
        'tradeBalance', 'tradeIndexUSD', 'forexUS_CHINA'
    ],
    'price': [
        'usGDP_deflator_YoY', 'pConsume_deflator_YoY', 'producerPPI', 'producerPPI_YoY', 
        'caseShillerHPI', 'caseShillerHPI_YoY', 'nonFarm_unitLabour', 'nonFarm_unitLabour_YoY'
    ],
    'debt': [
        'houseDebt', 'govDebt_GDP_ratio', 'houseDebt_GDP_ratio'
    ],
    'bondYield': [
        'yield10Yr_minusFFR', 'yield10Yr_minus2Yr'
    ],
}


# -------------------------------------------------------
# FRED API Endpoint. 
# -------------------------------------------------------

# API endpoints. 
url = 'https://api.stlouisfed.org/fred/series/observations'
params = {
    'series_id': 'UNRATE',
    'file_type': 'json',
    'limit': 100000,
    'observation_start': datetime(1950,1,1).strftime('%Y-%m-%d'),
    'observation_end': datetime(2020,12,1).strftime('%Y-%m-%d'),
    'units': 'lin',
    'frequency': 'm',
    'aggregation_method': 'avg',
    'api_key': '2da1858756aeff8b7837b7477b550f07'
}

# To store all the dataframes. 
FRED_data = {}


# -------------------------------------------------------
# API Request Tracking. 
# -------------------------------------------------------

# To track the failed API requests.
request_failed = {} 
sleep_time = 1