package main

import (
	"log"
	"math/rand"
	"net/http"
	"strconv"

	"project4/go_calculator"

	"github.com/gorilla/mux"
)

func YourHandler(w http.ResponseWriter, r *http.Request) {
	log.Println("Received request")
	rnd1 := rand.Intn(100)
	rnd2 := rand.Intn(100)

	msg := "我很懷疑你真的不知道 " + strconv.Itoa(rnd1) + " + " + strconv.Itoa(rnd2) + " = " + strconv.Itoa(go_calculator.Add(rnd1, rnd2))
	w.Write([]byte(msg))
}

func main() {
	r := mux.NewRouter()
	// Routes consist of a path and a handler function.

	r.HandleFunc("/", YourHandler)

	// Bind to a port and pass our router in
	log.Println("Going to listen on port 8080")
	log.Fatal(http.ListenAndServe(":8080", r))
}
