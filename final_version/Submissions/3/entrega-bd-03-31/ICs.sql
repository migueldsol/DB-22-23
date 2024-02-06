    --A
ALTER TABLE employee
ADD CONSTRAINT check_age CHECK (bdate <= current_date - INTERVAL '18 years')
;

    --B
--Verifica se o workplace, quando inserido ou atualizado,
--  é obrigatóriamente um office ou um workplace 
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
CREATE CONSTRAINT TRIGGER chk_workplace_specialization_trigger
AFTER UPDATE OR INSERT ON workplace DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE chk_workplace_specialization_proc();

--Verifica se ao adicionar/atualizar um office
--  se ele já é um warehouse
CREATE OR REPLACE FUNCTION chk_office_proc()
    RETURNS TRIGGER AS
    $$
    BEGIN
        IF (NEW.address IN (SELECT address FROM warehouse)) THEN
            RAISE EXCEPTION 'Workplace is already a Warehouse';
        END IF;

        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_office_trigger ON office;
CREATE CONSTRAINT TRIGGER chk_office_trigger
AFTER INSERT OR UPDATE ON office DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE chk_office_proc();

--Verifica se a adicionar/atualizar um warehouse
--  se ele já é um office
CREATE OR REPLACE FUNCTION chk_warehouse_proc()
    RETURNS TRIGGER AS
    $$
    BEGIN
        IF (NEW.address IN (SELECT address FROM office)) THEN
            RAISE EXCEPTION 'Workplace is already an Office';
        END IF;

        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_warehouse_trigger ON warehouse;
CREATE CONSTRAINT TRIGGER chk_warehouse_trigger
AFTER UPDATE OR INSERT ON warehouse DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE chk_warehouse_proc();

--Verifica se ao apagar um office
--  se existe um warehouse associado
--  a esse workplace
CREATE OR REPLACE FUNCTION chk_delete_office_proc()
    RETURNS TRIGGER AS
    $$
    BEGIN
        IF EXISTS (SELECT address FROM workplace WHERE address = old.address) AND NOT EXISTS (SELECT address FROM warehouse WHERE address = OLD.address) THEN
            RAISE EXCEPTION 'Cannot delete office without an associated warehouse to the workplace';
        END IF;

        RETURN OLD;
    END;
    $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_delete_office_trigger ON office;
CREATE CONSTRAINT TRIGGER chk_delete_office_trigger
AFTER DELETE ON office DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE chk_delete_office_proc();

--Verifica se ao apagar um warehouse
--  se existe um office associado
--  a esse workplace
CREATE OR REPLACE FUNCTION chk_delete_warehouse_proc()
    RETURNS TRIGGER AS
    $$
    BEGIN
        IF EXISTS (SELECT address FROM workplace WHERE address = old.address) AND NOT EXISTS (SELECT address FROM office WHERE address = OLD.address) THEN
            RAISE EXCEPTION 'Cannot delete warehouse without an associated office to the workplace';
        END IF;

        RETURN OLD;
    END;
    $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_delete_warehouse_trigger ON warehouse;
CREATE TRIGGER chk_delete_warehouse_trigger
BEFORE DELETE ON warehouse
FOR EACH ROW EXECUTE PROCEDURE chk_delete_warehouse_proc();

    --C
--verifica que a order tem contains
CREATE OR REPLACE FUNCTION chk_order_contains_proc()
    RETURNS TRIGGER AS
    $$
BEGIN
        IF NEW.order_no NOT IN (SELECT order_no FROM contains) THEN
            RAISE EXCEPTION 'Order needs to have at least one product.';
END IF;

RETURN NEW;
END;
    $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_order_contains_trigger on "order";
CREATE CONSTRAINT TRIGGER chk_order_contains_trigger
AFTER UPDATE OR INSERT ON "order" DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE chk_order_contains_proc();

--verifica que ao dar delete deixa pelo menos um contains
CREATE OR REPLACE FUNCTION chk_delete_contains_proc()
    RETURNS TRIGGER AS
    $$
BEGIN
    IF EXISTS (SELECT order_no FROM "order" WHERE order_no = old.order_no) AND NOT EXISTS (SELECT order_no FROM contains WHERE order_no = old.order_no) THEN
        RAISE EXCEPTION 'Order % needs to have at least one product.', old.order_no;
END IF;

RETURN NEW;
END;
    $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_delete_contains_trigger on contains;
CREATE CONSTRAINT TRIGGER chk_delete_contains_trigger
AFTER DELETE ON contains DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE chk_delete_contains_proc()
