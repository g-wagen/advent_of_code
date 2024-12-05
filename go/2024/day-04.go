package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strings"
)

func count(puzzle [][]string) int {
	// counts all occurences of XMAS and SMAX in one array
	total := 0
	for _, row := range puzzle {
		total += strings.Count(strings.Join(row, ""), "XMAS") + strings.Count(strings.Join(row, ""), "SAMX")
	}
	return total
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

func collectDiagDesc(puzzle [][]string) [][]string {
	// collects all array elements diagonally descending
	numRows := len(puzzle)
	numCols := len(puzzle[0])

	output := [][]string{}

	for r, row := range puzzle {
		if r == 0 {
			for c := range row {
				temp := []string{}
				for y := 0; y < numRows; y++ {
					if c+y < numCols {
						temp = append(temp, puzzle[y][c+y])
					}
				}
				output = append(output, temp)
			}
		}
		if r > 0 {
			temp2 := []string{}
			for c := 0; c < numCols; c++ {
				if r+c < numRows {
					temp2 = append(temp2, puzzle[r+c][c])
				}
			}
			output = append(output, temp2)
		}
	}
	return output
}

func day04part1(file *os.File) int {
	scanner := bufio.NewScanner(file)
	total := 0

	canvas := [][]string{}

	for scanner.Scan() {
		canvas = append(canvas, strings.Split(scanner.Text(), ""))
	}

	total += count(canvas)
	total += count(rot90(canvas))
	total += count(collectDiagDesc(canvas))
	total += count(collectDiagDesc(rot90(canvas)))

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
