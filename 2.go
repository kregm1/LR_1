package main

import (
	"fmt"
)

func CopyOnChange(src, dst chan float64, delta float64) {
	defer close(dst)
	var prevValue float64
	var initialized bool

	for value := range src {
		if !initialized {
			initialized = true
			prevValue = value
			dst <- value
		} else if abs(value-prevValue) > delta {
			prevValue = value
			dst <- value
		}
	}
}

func abs(a float64) float64 {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	src := make(chan float64)
	dst := make(chan float64)

	go CopyOnChange(src, dst, 0.5)

	go func() {
		values := []float64{0.0, -0.9, 0.4, 1.0, 1.1, 2.0, 2.48, 3.0}
		for _, v := range values {
			src <- v
		}
		close(src)
	}()

	for v := range dst {
		fmt.Println(v)
	}
}
