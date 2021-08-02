select count(*) from film

where length > (select AVG(length) from film );

select count(*) from film

where rental_rate = (select max(rental_rate) from film);

select title from film

where rental_rate = (select min(rental_rate) from film) and replacement_cost = (select min(replacement_cost) from film);

select first_name, count(payment.payment_id) from customer
JOIN payment ON customer.customer_id= payment.customer_id
group by customer.customer_id
order by count(payment.payment_id) DESC;
