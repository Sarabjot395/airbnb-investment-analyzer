CREATE TABLE listings (
	id BIGINT, 
	name TEXT, 
	host_id BIGINT, 
	host_name TEXT, 
	neighbourhood_group TEXT, 
	neighbourhood TEXT, 
	latitude FLOAT, 
	longitude FLOAT, 
	room_type TEXT, 
	price BIGINT, 
	minimum_nights BIGINT, 
	number_of_reviews BIGINT, 
	last_review TEXT, 
	reviews_per_month FLOAT, 
	calculated_host_listings_count BIGINT, 
	availability_365 BIGINT, 
	city TEXT
);
