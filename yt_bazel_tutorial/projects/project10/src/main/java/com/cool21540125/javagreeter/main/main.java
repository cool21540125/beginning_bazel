package com.cool21540125.javagreeter.main;

import com.cool21540125.javagreeter.greeter.Greeter;

class Main {
  public static void main(String[] args) {
    Greeter gg = new Greeter();
    System.out.println(gg.greet());
  }
}