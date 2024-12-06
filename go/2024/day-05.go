package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func splitByChar(line, sep string) []int {
	output := []int{}
	for _, item := range strings.Split(line, sep) {
		toInt, _ := strconv.Atoi(item)
		output = append(output, toInt)
	}
	return output
}

func day05part1(file *os.File) int {
	scanner := bufio.NewScanner(file)
	total := 0

	rules := [][]int{}
	updates := [][]int{}

	for scanner.Scan() {
		currentLine := scanner.Text()
		if strings.Contains(currentLine, "|") {
			rules = append(rules, splitByChar(currentLine, "|"))
		}
		if strings.Contains(currentLine, ",") {
			updates = append(updates, splitByChar(currentLine, ","))
		}
	}

	for _, update := range updates {
		pairsNumber := len(update) - 1
		correctCount := 0
		for p := 0; p < pairsNumber; p++ {
			pair := []int{update[p], update[p+1]}
			for _, rule := range rules {
				if slices.Equal(rule, pair) {
					correctCount++
				}
			}

		}
		if pairsNumber == correctCount {
			total += update[(len(update)-1)/2]
		}
	}

	return total
}

func day05part2(file *os.File) int {
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

	fmt.Println("Solution Day 5 Part 1:", day05part1(file))

	file.Seek(0, 0)

	fmt.Println("Solution Day 5 Part 2:", day05part2(file))
}
