package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, error := os.Open("01-input.txt")

	if error != nil {
		fmt.Println(error)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	left := []int{}
	right := []int{}

	for scanner.Scan() {

		fields := strings.Fields(scanner.Text())
		leftint, _ := strconv.Atoi(strings.TrimSpace(fields[0]))
		rightint, _ := strconv.Atoi(strings.TrimSpace(fields[1]))

		left = append(left, leftint)
		right = append(right, rightint)
	}

	similar := 0

	for i := range left {
		counts := 0

		for j := range right {
			if left[i] == right[j] {
				counts++
			}
		}

		similar = similar + left[i]*counts
	}

	fmt.Println(similar)

}
