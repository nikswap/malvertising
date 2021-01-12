SELECT
    domain
FROM
    domainnames
WHERE
    http_status BETWEEN 200 AND 299
;
