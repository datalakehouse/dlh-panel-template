# DataLakehouse sample panel application

This is a sample GitHub application that has the necessary structure to deploy your panel application in DataLakehouse.

### Structure

To make your panel application deployable, please follow the guidelines below:

* Add a `requirements.txt` file in the root directory of the repository with all the necessary libraries to run the project;
* The panel dashboard Python files should not use `pn.serve()` or `pn.show()`, as our code will be responsible for serving the dashboards. Instead, create a `pn.template.FastListTemplate` and make it `servable()`. Here is an example:
```python
row3 = pn.Row(bar_plot2, line_plot2)
row4 = pn.Row(scatter_plot2, area_plot2)

template2 = pn.template.FastListTemplate(title='Dashboard 2', main=[row3, row4])

template2.servable()
```
* Add a `dashboard_files.yaml` file pointing to each servable file path with the following structure:

```yaml=
dashboard-files:
  - file_path: "dashboards/dashboard1.ipynb"
    name: Dashboard_1
  - file_path: "dashboards/dashboard.py"
    name: Dashboard_2
```
* Ensure that the paths in dashboard_files.yaml point to the correct folder in your repository that contains the files. If the files are in the root folder, simply include their names as shown below:
```yaml=
dashboard-files:
  - file_path: "filename.py"
    name: Dashboard_Name
```
