import os

import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

RAW_FILE_PATH = os.getenv("RAW_FILE_PATH")
PROCESSED_FILE_PATH = os.getenv("PROCESSED_FILE_PATH")

dataset = pd.read_csv(RAW_FILE_PATH, index_col=0)


columns_Y = os.getenv("TARGET_COLUMN")
y_columns = columns_Y
datetime_col = "datetime"


def process_data(dataset, **kwargs):


    d = pd.to_datetime(dataset[datetime_col], format="mixed", utc=True)
    columns_X = dataset.columns[~dataset.columns.isin(columns_Y)]







    dataset["hour"] = [f.hour for f in d]
    dataset["day"] = [f.day for f in d]
    dataset["month"] = [f.month for f in d]
    dataset["year"] = [f.year for f in d]
    dataset["day_of_year"] = [f.timetuple().tm_yday for f in d]
    dataset["day_of_week"] = [f.timetuple().tm_wday for f in d]
    dataset["week_of_year"] = [f.weekofyear for f in d]



    time_cols = ["hour", "day", "month", "year", "day_of_year", "day_of_week", "week_of_year"]
    # Make the y the 1st column
    dataset = dataset[y_columns+[col for col in dataset.columns if col not in y_columns]]

    # make the time columns the last
    dataset = dataset[[col for col in dataset.columns if col not in time_cols]+time_cols]


    df = dataset.copy()
    df.drop("datetime", axis=1, inplace=True)
    # Sort DataFrame by DateTime index
    df.sort_index(inplace=True)

    # Perform imputation
    imputer = IterativeImputer(max_iter=10, random_state=0)
    df_imputed = imputer.fit_transform(df)

    # Convert the result back to a DataFrame
    df_imputed = pd.DataFrame(df_imputed, columns=df.columns, index=df.index)
    df_imputed["datetime"] = dataset["datetime"]

    df_imputed.to_csv(PROCESSED_FILE_PATH)

    # Contruct the method to process the data

    # Save final processed file to PROCESSED_FILE_PATH
    return df_imputed