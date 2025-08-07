from jinja2 import Environment, FileSystemLoader
import os 

def render_html_report(data, output_file):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")
    html_content = template.render(data=data)

    output_path = f"reports/html_reports/{output_file}"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    return output_path