import pandas as pd

cols = [
    'title',
    'developer',
    'released',
    'scoreText',
    'ratings',
    'reviews',
    'priceText',
    'version',
    'developerId',
    'developerEmail',
    'developerWebsite',
    'developerAddress',
    'genre',
    'installs',
    'minInstalls',
    'maxInstalls',
    'size',
    'androidVersionText',
    'contentRating',
    'privacyPolicy',
    'adSupported',
    'editorsChoice',
    'appId',
    'url'
]


def convertToCsv(file):
    df = pd.read_json(f"./{file}.json")
    df = pd.DataFrame(df, columns=cols)
    # df.drop(list_to_ignore, axis=1, inplace=True)
    # df.sort_values('score', ascending=False, inplace=True)
    df.drop_duplicates(subset="appId", inplace=True)

    df.to_csv(f'{file}.csv', index=False)


convertToCsv("pG_50")
