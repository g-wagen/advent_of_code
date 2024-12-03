package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func day01part1(file *os.File) int {
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
		distance += diff
	}
	return distance
}

func day01part2(file *os.File) int {
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

		similar += left[i] * counts
	}
	return similar
}

func main() {
	file, error := os.Open(os.Args[1])

	if error != nil {
		fmt.Println(error)
		return

	}

	defer file.Close()

	fmt.Println("Solution Day 1 Part 1: ", day01part1(file))

	file.Seek(0, 0)

	fmt.Println("Solution Day 1 Part 2: ", day01part2(file))
}
