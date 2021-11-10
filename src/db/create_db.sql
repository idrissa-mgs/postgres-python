CREATE SCHEMA IF NOT EXISTS e_commerce;

CREATE TABLE IF NOT EXISTS e_commerce.customers(
    customer_id              VARCHAR(32) NOT NULL,
    customer_unique_id      VARCHAR(32),
    customer_zip_code_prefix  VARCHAR(10),
    customer_city        VARCHAR(50),
    customer_state       VARCHAR(7),
    PRIMARY KEY (customer_id) 
);


CREATE TABLE IF NOT EXISTS e_commerce.orders(
    order_id  VARCHAR(32) NOT NULL,
    customer_id VARCHAR(32) NOT NULL,
    order_status  VARCHAR(50),
    order_purchase_timestamp timestamp,
    order_approved_at timestamp,
    order_delivered_carrier_date timestamp,
    order_delivered_customer_date timestamp,
    order_estimated_delivery_date timestamp,
    PRIMARY KEY (order_id),
    CONSTRAINT fk_customer 
        FOREIGN KEY (customer_id) 
            REFERENCES e_commerce.customers(customer_id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS e_commerce.products(
    product_id  VARCHAR(32) NOT NULL,
    product_category_name VARCHAR(100) ,
    product_name_lenght  integer ,
    product_description_lenght integer,
    product_photos_qty integer,
    product_weight_g integer,
    product_length_cm integer,
    product_height_cm integer,
    product_width_cm integer,
    product_category_name_english VARCHAR(100),
    PRIMARY KEY (product_id)
);

CREATE TABLE IF NOT EXISTS e_commerce.items(
    order_id  VARCHAR(32) NOT NULL,
    order_item_id  VARCHAR(10),
    product_id  VARCHAR(32) NOT NULL,
    seller_id  VARCHAR(32) NOT NULL,
    shipping_limit_date timestamp,
    price REAL,
    freight_value REAL
);


CREATE TABLE IF NOT EXISTS e_commerce.items(
    order_id  VARCHAR(32) NOT NULL,
    order_item_id  integer,
    product_id  VARCHAR(32) NOT NULL,
    seller_id  VARCHAR(32) NOT NULL,
    shipping_limit_date timestamp,
    price REAL,
    freight_value REAL,
    -- CONSTRAINT fk_product
    -- FOREIGN KEY(product_id) 
    --    REFERENCES e_commerce.products(product_id) ON DELETE CASCADE
    CONSTRAINT fk_order
        FOREIGN KEY(order_id) REFERENCES e_commerce.orders(orders_id)
;