"""Script to deliver insights to the user"""
import sys
import matplotlib.pyplot as plt
import wordcloud

sys.path.insert(0, "..")
from process_data import ProcessData

process_data_object = ProcessData()


class PlotInsights:
    def plot_average_spending_category(self):
        """Plot average spending category"""
        avg_spending_category = process_data_object.average_spending_category()
        fig, ax = plt.subplots()
        avg_spending_category.plot(kind="bar", ax=ax, figsize=(17, 6))
        ax.set_xlabel("Amount($)", size=20)
        ax.set_ylabel("Category", size=20)
        plt.show()

    def plot_monthly_expenses(self):
        """Plot monthly expenses"""
        monthly_expenses = process_data_object.monthly_expenses()
        fig, ax = plt.subplots()
        monthly_expenses.plot(
            x="year_month", y="sum", kind="bar", ax=ax, figsize=(17, 6)
        )
        ax.set_xlabel("Amount($)", size=20)
        ax.set_ylabel("Category", size=20)
        plt.show()

    def plot_payment_channels_used(self):
        """Plot payment channels used"""
        payment_channels = process_data_object.payment_channels_used()
        payment_channels.plot(kind="bar")
        plt.show()

    def plot_transaction_type_used(self):
        """Plot transaction type used"""
        transaction_type_used = process_data_object.transaction_type_used()
        transaction_type_used.plot(kind="bar")
        plt.show()

    def plot_merchant_names_dealt_with(self):
        """Plot merchant names dealt with"""
        merchant_names_dealt_with = process_data_object.merchant_names_dealt_with()
        merchant_names_dealt_with.plot(kind="bar")
        plt.show()

    def generate_wordcloud(self):
        """Plot word cloud based on merchant names"""
        text = process_data_object.return_text_for_wordcloud()
        wordcloud2 = wordcloud.WordCloud().generate(text)
        # Generate plot
        plt.imshow(wordcloud2)
        plt.axis("off")
        plt.show()
