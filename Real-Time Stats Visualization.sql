/* ************************************************
Author: Tomaz Kastrun
Date: 17.06.2018

Visualizing real-time data stream  
using Python Dash and Microsoft SQL Server
**************************************************/

USE Test;
GO


SELECT @@SERVERNAME as Servername
-- TOMAZK\MSSQLSERVER2017



DROP TABLE IF EXISTS dbo.LiveStatsFromSQLServer;
GO


CREATE TABLE dbo.LiveStatsFromSQLServer
(
 ID int identity(1,1)
,Num tinyint NOT NULL
)


-- Insert some test data
INSERT INTO dbo.LiveStatsFromSQLServer(num)
SELECT ABS(CHECKSUM(NewId())) % 14
GO 2


-- Do some inserts to mimic the data stream
INSERT INTO dbo.LiveStatsFromSQLServer(num)
SELECT ABS(CHECKSUM(NewId())) % 14
WAITFOR DELAY '00:00:01.500'
GO 1000



-- Open new connection 
-- Run this query and watch the last records being inserted 
-- as they are presented on the graph as well
SELECT 
	TOP 10 num,ID 
FROM dbo.LiveStatsFromSQLServer WITH (NOLOCK)
ORDER BY ID DESC



