select country_name, count(d.id), cast(avg(total_price) as decimal(12,6))
from invoice a
inner join customer b on a.customer_id=b.id
inner join city c on b.city_id=c.id
inner join country d on c.country_id=d.id
group by country_name,d.id
having (select avg(total_price) 
from invoice z
inner join customer y on z.customer_id=y.id
inner join city x on y.city_id=x.id
inner join country w on x.country_id=w.id
where w.id=d.id
) > 
(select avg(total_price) 
from invoice 
)
for read only;