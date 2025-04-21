

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    # marimo

    import marimo as mo
    import pandas as pd

    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    return mo, pd


@app.cell
def _(mo):
    mo.md(
        r"""
        # Analyze Stackoverflow survey data focusing on locations
        using the /users endpoint
        """
    )
    return


@app.cell
def _(pd):
    data = pd.read_csv("data/survey_results_public.csv")
    data.head()
    return (data,)


@app.cell
def _(data):
    data.columns.to_list()
    return


@app.cell
def _(data):
    # select relevant columns for the analysis
    cols = [
        "Country",
        "LanguageHaveWorkedWith",
        "LanguageWantToWorkWith",
        "YearsCodePro",
        "DevType",
        "Employment"
    ]

    devs_df = data[cols].copy()

    #drop rows with missing country or main language info
    devs_df.dropna(subset=["Country", "LanguageHaveWorkedWith"], inplace=True)

    devs_df.head()
    return (devs_df,)


@app.cell
def _(devs_df):
    devs_df.YearsCodePro.unique()
    return


@app.cell
def _(X, devs_df):
    # clean and convert years of experience
    def clean_experience(x):
        if x == "Less than 1 year":
            return 0.5
        elif x == "More than 50 years":
            return 51
        try:
            return float(X)
        except:
            return None

    devs_df["YearsCodePro"] = devs_df["YearsCodePro"].apply(clean_experience)

    #drop rows where experience could not be converted
    devs_df.dropna(subset=["YearsCodePro"], inplace=True)

    devs_df["YearsCodePro"].describe()
    return


@app.cell
def _(devs_df, mo):
    # Create a sorted list of unique countries
    country_list = sorted(devs_df["Country"].unique())

    # Dropdown menu for selecting a country
    country_filter = mo.ui.dropdown(
        options=country_list,
        label="Select Country",
        value="Kenya" if "Kenya" in country_list else country_list[0]
    )

    # Show the widget
    country_filter

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
