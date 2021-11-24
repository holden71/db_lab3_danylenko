select * from products;
create table productscopy as select * from products; 
select * from productscopy;


DO $$
DECLARE
    product_id     productscopy.product_id%TYPE;
    product_name   productscopy.product_name%TYPE;
	product_price  productscopy.product_price%TYPE;
	

BEGIN
    product_id := 10000;
    product_name := 'Script';
	product_price := 4.99;
	
    FOR counter IN 1..10
        LOOP
            INSERT INTO productscopy(product_id, product_name, product_price)
            VALUES (product_id + counter, product_name || counter, product_price + counter);
        END LOOP;
END;
$$
