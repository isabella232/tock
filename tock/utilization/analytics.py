
from django.apps import apps
from django.db.models import F, Sum

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot

def utilization_plot(data_frame):
    """Make a stacked area plot of billable and nonbillable hours.

    data_frame has start_date, billable, and non_billable columns
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data_frame["start_date"],
        y=data_frame["billable"],
        line_shape="hv",
        stackgroup="only",
        name="Billable",
        )
    )
    fig.add_trace(go.Scatter(
        x=data_frame["start_date"],
        y=data_frame["non_billable"],
        line_shape="hv",
        stackgroup="only",
        name="Non-Billable",
        )
    )

    fig.update_layout(
        # autosize=False,
        # width=900,
        # height=500,
        xaxis=dict(autorange=True),
        yaxis=dict(autorange=True),
        xaxis_title="Reporting Period Start Date",
        yaxis_title="Hours",
        title="Total Hours recorded vs. Time",
        hovermode="x",
    )

    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def utilization_data(start_date, end_date):
    """Get a data frame of utilization data.

    Has start_date, billable, and nonbillable columns.
    """
    Timecard = apps.get_model("hours", "Timecard")
    data = (Timecard.objects.filter(reporting_period__start_date__gte=start_date,
                                    reporting_period__end_date__lte=end_date,
        )
        .values(start_date=F("reporting_period__start_date"))
        .annotate(billable=Sum("billable_hours"),
            non_billable=Sum("non_billable_hours"))
        .filter(billable__isnull=False)
        .order_by("start_date")
    )
    frame = pd.DataFrame.from_records(data)
    return frame


def nonbillable_plot(data_frame):
    """Make a stacked area plot of nonbillable hours by project code.

    data_frame has start_date, category, and hours columns
    """
    fig = px.area(data_frame, x="start_date", y="hours", color="code_name",
            line_shape="hv")

    fig.update_layout(
        # autosize=False,
        # width=900,
        # height=500,
        xaxis=dict(autorange=True),
        yaxis=dict(autorange=True),
        xaxis_title="Reporting Period Start Date",
        yaxis_title="Hours",
        title=None,
        legend=dict(
            title=None,
            orientation="h",
            xanchor="right",
            x=1.0,
            yanchor="bottom",
            y=1.02,
        ),
    )

    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def nonbillable_data(start_date, end_date):
    """Get a data frame of non-billable category data.

    Has start_date, hours, and category columns.
    """
    Timecard = apps.get_model("hours", "Timecard")
    data = (Timecard.objects.filter(reporting_period__start_date__gte=start_date,
                                    reporting_period__end_date__lte=end_date,
                                    timecardobjects__project__accounting_code__billable=False,
        )
        .values(start_date=F("reporting_period__start_date"),
                category=F("timecardobjects__project__accounting_code"))
        .annotate(hours=Sum("timecardobjects__hours_spent"))
        .filter(hours__gt=0)
        .order_by("start_date")
    )
    # add the string representation of the account code back in
    data_list = list(data)  # list of dicts
    AccountingCode = apps.get_model("projects", "AccountingCode")
    categories = set(item["category"] for item in data_list)
    name_map = {}
    for category in categories:
        name_map[category] = str(AccountingCode.objects.filter(id=category)[0])
    for item in data_list:
        item["code_name"] = name_map[item["category"]]
    frame = pd.DataFrame.from_records(data_list)
    return frame
