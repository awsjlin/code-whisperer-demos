package com.amazon.aws.customerapi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

//load values into database
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;


@SpringBootApplication
public class CustomerapiApplication {

	public static void main(String[] args) {
		SpringApplication.run(CustomerapiApplication.class, args);
	}

	@Bean
	public CommandLineRunner loadData(CustomerRepository repository) {
		return (args) -> {
			// ENTER CW COMMENT HERE TO GENERATE TEST DATA
			

			//get all customers from database and print to console
			for (Customer customer : repository.findAll()) {
				System.out.println(customer);
			}
		};

	}
}
