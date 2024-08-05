import pandas as pd

from .environments import excel_export


def write_to_excel(data_frame, aggregated_data):
    with pd.ExcelWriter(excel_export) as writer:
        for name, data in data_frame.items():
            data.to_excel(writer, sheet_name=name, index=False)

        consolidate_data = pd.DataFrame(aggregated_data)
        consolidate_data.to_excel(writer, sheet_name="CONSOLIDADO", index=False)
