package com.cool21540125.javagreeter.greeter;

import com.github.javafaker.Faker;

public class Greeter {
  private Faker faker;

  public Greeter() {
    this.faker = new Faker();
  }

  public String greet() {
    return "Hello, " + this.faker.name().fullName() + ".";
  }
}