select city, country from country
LEFT JOIN city ON city.country_id = country.country_id;

select payment_id, first_name, last_name from customer
RIGHT JOIN payment ON customer.customer_id = payment.customer_id;

select rental_id, first_name, last_name from customer
FULL JOIN rental ON customer.customer_id = rental.customer_id;
