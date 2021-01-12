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
;