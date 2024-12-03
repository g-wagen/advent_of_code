package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func day04part1(file *os.File) int {
	scanner := bufio.NewScanner(file)
	total := 0

	for scanner.Scan() {
		//puzzleInput := scanner.Text()
	}
	return total
}

func day04part2(file *os.File) int {
	scanner := bufio.NewScanner(file)
	total := 0

	for scanner.Scan() {
		//puzzleInput := scanner.Text()
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

	fmt.Println("Solution Day 4 Part 1:", day04part1(file))

	file.Seek(0, 0)

	fmt.Println("Solution Day 4 Part 2:", day04part2(file))
}
