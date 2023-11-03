package main

import (
	"log"
	"net/http"

	"project4/go_hello_world"

	"github.com/gorilla/mux"
)

func YourHandler(w http.ResponseWriter, r *http.Request) {
	log.Println("Received request")
	w.Write([]byte(go_hello_world.HelloWorld()))
	w.Write([]byte("Hello World"))
}

func main() {
	r := mux.NewRouter()
	// Routes consist of a path and a handler function.

	r.HandleFunc("/", YourHandler)

	// Bind to a port and pass our router in
	log.Println("Going to listen on port 8080")
	log.Fatal(http.ListenAndServe(":8080", r))
}
