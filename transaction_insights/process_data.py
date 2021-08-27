"""Script to process raw data with support functions for other scripts"""
import pandas as pd
import requests


def _get_data():
    # we are getting json data already from the url but in production, we'll have a separate method to get this data
    response = requests.get("url")
    data = pd.DataFrame(response)
    data.to_csv("sample_transactions.csv", index=False)


class ProcessData:
    _get_data()
    df = pd.read_csv("sample_transactions.csv")
    # process data, only keep valuable columns
    df = df[
        [
            "payment_channel",
            "name",
            "amount",
            "transaction_type",
            "merchant_name",
            "date",
            "category",
        ]
    ]
    # convert date to datetime
    df["date"] = pd.to_datetime(df["date"])
    # create additional column for year_month
    df["year_month"] = df["date"].dt.to_period("M")

    def average_spending_category(self):
        """Average spending per category"""
        avg_spending_category = self.df.groupby("category")["amount"].mean()
        return avg_spending_category

    def monthly_expenses(self):
        """Monthly expenses in total"""
        monthly_expenses = (
            self.df.groupby("year_month")["amount"].sum().reset_index(name="sum")
        )
        return monthly_expenses

    def monthly_expenses_per_category(self):
        """Monthly expenses per category"""
        expenses_per_category = pd.pivot_table(
            self.df, values=["amount"], index=["category", "year_month"], aggfunc=sum
        ).reset_index()
        return expenses_per_category

    def payment_channels_used(self):
        """Count of payment channels used"""
        return self.df["payment_channel"].value_counts()

    def transaction_type_used(self):
        """Count of transaction type used"""
        return self.df["transaction_type"].value_counts()

    def merchant_names_dealt_with(self):
        """Count of merchant names dealt with"""
        return self.df["merchant_name"].value_counts()

    def return_text_for_wordcloud(self):
        """Process text for the wordcloud"""
        text = " ".join(self.df["name"])
        return text
