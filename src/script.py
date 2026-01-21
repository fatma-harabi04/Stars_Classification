from pathlib import Path
import pandas as pd

def wrangle_data(data):
    base_path = Path.cwd().parent
    data_path = base_path / "data" / "raw" / "star_classification.csv"

    df = pd.read_csv(data_path)

    df["u_g"] = df["u"] - df["g"]
    df["g_r"] = df["g"] - df["r"]
    df["r_i"] = df["r"] - df["i"]
    df["i_z"] = df["i"] - df["z"]

    df.drop(
        columns=[
            "obj_ID",
            "alpha",
            "delta",
            "run_ID",
            "rerun_ID",
            "cam_col",
            "field_ID",
            "spec_obj_ID",
            "redshift",
            "plate",
            "MJD",
            "fiber_ID",
        ],
        inplace=True,
    )

    mapp = {"GALAXY": 0, "QSO": 1, "STAR": 2}
    df["class"] = df["class"].map(mapp)

    return df
def split_features_target(data):
    X = data.drop("class", axis=1)
    y = data["class"]
    return X, y


def get_data_splits(data, test_size=0.2, random_state=42):
    from sklearn.model_selection import train_test_split

    X, y = split_features_target(data)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

    return X_train, X_test, y_train, y_test


def load_model(model_path):
    import joblib

    model = joblib.load(model_path)
    return model


def predict(model, X):
    return model.predict(X)

