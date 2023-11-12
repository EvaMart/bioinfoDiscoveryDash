import dash_mantine_components as dmc

from charts.utils import connectMongo

collection, logCollection = connectMongo()

totalRepos = logCollection.count_documents({})

# docs with repository.response == 200
reposAccessed = logCollection.count_documents({
    'repository.response': 200
})

# docs with readme.response == 200

readmesAccessed = logCollection.count_documents({
    'readme.response': 200
})


bioinformaticsRepos = collection.count_documents({
    'prediction': 'bioinformatics'
})

nonBioinformaticsRepos = collection.count_documents({
    'prediction': 'non-bioinformatics'
})


def card(title, number):
    card = dmc.Card(
        children=[
            dmc.Text(title, size="sm"),
            dmc.Space(h=10),
            dmc.Text(number, weight=500, size="xl"),
        ],
        
        shadow=False,
        withBorder = True,
    )
    return card



cards = dmc.SimpleGrid(
    cols=5,
    children=[
        card('Repos searched', totalRepos),
        card('Repos accessed', reposAccessed),
        card('Readmes', readmesAccessed),
        card('Bioinformatics readmes', bioinformaticsRepos),
        card('Non-bioinformatics readmes', nonBioinformaticsRepos)
    ]
)