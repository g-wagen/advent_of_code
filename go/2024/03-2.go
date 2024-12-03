package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	file, error := os.Open(os.Args[1])

	if error != nil {
		fmt.Println(error)
		return
	}
	defer file.Close()

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
				factorsString := subPattern.FindAllString(v, -1)
				factors := []int{}

				for _, m := range factorsString {
					conv, _ := strconv.Atoi(m)
					factors = append(factors, conv)
				}
				product := factors[0] * factors[1]

				total += product
			}
		}
	}
	fmt.Println(total)
}
