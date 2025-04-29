package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("This is New Added Life ... ")
	sum()
}

func sum() {
	fmt.Println("added new life")

	x := 0
	fmt.Scanf("%d", &x)
	fmt.Printf("The Number is %v \n ", x)

	if z := 2 * rand.Intn(x); z <= x {
		fmt.Printf("z is %v and x is %v \n ", z, x)
	} else {
		fmt.Println("Added New Lifes ")
	}

}
