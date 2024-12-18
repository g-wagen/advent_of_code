package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
	_ "strconv"
	_ "strings"
)

func permutate(slice [][]int) [][][]int {
	out := [][][]int{}
	for i := 0; i < len(slice)-1; i++ {
		for j := i; j < len(slice)-1; j++ {
			pair := [][]int{slice[i], slice[j+1]}
			out = append(out, pair)
		}
	}
	return out
}

func readInput(file *os.File) []string{
	output := []string{}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		output = append(output, scanner.Text())
	}
    return output
}

func d8p1(file *os.File) int {
	total := 0

	// initiate antenna data structures
	antennas := []string{}
	antennasPairs := make(map[string][][][]int)
	antennasPositions := make(map[string][][]int)

	for _, ant := range antennas {
		antennasPairs[ant] = [][][]int{}
		antennasPositions[ant] = [][]int{}
	}

	m := []string{}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		currentLine := scanner.Text()
		for _, char := range currentLine {
			strChar := string(char)
			if strChar != "." && slices.Contains(antennas, strChar) == false {
				antennas = append(antennas, strChar)
			}
		}
		m = append(m, currentLine)
	}

	maxY := len(m) - 1
	maxX := len(m[0]) - 1

	// find all antenna positions
	for y, row := range m {
		for x, col := range row {
			strCol := string(col)
			if strCol != "." {
				position := []int{x, y}
				antennasPositions[strCol] = append(antennasPositions[strCol], position)
			}
		}
	}

	// find all antenna pairs
	for ant, positions := range antennasPositions {
		permutations := permutate(positions)
		pairs := [][][]int{}
		for _, pair := range permutations {
			pos0, pos1 := pair[0], pair[1]
			x0, x1 := pos0[0], pos1[0]
			// flip pair if first coordinate X
			// is larger than second coordinate X
			if x0 > x1 {
				pair = [][]int{pos1, pos0}
			}
			pairs = append(pairs, pair)
		}
		antennasPairs[ant] = pairs
	}

	// find all antinodes
	antinodes := make(map[string]int)

	for _, pairs := range antennasPairs {
		for _, pair := range pairs {
			pos0, pos1 := pair[0], pair[1]

			pos0x, pos0y := pos0[0], pos0[1]
			pos1x, pos1y := pos1[0], pos1[1]

			xDiff := int(math.Abs(float64(pos1x - pos0x)))
			yDiff := int(math.Abs(float64(pos1y - pos0y)))

			anode0x := pos0x - xDiff
			anode1x := pos1x + xDiff
			anode0y, anode1y := 0, 0
			
            anode0y = pos0y + yDiff
			anode1y = pos1y - yDiff
			
            if pos0y < pos1y {
				anode0y = pos0y - yDiff
				anode1y = pos1y + yDiff
			}

			if anode0x >= 0 && anode0x <= maxX && anode0y >= 0 && anode0y <= maxY {
				antinode := []int{anode0x, anode0y}
				antinodes[fmt.Sprintf("%v", antinode)]++
			}
			if anode1x >= 0 && anode1x <= maxX && anode1y >= 0 && anode1y <= maxY {
				antinode := []int{anode1x, anode1y}
				antinodes[fmt.Sprintf("%v", antinode)]++
			}
		}
	}
	total += len(antinodes)

	return total
}

func d8p2(file *os.File) int {
	total := 0

	// initiate antenna data structures
	antennas := []string{}
	antennasPairs := make(map[string][][][]int)
	antennasPositions := make(map[string][][]int)

	for _, ant := range antennas {
		antennasPairs[ant] = [][][]int{}
		antennasPositions[ant] = [][]int{}
	}

	m := []string{}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		currentLine := scanner.Text()
		for _, char := range currentLine {
			strChar := string(char)
			if strChar != "." && slices.Contains(antennas, strChar) == false {
				antennas = append(antennas, strChar)
			}
		}
		m = append(m, currentLine)
	}

	maxY := len(m) - 1
	maxX := len(m[0]) - 1

	// find all antenna positions
	for y, row := range m {
		for x, col := range row {
			strCol := string(col)
			if strCol != "." {
				position := []int{x, y}
				antennasPositions[strCol] = append(antennasPositions[strCol], position)
			}
		}
	}

	// find all antenna pairs
	for ant, positions := range antennasPositions {
		permutations := permutate(positions)
		pairs := [][][]int{}
		for _, pair := range permutations {
			pos0, pos1 := pair[0], pair[1]
			x0, x1 := pos0[0], pos1[0]
			// flip pair if first coordinate X
			// is larger than second coordinate X
			if x0 > x1 {
				pair = [][]int{pos1, pos0}
			}
			pairs = append(pairs, pair)
		}
		antennasPairs[ant] = pairs
	}

	// find all antinodes
	antinodes := make(map[string]int)

	for _, pairs := range antennasPairs {
		for _, pair := range pairs {
			pos0, pos1 := pair[0], pair[1]

			pos0x, pos0y := pos0[0], pos0[1]
			pos1x, pos1y := pos1[0], pos1[1]

			xDiff := int(math.Abs(float64(pos1x - pos0x)))
			yDiff := int(math.Abs(float64(pos1y - pos0y)))

			antinodes[fmt.Sprintf("%v", pos0)]++
			antinodes[fmt.Sprintf("%v", pos1)]++

			if pos0y < pos1y {
				// ascending line
				//
				// go left down
				ix, iy := pos0x, pos0y
				for ix >= 0 && iy >= 0 {
					antinode := []int{ix, iy}
					antinodes[fmt.Sprintf("%v", antinode)]++
					ix -= xDiff
					iy -= yDiff
				}
				ix, iy = pos1x, pos1y
				for ix >= 0 && iy >= 0 {
					antinode := []int{ix, iy}
					antinodes[fmt.Sprintf("%v", antinode)]++
					ix -= xDiff
					iy -= yDiff
				}
				// go right up
				ix, iy = pos0x, pos0y
				for ix <= maxX && iy <= maxY {
					antinode := []int{ix, iy}
					antinodes[fmt.Sprintf("%v", antinode)]++
					ix += xDiff
					iy += yDiff
				}
				ix, iy = pos1x, pos1y
				for ix <= maxX && iy <= maxY {
					antinode := []int{ix, iy}
					antinodes[fmt.Sprintf("%v", antinode)]++
					ix += xDiff
					iy += yDiff
				}
			} else {
				// descending line
				//

				// go left up
				ix, iy := pos0x, pos0y
				for ix >= 0 && iy <= maxY {
					antinode := []int{ix, iy}
					antinodes[fmt.Sprintf("%v", antinode)]++
					ix -= xDiff
					iy += yDiff
				}
				ix, iy = pos1x, pos1y
				for ix >= 0 && iy <= maxY {
					antinode := []int{ix, iy}
					antinodes[fmt.Sprintf("%v", antinode)]++
					ix -= xDiff
					iy += yDiff
				}
				// go right down
				ix, iy = pos0x, pos0y
				for ix <= maxX && iy >= 0 {
					antinode := []int{ix, iy}
					antinodes[fmt.Sprintf("%v", antinode)]++
					ix += xDiff
					iy -= yDiff
				}
				ix, iy = pos1x, pos1y
				for ix <= maxX && iy >= 0 {
					antinode := []int{ix, iy}
					antinodes[fmt.Sprintf("%v", antinode)]++
					ix += xDiff
					iy -= yDiff
				}
			}
		}
	}
	total += len(antinodes)

	return total
}

func main() {
	file, error := os.Open(os.Args[1])

	if error != nil {
		fmt.Println(error)
		return
	}

	defer file.Close()

	fmt.Println("Solution Day 8 Part 1:", d8p1(file))

	file.Seek(0, 0)

	fmt.Println("Solution Day 8 Part 2:", d8p2(file))
}
