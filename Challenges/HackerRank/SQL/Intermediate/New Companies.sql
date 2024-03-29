SELECT COMPANY_CODE, FOUNDER,
(SELECT COUNT(DISTINCT LEAD_MANAGER_CODE) FROM Employee WHERE COMPANY_CODE = C.COMPANY_CODE ),
(SELECT COUNT(DISTINCT SENIOR_MANAGER_CODE) FROM Employee WHERE COMPANY_CODE = C.COMPANY_CODE ),
(SELECT COUNT(DISTINCT MANAGER_CODE) FROM Employee WHERE COMPANY_CODE = C.COMPANY_CODE ),
(SELECT COUNT(DISTINCT EMPLOYEE_CODE) FROM Employee WHERE COMPANY_CODE = C.COMPANY_CODE )
FROM COMPANY C
ORDER BY COMPANY_CODE;