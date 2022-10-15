select * from (
  select 
    product_class_name
    ,rank() over (partition by product_class_name order by sales_value desc, total_quantity asc) as rank
    ,product_name
    ,sales_value
  from (
    select
      product_class_name
      ,product_name
      ,sum(quantity) as total_quantity
      ,sum(quantity*retail_price) as sales_value
    from `sales-transaction` st
    inner join `product` p on st.product_id = p.product_id
    inner join `product_class` pc on pc.product_class_id = p.product_class_id
    group by 1,2
  )
)where rank between 1 and 2
order by product_class_name ,rank