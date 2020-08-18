Instructions for the Covid Impact Lab Dashboard
================================================

To run dashboard, there are two steps.

First, you must create the dictionary with the aggregated data that will be passed to
the bokeh app. To do so, call the `from_data_to_dashboard.py` with the following arguments:

`python from_data_to_dashboard.py [lang] [path/to/data]`

`lang` can be either english or german.

`path/to/data` must be the path to the Covid LISS dataset.

This will create a `dashboard_data_liss_{lang}_current.pickle` file in the folder you are in.

Only Hans-Martin has the true region codes. He passes a third argument to the command
that is the path to the regions identifiers. If no third argument is passed, mock regions
are created and you are warned about this.

Secondly, you must start the bokeh server passing the created pickle to it. To do so, run:

`python run_dashboard.py dashboard_data_liss_{lang}_current.pickle`

Assuming - as the Python module does - that you are in the same directory as the app
directory and that the dashboard_data pickle was also created there.
