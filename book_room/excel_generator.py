import xlsxwriter


def create_excel_file(data):
    workbook = xlsxwriter.Workbook('results.xlsx')

    worksheet_name = 'Days'
    worksheet = workbook.add_worksheet(worksheet_name)

    # table headers
    header = workbook.add_format({'italic': True, 'border': 1, 'align': 'center'})
    worksheet.write(0, 0, 'Value', header)
    worksheet.write(0, 1, 'Created At', header)
    worksheet.set_column("A:B", 16)
    worksheet.freeze_panes(1, 0)

    # table
    date_format = workbook.add_format({'num_format': 'yyyy-mm-dd hh:mm'})

    row = 1

    for value, dt in data:
        worksheet.write_number(row, 0, value)
        worksheet.write_datetime(row, 1, dt, date_format)
        row += 1

    # chart
    stats_len = len(data)

    chart = workbook.add_chart({'type': 'line'})
    chart.add_series({
        'categories': f'={worksheet_name}!$B$2:$B${stats_len + 1}',
        'values': f'={worksheet_name}!$A$2:$A${stats_len + 1}',
        'line': {'color': '#4A8F31'},
        'marker': {'type': 'circle'},
        'data_labels': {
            'value': True,
            'font': {'rotation': 45, 'size': 6, 'bold': True},
        },
    })
    chart.set_x_axis({
        'name': 'Date',
        'date_axis': True,
        'num_format': 'yyyy-mm-dd',
        'name_font': {'size': 8},
        'num_font': {'size': 8},
    })
    chart.set_y_axis({
        'name': 'Value',
        'name_font': {'size': 8},
        'num_font': {'size': 8},
    })
    chart.set_legend({'none': True})

    worksheet.insert_chart('D2', chart, {
        'x_scale': 1.2,
        'y_scale': 1.2,
    })

    workbook.close()


from datetime import datetime

create_excel_file([
    (22, datetime.fromisoformat('2022-01-01T12:00:00')),
    (11, datetime.fromisoformat('2022-02-01T12:00:00')),
    (35, datetime.fromisoformat('2022-03-01T12:00:00')),
    (87, datetime.fromisoformat('2022-04-01T12:00:00')),
    (20, datetime.fromisoformat('2022-05-01T12:00:00')),
])
