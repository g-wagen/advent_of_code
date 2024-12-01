package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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

	sort.Ints(left)
	sort.Ints(right)

	distance := 0

	for i := range left {
		diff := left[i] - right[i]
		if left[i] < right[i] {
			diff = right[i] - left[i]
		}
		distance = distance + diff
	}

	fmt.Println(distance)

}
