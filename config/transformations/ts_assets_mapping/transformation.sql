  select ts.externalId as externalId, ast.id as assetId

  from `_cdf`.`timeseries` as ts

  INNER JOIN `_cdf`.`assets` AS ast ON split(ts.externalId, ":") [0] = ast.externalId;
