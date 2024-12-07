package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strings"
)

func walk(m [][]string, pos []int, dir string) bool {
	/*
	   recursive walk

	   Args
	   ---------------
	   m [][]string: the map where the "character" walks on
	   pos []int: current position in y, x
	   dir string: current walking direction

	   Returns
	   -------
	   bool

	   And also paints pretty X's at the visited positions :)
	*/

	m[pos[0]][pos[1]] = "X"

	nextDir := ""
	nextPos := []int{0, 0}

	switch dir {
	case "up":
		nextDir = "right"
		nextPos[0] = pos[0] - 1
		nextPos[1] = pos[1]
	case "right":
		nextDir = "down"
		nextPos[0] = pos[0]
		nextPos[1] = pos[1] + 1
	case "down":
		nextDir = "left"
		nextPos[0] = pos[0] + 1
		nextPos[1] = pos[1]
	case "left":
		nextDir = "up"
		nextPos[0] = pos[0]
		nextPos[1] = pos[1] - 1
	default:
		panic("I need directions")
	}

	if nextPos[0] < 0 || nextPos[0] > len(m)-1 || nextPos[1] < 0 || nextPos[1] > len(m[0])-1 {
		return false
	}

	if m[nextPos[0]][nextPos[1]] == "#" {
		walk(m, pos, nextDir)
	}

	if m[nextPos[0]][nextPos[1]] == "X" || m[nextPos[0]][nextPos[1]] == "." {
		walk(m, nextPos, dir)
	}

	return false
}

func day06part1(file *os.File) int {
	scanner := bufio.NewScanner(file)
	total := 0

	m := [][]string{}

	for scanner.Scan() {
		m = append(m, strings.Split(scanner.Text(), ""))
	}

	start := []int{}

out:
	for y, row := range m {
		pos := slices.Index(row, "^")
		if pos != -1 {
			start = append(start, y)
			start = append(start, pos)
			break out
		}
	}

	walk(m, start, "up")

	for _, r := range m {
		for _, c := range r {
			if c == "X" {
				total++
			}
		}
	}

	return total
}

func day06part2(file *os.File) int {
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

	fmt.Println("Solution Day 6 Part 1:", day06part1(file))

	file.Seek(0, 0)

	fmt.Println("Solution Day 6 Part 2:", day06part2(file))
}
