package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func checksafe(levels []int) bool {
	safe := 0
	optimal := len(levels) - 1

	for i, v := range levels {
		if i > 0 && v-levels[i-1] <= 3 && v-levels[i-1] >= 1 {
			safe++
		}
	}

	return optimal == safe
}

func day02part1(file *os.File) int {
	scanner := bufio.NewScanner(file)

	total := 0

	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		fieldsi := []int{}

		for _, v := range fields {
			iv, _ := strconv.Atoi(v)
			fieldsi = append(fieldsi, iv)
		}

		fieldsir := []int{}

		for _, v := range fieldsi {
			fieldsir = append(fieldsir, v)
		}

		slices.Reverse(fieldsir)

		if checksafe(fieldsi) || checksafe(fieldsir) {
			total++
		}

	}
	return total
}

func permutate(levels []int) [][]int {
	output := [][]int{}
	for i, _ := range levels {
		temp := []int{}
		if i == 0 {
			temp = levels[1:]
		}
		if i > 0 && i < len(levels)-1 {
			temp = slices.Concat(levels[:i], levels[i+1:len(levels)])
		}
		if i == len(levels)-1 {
			temp = levels[:len(levels)-1]
		}
		output = append(output, temp)
	}
	return output
}

func dampener(levels []int) bool {
	if checksafe(levels) {
		return true
	}

mfor _, v := range permutate(levels) {
		if checksafe(v) {
			return true
		}
	}

	return false
}

func day02part2(file *os.File) int {
	scanner := bufio.NewScanner(file)

	total := 0

	for scanner.Scan() {
		flds := strings.Fields(scanner.Text())
		fields := []int{}

		for _, v := range flds {
			iv, _ := strconv.Atoi(v)
			fields = append(fields, iv)
		}

		if dampener(fields) {
			total++
		}

		slices.Reverse(fields)

		if dampener(fields) {
			total++
		}
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

	fmt.Println("Solution Day 2 Part 1: ", day02part1(file))

	file.Seek(0, 0)

	fmt.Println("Solution Day 2 Part 2: ", day02part2(file))
}
