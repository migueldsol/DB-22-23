    --A
ALTER TABLE employee
ADD CONSTRAINT check_age CHECK (bdate <= current_date - INTERVAL '18 years');

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
BEFORE UPDATE OR INSERT ON workplace DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE chk_workplace_specialization_proc();

--Verifica se ao adicionar/atualizar um office
--  se ele já é um warehouse
CREATE OR REPLACE FUNCTION chk_office_proc()
    RETURNS TRIGGER AS
    $$
    BEGIN
        IF (NEW.address IN (SELECT address FROM warehouse))
            RAISE EXCEPTION 'Workplace is already a Warehouse';
        END IF;

        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_office_trigger ON office;
CREATE CONSTRAINT TRIGGER chk_office_trigger
BEFORE INSERT OR UPDATE ON office DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE chk_office_proc();

--Verifica se a adicionar/atualizar um warehouse
--  se ele já é um office
CREATE OR REPLACE FUNCTION chk_warehouse_proc()
    RETURNS TRIGGER AS
    $$
    BEGIN
        IF (NEW.address IN (SELECT address FROM office))
            RAISE EXCEPTION 'Workplace is already an Office';
        END IF;

        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_warehouse_trigger ON warehouse;
CREATE CONSTRAINT TRIGGER chk_warehouse_trigger
BEFORE UPDATE OR INSERT ON warehouse DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE chk_warehouse_proc();

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
BEFORE UPDATE OR INSERT ON "order" DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE chk_order_contains_proc();

--ao apagar uma order apaga também os contains (acho que é opcional)
CREATE OR REPLACE FUNCTION delete_order_proc()
    RETURNS TRIGGER AS
    $$
BEGIN
        DELETE FROM contains WHERE order_no = old.order_no;
END IF;

RETURN NEW;
END;
    $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS delete_order_trigger on "order";
CREATE TRIGGER delete_order_trigger
AFTER DELETE ON "order"
FOR EACH ROW EXECUTE PROCEDURE delete_order_proc();

--verifica que ao dar delete deixa pelo menos um contains
CREATE OR REPLACE FUNCTION chk_delete_contains_proc()
    RETURNS TRIGGER AS
    $$
BEGIN
        IF (SELECT COUNT(*) FROM contains WHERE order_no = old.order_no) == 1 THEN 
            RAISE EXCEPTION 'Order needs to have at least one product.'
END IF;

RETURN NEW;
END;
    $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_delete_contains_trigger on contains;
CREATE CONSTRAINT TRIGGER chk_delete_contains_trigger
BEFORE UPDATE OR INSERT ON contains DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE chk_delete_contains_proc();

