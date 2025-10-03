# html_report/generate.py
import os
import uuid
import webbrowser

def generate_html(dataframe):
    """Generate HTML with DataTables, toggles for original/adjusted columns."""
    table_html = dataframe.to_html(table_id="table", index=False, classes="display")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Soccer Player Analysis</title>
        <link rel="stylesheet"
              href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css">
        <link rel="stylesheet"
              href="https://cdn.datatables.net/fixedheader/3.2.2/css/fixedHeader.dataTables.min.css">
        <link rel="stylesheet"
              href="https://cdn.datatables.net/fixedcolumns/4.0.2/css/fixedColumns.dataTables.min.css">
        <style>
            body {{ font-family: Arial, sans-serif; }}
            #controls {{
                display: flex;
                align-items: center;
                margin-bottom: 1em;
            }}
            #controls label {{ margin-right: 1.5em; font-size: 0.9em; }}
            table {{ width: 100%; }}
            th, td {{ text-align: left; padding: 8px; white-space: nowrap; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
            .DTFC_LeftBodyWrapper table,
            .DTFC_LeftHeadWrapper table {{ background-color: white; }}
            .hidden-col {{ display: none !important; }}
        </style>
    </head>
    <body>
        <div id="controls">
            <label><input type="checkbox" id="origToggle" checked> Original</label>
            <label><input type="checkbox" id="adjToggle" checked> Adjusted</label>
        </div>

        {table_html}

        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
        <script src="https://cdn.datatables.net/fixedheader/3.2.2/js/dataTables.fixedHeader.min.js"></script>
        <script src="https://cdn.datatables.net/fixedcolumns/4.0.2/js/dataTables.fixedColumns.min.js"></script>

        <script>
        $(document).ready(function() {{
            const alwaysVisible = ['Name', 'Position', 'Age', 'Height', 'Club', 'TransferValue', 'Salary'];
            var adjIndexes = [];
            $('#table thead th').each(function(i) {{
                if ($(this).text().trim().endsWith('_adj')) {{
                    adjIndexes.push(i);
                }}
            }});

            var table = $('#table').DataTable({{
                scrollX: true,
                scrollY: true,
                paging: true,
                searching: true,
                order: [[1, 'asc']],
                pageLength: 15,
                fixedHeader: true,
                fixedColumns: {{ leftColumns: 4 }},
                columnDefs: [
                    {{
                        targets: adjIndexes,
                        type: 'num',
                        render: $.fn.dataTable.render.number(',', '.', 1)
                    }}
                ]
            }});

            var fc = table.fixedColumns();

            table.columns().every(function(idx) {{
                var header = $(this.header()).text().trim();
                if (alwaysVisible.includes(header)) {{
                    $(this.header()).addClass('identity-col');
                    $(this.nodes()).addClass('identity-col');
                }} else if (header.endsWith('_adj')) {{
                    $(this.header()).addClass('adj-col');
                    $(this.nodes()).addClass('adj-col');
                }} else {{
                    $(this.header()).addClass('orig-col');
                    $(this.nodes()).addClass('orig-col');
                }}
            }});

            function toggleColumnGroup(groupClass, visible) {{
                const action = visible ? 'removeClass' : 'addClass';
                $('.' + groupClass)[action]('hidden-col');
                table.columns.adjust();
                fc.update();
            }}

            $('#origToggle').on('change', function() {{
                toggleColumnGroup('orig-col', this.checked);
            }});

            $('#adjToggle').on('change', function() {{
                toggleColumnGroup('adj-col', this.checked);
            }});

            $(window).on('resize', function() {{
                table.columns.adjust();
                fc.update();
            }});
        }});
        </script>
    </body>
    </html>
    """
    return html

def save_and_open_html(html_content, directory):
    """Save HTML content to a file and open it in the default browser."""
    os.makedirs(directory, exist_ok=True)
    filename = str(uuid.uuid4()) + ".html"
    full_path = os.path.join(directory, filename)
    with open(full_path, "w", encoding="utf-8") as file:
        file.write(html_content)
    webbrowser.open_new_tab(full_path)
    print(f"File saved to {full_path}")
