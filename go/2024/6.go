package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

// dirty global variable
var visited = [][]int{}

var cycles = 0

func walk(m [][]string, pos []int, dir string, cycleCheck bool) bool {
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

	   And also records all visited positions to a global variable
	*/

	visited = append(visited, pos)

	if cycleCheck == true && isCycle(visited) == true {
		cycles++
		return false
	}

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
		walk(m, pos, nextDir, cycleCheck)
	}

	if m[nextPos[0]][nextPos[1]] == "X" || m[nextPos[0]][nextPos[1]] == "." {
		walk(m, nextPos, dir, cycleCheck)
	}

	return false
}

func d6p1(file *os.File) int {
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

	walk(m, start, "up", false)

	// store unique positions in this map like:
	// "12,10":"12,10"
	// using string keys might be weird but it works
	uniquePositions := make(map[string]string)

	for _, v := range visited {
		key := strconv.Itoa(v[0]) + "," + strconv.Itoa(v[1])
		uniquePositions[key] = key
	}

	total += len(uniquePositions)

	return total
}

func isCycle(positions [][]int) bool {
	strPos := []string{}

	repeating := []string{}

	for _, pos := range positions {
		strPos = append(strPos, strconv.Itoa(pos[0])+","+strconv.Itoa(pos[1]))
	}

	for p, pos := range strPos {
		count := 0
		for _, dupe := range strPos {
			if pos == dupe {
				count++
			}
		}
		if count > 1 {
			count2 := 0
			for _, dupe2 := range strPos {
				if p+1 < len(strPos)-1 && strPos[p+1] == dupe2 {
					count2++
				}
			}
			if count2 > 1 {
				repeating = append(repeating, pos)
			}
		}
	}

	if len(repeating) > 3 {
		return true
	}

	return false
}

func d6p2(file *os.File) int {
	scanner := bufio.NewScanner(file)

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

	for y := range m {
		for x := range m[0] {
			if m[y][x] != "#" || m[y][x] != "^" {
				current := m[y][x]
				newM := make([][]string, len(m))
				copy(newM, m)
				newM[y][x] = "#"
				fmt.Println("----------")
				for _, a := range newM {
					fmt.Println(a)
				}

				walk(newM, start, "up", true)
				newM[y][x] = current
			}
		}
	}

	return cycles
}

func main() {
	file, error := os.Open(os.Args[1])

	if error != nil {
		fmt.Println(error)
		return
	}

	defer file.Close()

	fmt.Println("Solution Day 6 Part 1:", d6p1(file))

	file.Seek(0, 0)

	fmt.Println("Solution Day 6 Part 2:", d6p2(file))
}
