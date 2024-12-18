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

func readInput(file *os.File) []string {
	output := []string{}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		output = append(output, scanner.Text())
	}
	return output
}

func getAntennasFromInput(input []string) []string {
	antennas := []string{}
	for _, line := range input {
		for _, char := range line {
			character := string(char)
			if character != "." && slices.Contains(antennas, character) == false {
				antennas = append(antennas, character)
			}
		}
	}
	return antennas
}

func findAntennaPositions(input []string) map[string][][]int {
	// find all antenna positions
	positions := make(map[string][][]int)
	for y, row := range input {
		for x, col := range row {
			strCol := string(col)
			if strCol != "." {
				position := []int{x, y}
				positions[strCol] = append(positions[strCol], position)
			}
		}
	}
	return positions
}

func findAntennaPairs(positions map[string][][]int) map[string][][][]int {
	// find all antenna pairs
	antennaPairs := make(map[string][][][]int)
	for ant, posis := range positions {
		permutations := permutate(posis)
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
		antennaPairs[ant] = pairs
	}
	return antennaPairs
}

func addAntinode(coords []int, antinodesMap map[string]int) {
	antinodesMap[fmt.Sprintf("%v", []int{coords[0], coords[1]})]++
}

func calculatePositionDiff(pos0, pos1 []int) (int, int) {
	xDiff := int(math.Abs(float64(pos1[0] - pos0[0])))
	yDiff := int(math.Abs(float64(pos1[1] - pos0[1])))
	return xDiff, yDiff
}

func d8p1(file *os.File) int {
	total := 0

	input := readInput(file)

	maxY := len(input) - 1
	maxX := len(input[0]) - 1

	antennasPositions := findAntennaPositions(input)
	antennasPairs := findAntennaPairs(antennasPositions)

	// find all antinodes
	antinodes := make(map[string]int)

	for _, pairs := range antennasPairs {
		for _, pair := range pairs {
			pos0, pos1 := pair[0], pair[1]

			pos0x, pos0y := pos0[0], pos0[1]
			pos1x, pos1y := pos1[0], pos1[1]

			xDiff, yDiff := calculatePositionDiff(pos0, pos1)

			anode0y, anode1y := 0, 0

			anode0x := pos0x - xDiff
			anode0y = pos0y + yDiff

			anode1x := pos1x + xDiff
			anode1y = pos1y - yDiff

			if pos0y < pos1y {
				anode0y = pos0y - yDiff
				anode1y = pos1y + yDiff
			}

			if anode0x >= 0 && anode0x <= maxX && anode0y >= 0 && anode0y <= maxY {
				antinode := []int{anode0x, anode0y}
				addAntinode(antinode, antinodes)
			}

			if anode1x >= 0 && anode1x <= maxX && anode1y >= 0 && anode1y <= maxY {
				antinode := []int{anode1x, anode1y}
				addAntinode(antinode, antinodes)
			}
		}
	}
	total += len(antinodes)

	return total
}

func d8p2(file *os.File) int {
	total := 0

	input := readInput(file)

	maxY := len(input) - 1
	maxX := len(input[0]) - 1

	antennasPositions := findAntennaPositions(input)
	antennasPairs := findAntennaPairs(antennasPositions)

	// find all antinodes
	antinodes := make(map[string]int)

	for _, pairs := range antennasPairs {
		for _, pair := range pairs {
			pos0, pos1 := pair[0], pair[1]

			pos0x, pos0y := pos0[0], pos0[1]
			pos1x, pos1y := pos1[0], pos1[1]

			xDiff, yDiff := calculatePositionDiff(pos0, pos1)

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
