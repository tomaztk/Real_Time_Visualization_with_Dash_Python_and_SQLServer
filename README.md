# Real Time Visualization with Dash Python and Microsoft SQL Server

<!-- badges: start -->
![](http://img.shields.io/badge/Real_Time_Visualization-green.svg)
![](http://img.shields.io/badge/Dash-blue.svg)
![](http://img.shields.io/badge/MSSQL-darkred.svg)
<!-- badges: end -->

(Near) Real-Time data visualization with Dash Python and Microsoft SQL Server

<div>
  <a href="https://tomaztsql.files.wordpress.com/2018/06/2018-06-18-18_28_08-dash.png"><img width="60%" src="https://tomaztsql.files.wordpress.com/2018/06/2018-06-18-18_28_08-dash.png"></a>

</div>
<span style="font-size: xx-large; font-weight: normal;">Real-time setup for visualizing MSSQL Server data with
use of Dash application as client server and little Python code to get the Dash framework started.</span>


## Cloning the repository
You can follow the steps below to clone the repository.
```
git clone https://github.com/tomaztk/Real_Time_Visualization_with_Dash_Python_and_SQLServer.git
```

## Quickstart

1.  Clone the repository
2.  In your local Microsoft SQL Server run the file: `Real-Time Stats Visualization.sql`
3.  Run your Python environment and `{sudo} pip install dash`
4.  When Dash is installed, run the file: `Real_TimeStatsVisualizationWithDash.py`
5.  Change connection string in Python file, pointing to your local database server.

``` Python

    sql_conn = connectSQLServer('ODBC Driver 13 for SQL Server', 'MyMSSQL\Database', 'UserName', 'Pa$$w0rd') 
    cursor = sql_conn.cursor()
```     
6.  Open your web browser pointing to your localhost.


## Blogpost
Originally posted on ([blog](https://tomaztsql.wordpress.com/2018/06/18/real-time-data-visualization-with-sql-server-and-python-dash/)). Read blogpost for additional information.


## Video

![Dash Process](https://github.com/tomaztk/Real_Time_Visualization_with_Dash_Python_and_SQLServer/blob/master/ScreenCaptureProject1.mp4)
