package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func d7p1(file *os.File) int {
	scanner := bufio.NewScanner(file)
	total := 0

	m := []string{}

	for scanner.Scan() {
		m = append(m, scanner.Text())
	}

	for _, item := range m {
		input := strings.Split(item, ":")
		target, _ := strconv.Atoi(input[0])
		numbersLine := strings.Split(strings.TrimSpace(input[1]), " ")

		numbers := make([]int, len(numbersLine))
		for i, num := range numbersLine {
			numbers[i], _ = strconv.Atoi(num)
		}

		result := []int{}

		result = append(result, numbers[0]+numbers[1])
		result = append(result, numbers[0]*numbers[1])

		remaining := numbers[2:]

		for _, num := range remaining {
			newResult := []int{}
			for _, o := range result {
				newResult = append(newResult, o+num)
				newResult = append(newResult, o*num)
			}
			result = newResult
		}
		if slices.Contains(result, target) {
			total += target
		}
	}
	return total
}

func d7p2(file *os.File) int {
	scanner := bufio.NewScanner(file)
	total := 0

	canvas := [][]string{}

	for scanner.Scan() {
		canvas = append(canvas, strings.Split(scanner.Text(), ""))
	}

	return total
}

func main() {
	file, error := os.Open(os.Args[1])

	if error != nil {
		fmt.Println(error)
		return
	}

	defer file.Close()

	fmt.Println("Solution Day 7 Part 1:", d7p1(file))

	file.Seek(0, 0)

	fmt.Println("Solution Day 7 Part 2:", d7p2(file))
}
