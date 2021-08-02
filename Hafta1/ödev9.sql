select city,country from city
INNER JOIN country ON city.country_id = country.country_id;

select first_name, last_name,payment_id from customer
INNER JOIN payment ON customer.customer_id = payment.customer_id;

select rental_id,first_name, last_name from customer
INNER JOIN rental ON customer.customer_id= rental.customer_id;
