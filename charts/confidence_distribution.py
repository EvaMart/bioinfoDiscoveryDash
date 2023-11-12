import plotly.figure_factory as ff
import numpy as np
import pandas as pd

from charts.utils import connectMongo

collection, logCollection = connectMongo()

cursorBioinformatics = collection.find({
    'prediction': 'bioinformatics'
})
dfBioinformatics = pd.DataFrame(list(cursorBioinformatics))

cursorNonBioinformatics = collection.find({
    'prediction': 'non-bioinformatics'
})
dfNonBioinformatics = pd.DataFrame(list(cursorNonBioinformatics))


# Group data together
hist_data = [dfBioinformatics['confidence'], dfNonBioinformatics['confidence']]

group_labels = ['Bioinformatics', 'Non-bioinformatics']

# Create distplot with custom bin_size
confidence_distribution = ff.create_distplot(hist_data, group_labels, bin_size=.2, colors=["#EA738D","#89ABE3"])

confidence_distribution.update_layout(
    # plotly light template
    template="plotly_white",
    xaxis_title="Confidence",
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
        y=-0.4)
        
)