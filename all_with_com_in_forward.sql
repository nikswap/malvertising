SELECT
        domainnames.added_at
    ,   forwards.added_at
    ,    domain
    ,   forward_to
FROM
    domainnames
    INNER JOIN forwards ON
    domainnames.id = forwards.domainid
WHERE
    INSTR(forward_to,REPLACE(domain,'www.','')) = 0
	AND
    INSTR(forward_to,'.com') > 0
	AND
    INSTR(forward_to, substr(REPLACE(domain,'www.',''),1,INSTR(REPLACE(domain,'www.',''),'.'))) = 0
ORDER BY
    domainnames.added_at DESC
LIMIT 30
;
