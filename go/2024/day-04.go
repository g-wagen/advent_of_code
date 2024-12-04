package main

import (
	"bufio"
	"fmt"
	"os"
	_ "regexp"
	_ "slices"
	_ "strconv"
	"strings"
)

func countHoriz(line []string) int {
	return strings.Count(strings.Join(line, ""), "XMAS") + strings.Count(strings.Join(line, ""), "SAMX")
}

func day04part1(file *os.File) int {
	scanner := bufio.NewScanner(file)
	total := 0

	canvas := [][]string{}

	for scanner.Scan() {
		puzzleInput := scanner.Text()
		currentLine := strings.Split(puzzleInput, "")
		canvas = append(canvas, currentLine)
		fmt.Println(currentLine, countHoriz(currentLine))
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
