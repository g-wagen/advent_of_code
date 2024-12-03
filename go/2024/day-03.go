package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func day03part1(file *os.File) int {
	scanner := bufio.NewScanner(file)
	total := 0

	for scanner.Scan() {
		puzzleInput := scanner.Text()
		pattern := regexp.MustCompile(`mul\(\d{1,3},\d{1,3}\)`)

		found := pattern.FindAllString(puzzleInput, -1)

		for _, v := range found {
			subPattern := regexp.MustCompile(`\d+`)
			factors := subPattern.FindAllString(v, -1)
			factor1, _ := strconv.Atoi(factors[0])
			factor2, _ := strconv.Atoi(factors[1])
			total += factor1 * factor2
		}
	}
	return total
}

func day03part2(file *os.File) int {
	scanner := bufio.NewScanner(file)

	total := 0
	doIt := true

	for scanner.Scan() {
		puzzleInput := scanner.Text()
		pattern := regexp.MustCompile(`mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)`)

		found := pattern.FindAllString(puzzleInput, -1)

		for _, v := range found {
			if v == "do()" {
				doIt = true
			}
			if v == "don't()" {
				doIt = false
			}

			if doIt && strings.HasPrefix(v, "mul") {
				subPattern := regexp.MustCompile(`\d+`)
				factors := subPattern.FindAllString(v, -1)
				factor1, _ := strconv.Atoi(factors[0])
				factor2, _ := strconv.Atoi(factors[1])
				total += factor1 * factor2
			}
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

	fmt.Println("Solution Day 3 Part 1:", day03part1(file))

	file.Seek(0, 0)

	fmt.Println("Solution Day 3 Part 2:", day03part2(file))
}
