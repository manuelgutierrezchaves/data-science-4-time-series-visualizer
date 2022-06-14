import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=["date"])

# Clean data
df = df.loc[(df["value"] > df["value"].quantile(0.025)) & (df["value"] < df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32,10))
    ax.plot(df)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month])["value"].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot.bar(legend = True, ylabel = "Average Page Views", xlabel = "Years").figure
    plt.legend(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_figheight(10)
    fig.set_figwidth(28)

    sns.boxplot(x="year", y="value", data=df_box, ax = ax1)
    sns.boxplot(x="month", y="value", data=df_box, ax = ax2, order = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"])
    # ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_ylim(0, 200000)
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_ylim(0, 200000)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_line_plot()
draw_bar_plot()
draw_box_plot()