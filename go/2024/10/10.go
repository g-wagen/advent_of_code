package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func to2dIntSlice(file *os.File) [][]int {
	output := [][]int{}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		text := scanner.Text()
		line := []int{}
		for _, char := range text {
			number, _ := strconv.Atoi(string(char))
			line = append(line, number)
		}
		output = append(output, line)
	}
	return output
}

func findTrailheads(data [][]int) [][]int {
	trailheads := [][]int{}
	for y, d := range data {
		for x, c := range d {
			if c == 0 {
				trailheads = append(trailheads, []int{y, x})
			}
		}
	}
	return trailheads
}

func toIntCoords(input string) []int {
	// converts string coordinates "2,5" to [2, 5] integer slice
	y, x, _ := strings.Cut(input, ",")
	yint, _ := strconv.Atoi(y)
	xint, _ := strconv.Atoi(x)
	return []int{yint, xint}
}

func toStrCoords(input []int) string {
	// converts integer slice coordinates [2, 5] to "2,5" string
	return fmt.Sprintf("%d,%d", input[0], input[1])
}

func hike(data [][]int, trailhead []int) int {
	/*
	    hacky way to use string coordinates instead of proper slices.
		comparing if a slice contains a string is easier than checking for slices within slices.
	    but it's the advent of code... everything is allowed here :-D
	*/
	start := toStrCoords(trailhead)

	queue := []string{start}

	nines := []string{}

	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]

		currentPos := toIntCoords(current)

		elevation := data[currentPos[0]][currentPos[1]]
		nextElevation := elevation + 1

		cy, cx := currentPos[0], currentPos[1]

		// add coordinate of 9 elevation
		if elevation == 9 && slices.Contains(nines, current) == false {
			nines = append(nines, current)
		}

		// up
		if cy-1 >= 0 && data[cy-1][cx] == nextElevation {
			queue = append(queue, fmt.Sprintf("%d,%d", cy-1, cx))
		}
		// down
		if cy+1 < len(data) && data[cy+1][cx] == nextElevation {
			queue = append(queue, fmt.Sprintf("%d,%d", cy+1, cx))
		}
		// left
		if cx-1 >= 0 && data[cy][cx-1] == nextElevation {
			queue = append(queue, fmt.Sprintf("%d,%d", cy, cx-1))
		}
		// right
		if cx+1 < len(data[0]) && data[cy][cx+1] == nextElevation {
			queue = append(queue, fmt.Sprintf("%d,%d", cy, cx+1))
		}
	}

	return len(nines)

}

func hike2(data [][]int, trailhead []int) int {
	/*
	    hacky way to use string coordinates instead of proper slices.
		comparing if a slice contains a string is easier than checking for slices within slices.
	    but it's the advent of code... everything is allowed here :-D
	*/
	start := toStrCoords(trailhead)

	queue := []string{start}

	nines := []string{}

	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]

		currentPos := toIntCoords(current)

		elevation := data[currentPos[0]][currentPos[1]]
		nextElevation := elevation + 1

		cy, cx := currentPos[0], currentPos[1]

		// add coordinate of 9 elevation
		if elevation == 9 {
			nines = append(nines, current)
		}

		// up
		if cy-1 >= 0 && data[cy-1][cx] == nextElevation {
			queue = append(queue, fmt.Sprintf("%d,%d", cy-1, cx))
		}
		// down
		if cy+1 < len(data) && data[cy+1][cx] == nextElevation {
			queue = append(queue, fmt.Sprintf("%d,%d", cy+1, cx))
		}
		// left
		if cx-1 >= 0 && data[cy][cx-1] == nextElevation {
			queue = append(queue, fmt.Sprintf("%d,%d", cy, cx-1))
		}
		// right
		if cx+1 < len(data[0]) && data[cy][cx+1] == nextElevation {
			queue = append(queue, fmt.Sprintf("%d,%d", cy, cx+1))
		}
	}

	return len(nines)

}

func d10p1(file *os.File) int {
	input := to2dIntSlice(file)
	score := 0

	trailheads := findTrailheads(input)
	for _, s := range trailheads {
		score += hike(input, s)
	}

	return score
}

func d10p2(file *os.File) int {
	input := to2dIntSlice(file)
	rating := 0

	trailheads := findTrailheads(input)
	for _, s := range trailheads {
		rating += hike2(input, s)
	}

	return rating
}

func main() {
	file, _ := os.Open(os.Args[1])
	defer file.Close()

	fmt.Println("Solution Day 10 Part 1:", d10p1(file))
	file.Seek(0, 0)
	fmt.Println("Solution Day 10 Part 2:", d10p2(file))
}
