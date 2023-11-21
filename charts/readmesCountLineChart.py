import plotly.graph_objects as go
import pandas as pd

from random import randint
from charts.utils import connectMongo

# Obtaining data
# mongo aggregation query
collection, logCollection = connectMongo()

# aggregate by date and count 

bioinformaticsP = [
    {
        '$match': {
            'prediction': 'bioinformatics'
        }
    },
    {
        '$group': {
            '_id': {
                'date': '$date'
            }, 
            'count': {
                '$sum': 1
            },
            'date' : {
                '$first': '$date'
            }
        }
    }, {
        '$sort': {
            '_id.date': 1
        }
    }
]


cursorBioinformatics = collection.aggregate(bioinformaticsP)

# convert cursor to pandas dataframe
dfBioinformatics = pd.DataFrame(list(cursorBioinformatics))

# bioinformatics readmes with confidence bigger than 0.9
bioinformaticsP_90 = [
    {
        '$match': {
            'prediction': 'bioinformatics', 
            'confidence': {
                '$gte': 0.5
            }
        }
    }, {
        '$group': {
            '_id': {
                'date': '$date'
            }, 
            'count': {
                '$sum': 1
            },
            'date' : {
                '$first': '$date'
            }
        }
    }, {
        '$sort': {
            '_id.date': 1
        }
    }
]

cursorBioinformatics_90 = collection.aggregate(bioinformaticsP_90)
dfBioinformatics_90 = pd.DataFrame(list(cursorBioinformatics_90))



# aggregate by date and count
nonBioinformaticsP = [
    {
        '$match': {
            'prediction': 'non-bioinformatics'
        }
    },
    {
        '$group': {
            '_id': {
                'date': '$date'
            }, 
            'count': {
                '$sum': 1
            },
            'date' : {
                '$first': '$date'
            }
        }
    }, {
        '$sort': {
            '_id.date': 1
        }
    }
]

cursorNonBioinformatics = collection.aggregate(nonBioinformaticsP)
dfNonBioinformatics = pd.DataFrame(list(cursorNonBioinformatics))

# convert date to datetime


dfBioinformatics['date'] = pd.to_datetime(dfBioinformatics['date'])
# remove hour and minutes
dfBioinformatics['date'] = dfBioinformatics['date'].dt.date
dffBioinformatics = dfBioinformatics.groupby(["date"])['count'].sum().reset_index()

dfNonBioinformatics['date'] = pd.to_datetime(dfNonBioinformatics['date'])
# remove hour and minutes
dfNonBioinformatics['date'] = dfNonBioinformatics['date'].dt.date
dffNonBioinformatics = dfNonBioinformatics.groupby(["date"])['count'].sum().reset_index()



if len(dfBioinformatics_90) > 0:
    dfBioinformatics_90['date'] = pd.to_datetime(dfBioinformatics_90['date'])
    # remove hour and minutes
    dfBioinformatics_90['date'] = dfBioinformatics_90['date'].dt.date
    dffBioinformatics_90 = dfBioinformatics_90.groupby(["date"])['count'].sum().reset_index()
else:
    # in order to have this trace visible (although at zero),
    #  generate zero counts for dates in dfNonBioinformatics
    dfBioinformatics_90['date'] = dfNonBioinformatics['date']
    dfBioinformatics_90['prediction'] = [0 for i in range(len(dfNonBioinformatics))]
    dffBioinformatics_90 = dfBioinformatics_90

readmes_count_line_chart = go.Figure(data=go.Scatter(x=dffBioinformatics['date'], y=dffBioinformatics['count'], name="Bioinformatics", line=dict(color="#EFACBA", width=1.5)))
readmes_count_line_chart.add_trace(go.Scatter(x=dffBioinformatics_90['date'], y=dffBioinformatics_90['prediction'], name="Bioinformatics (conf>0.9)", line=dict(color="#EA526E", width=1.5)))
readmes_count_line_chart.add_trace(go.Scatter(x=dffNonBioinformatics['date'], y=dffNonBioinformatics['count'], name="Non-bioinformatics", line=dict(color="#89ABE3", width=1.5)))

readmes_count_line_chart.update_layout(
    # plotly light template
    template="plotly_white",
    xaxis_title="Date",
    yaxis_title="Count",
    height=400,
    autosize= True,
    margin=dict(
        t=20,
        pad=0
    ),
    font=dict(
        family="Inter",
        size=12,
        color="black"
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.5)
        
)

