
import IPython.display
import pandas


__all__ = ["output_url"]

def output_url(url):
    IPython.display.publish_display_data(
        {"application/x.jupyter.relative-dataset-urls+json": [url]}
    )