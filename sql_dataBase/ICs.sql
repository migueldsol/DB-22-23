--A
CREATE OR REPLACE FUNCTION chk_employee_age_proc()
    RETURNS TRIGGER AS
    $$
    BEGIN
        IF date_part('year', age(current_date, NEW.bdate)) < 18 THEN
            RAISE EXCEPTION 'Employee must be at least 18 years old';
        END IF;

        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
DROP TRIGGER IF EXISTS chk_employee_age_trigger on employee;
CREATE TRIGGER chk_employee_age_trigger
BEFORE UPDATE OR INSERT ON employee
FOR EACH ROW EXECUTE PROCEDURE chk_employee_age_proc();

--B
CREATE OR REPLACE FUNCTION chk_workplace_specialization_proc()
    RETURNS TRIGGER AS
    $$
    BEGIN
        IF (NEW.address NOT IN (SELECT address FROM office) AND NEW.address NOT IN (SELECT address FROM warehouse))
            OR
           (NEW.address IN (SELECT address FROM warehouse) AND NEW.address IN (SELECT address from office)) THEN
            RAISE EXCEPTION 'Workplace must exclusively be an Office or Warehouse';
        END IF;

        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_workplace_specialization_trigger ON workplace;
CREATE TRIGGER chk_workplace_specialization_trigger
BEFORE UPDATE OR INSERT ON workplace
FOR EACH ROW EXECUTE PROCEDURE chk_workplace_specialization_proc();

--C
CREATE OR REPLACE FUNCTION chk_order_contains_proc()
    RETURNS TRIGGER AS
    $$
BEGIN
        IF NEW.order_no NOT IN (SELECT order_no FROM contains) THEN
            RAISE EXCEPTION 'Order must contain some product';
END IF;

RETURN NEW;
END;
    $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_order_contains_trigger on "order";
CREATE TRIGGER chk_order_contains_trigger
    BEFORE UPDATE OR INSERT ON "order"
    FOR EACH ROW EXECUTE PROCEDURE chk_order_contains_proc();




