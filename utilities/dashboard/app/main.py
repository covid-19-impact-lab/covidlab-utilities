"""
usage: bokeh server run_dashboard.py --show --args path/to/overview_tab_data_dict.pickle

"""
import sys
from pathlib import Path

import pandas as pd
from bokeh.models import Panel
from bokeh.models import Tabs
from bokeh.plotting import curdoc

from utilities.dashboard.components.intro_page.create_component import create_intro_page
from utilities.dashboard.components.run_charts.create_component import create_run_charts
from utilities.dashboard.components.univariate_distributions.create_component import (
    create_univariate_distributions,
)


def assemble_dashboard_components(
    intro_page_data,
    univariate_distributions_data,
    shared_data,
    run_charts_data,
    run_charts_mapping,
):
    """Create the dashboard tabs.

    Args:
        intro_page_data (dict): Data to generate Introduction tab.
        univariate_distributions_data (dict): Data to generate Group Differences
            tab.
        shared_data (dict): Metadata shared between Maps and Group Differences tab.
        run_charts_data (dict): Data for Labor Supply tab.
        run_charts_mapping (dict): Metadata for Labor Supply tab.

    Returns:
        bokeh Column

    """

    intro_page = create_intro_page(**intro_page_data, language=shared_data["language"])

    univariate_distributions_page = create_univariate_distributions(
        **univariate_distributions_data,
        menu_labels=shared_data["menu_labels"],
        variable_mappings=shared_data["variable_mappings"],
    )

    run_charts_page = create_run_charts(
        data=run_charts_data,
        variable_mappings=run_charts_mapping["variable_mappings"],
    )

    if language == "german":
        tab_names = [
            "Einleitung",
            "Karten",
            "Unterschiede zw. Gruppen",
            "Arbeitskräfteangebot",
        ]
    elif language == "english":
        tab_names = ["Introduction", "Group Differences", "Labor Supply"]

    page = Tabs(
        tabs=[
            Panel(child=intro_page, title=tab_names[0]),
            Panel(child=univariate_distributions_page, title=tab_names[1]),
            Panel(child=run_charts_page, title=tab_names[2]),
        ]
    )
    return page


# ======================================================================================
# The actual app
# ======================================================================================

data_dir = Path(sys.argv[1]).resolve()
dashboard_data_shared = pd.read_pickle(data_dir / "dashboard_data_single.pickle")
dashboard_data_waves = pd.read_pickle(data_dir / "dashboard_data_waves.pickle")

kwargs = {
    "intro_page_data": dashboard_data_shared["intro_page_data"],
    "univariate_distributions_data": dashboard_data_shared[
        "univariate_distributions_data"
    ],
    "shared_data": dashboard_data_shared["shared_data"],
    "run_charts_data": dashboard_data_waves["run_charts_data"],
    "run_charts_mapping": dashboard_data_waves["mapping"],
}


language = dashboard_data_shared["shared_data"]["language"]

doc = curdoc()
if language == "english":
    doc.title = "Explore What People Believe and Do in Response to CoViD-19"
elif language == "german":
    doc.title = "Was Menschen zur Corona-Epidemie wissen, erwarten und tun"


overview_tab = assemble_dashboard_components(**kwargs)
# corr_tab = create_corr_tab(dashboard_data["correlation"])
# timeline_tab = create_timeline_tab(dashboard_data["timeline"])
# tabs = Tabs(tabs=[overview_tab, corr_tab], name="tabs")
# doc.add_root(tabs)
doc.add_root(overview_tab)
