package main

import (
	"bufio"
	"fmt"
	_ "math"
	"os"
	_ "regexp"
	"slices"
	_ "strconv"
	"strings"
)

func countLine(line []string) int {
	return strings.Count(strings.Join(line, ""), "XMAS") + strings.Count(strings.Join(line, ""), "SAMX")
}

func countAll(puzzle [][]string) int {
	total := 0
	for _, row := range puzzle {
		total += countLine(row)
	}
	return total
}

func diagDesc(puzzle [][]string) [][]string {
	// Shifts the puzzle rows that the diagonal descending lines become vertical
	rotated := [][]string{}
	for r, row := range puzzle {
		rl := len(row)
		safeIndex := r % rl
		newRow := slices.Concat(row[safeIndex:], row[:safeIndex])
		rotated = append(rotated, newRow)
	}
	return rotated
}

func diagAsc(puzzle [][]string) [][]string {
	// Shifts the puzzle rows that the diagonal ascending lines become vertical
	// It is weird to reverse the slice twice
	rotated := [][]string{}
	for r, row := range puzzle {
		rl := len(row)
		safeIndex := r % rl

		tempRow := []string{}
		for _, item := range slices.Backward(row) {
			tempRow = append(tempRow, item)
		}

		newRow := slices.Concat(tempRow[safeIndex:], tempRow[:safeIndex])
/*
		tempRow2 := []string{}
		for _, item := range slices.Backward(newRow) {
			tempRow2 = append(tempRow2, item)
		}
*/
		rotated = append(rotated, newRow)
	}
	return rotated
}

func rot90(puzzle [][]string) [][]string {
	// Rotates the puzzle 90 degrees clockwise
	rotated := [][]string{}
	revPuzzle := [][]string{}

	for _, item := range slices.Backward(puzzle) {
		revPuzzle = append(revPuzzle, item)
	}

	for y, _ := range puzzle[0] {
		temp := []string{}
		for x, _ := range puzzle {
			temp = append(temp, revPuzzle[x][y])
		}
		rotated = append(rotated, temp)
	}
	return rotated

}

func day04part1(file *os.File) int {
	scanner := bufio.NewScanner(file)
	total := 0

	canvas := [][]string{}

	for scanner.Scan() {
		canvas = append(canvas, strings.Split(scanner.Text(), ""))
	}

	total += countAll(canvas)
	total += countAll(rot90(canvas))
	total += countAll(rot90(diagDesc(canvas)))
	total += countAll(rot90(diagAsc(canvas)))

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
