-- Projects are high-level activities made up of tasks

--FruitKind
create table FruitCatagory(
    id        int primary key,  --catagory_id
    catagory_description text,

)
create table fruit_item (
    id        int primary key,
    catagory_id int,
    list_price DECIMAL,
    fruit_name  text,
    description text,
    barcode text,
    last_update_timestamp DATE,
    create_timestamp DATE
);

create table stock (
    item_id        int primary key,
    fruit_id int,
    weight_in_stock DECIMAL,
    purchase_price DECIMAL,
    last_update_timestamp DATE,
    create_timestamp DATE
);
