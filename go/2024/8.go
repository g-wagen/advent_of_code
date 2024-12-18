package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	_ "strconv"
	_ "strings"
    "math"
)


func permutate(slice [][]int) [][][]int{
    out := [][][]int{}
	for i := 0; i < len(slice)-1; i++ {
		for j := i; j < len(slice)-1; j++ {
            pair := [][]int{slice[i], slice[j+1]}
            out = append(out, pair)
		}
	}
    return out
}

func d8p1(file *os.File) int {
	total := 0

    // initiate antenna data structures
	antennas := []string{}
	antennasPairs := make(map[string][][][]int)
	antennasPositions := make(map[string][][]int)
	antennasAntinodes := make(map[string][][]int)

	for _, ant := range antennas {
		antennasPairs[ant] = [][][]int{}
		antennasPositions[ant] = [][]int{}
		antennasAntinodes[ant] = [][]int{}
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

    minXY := 0
    maxY := len(m)-1
    maxX := len(m[0])-1

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
            c0, c1 := pair[0], pair[1]
            x0, x1 := c0[0], c1[0]
            // flip pair if first coordinate X 
            // is larger than second coordinate X
            if x0 > x1 {
                pair = [][]int{c1, c0}
            } 
            pairs = append(pairs, pair)
        }
		antennasPairs[ant] = pairs	
    }
    

    // find all antinodes
    antinodes := make(map[string]int)

    for ant, pairs := range antennasPairs {
        for _, pair := range pairs {
            c0, c1 := pair[0], pair[1]

            c0x, c0y := c0[0], c0[1]
            c1x, c1y := c1[0], c1[1]

            xDiff := int(math.Abs(float64(c1x - c0x)))
            yDiff := int(math.Abs(float64(c1y - c0y)))

            a0x := c0x - xDiff
            a1x := c1x + xDiff
            a0y, a1y := 0, 0
            if c0y < c1y {
                a0y = c0y - yDiff
                a1y = c1y + yDiff
            } else {
                a0y = c0y + yDiff
                a1y = c1y - yDiff
            }
            if a0x >= minXY && a0x <= maxX && a0y >= minXY && a0y <= maxY {
                antinode := []int{a0x, a0y}
                antennasAntinodes[ant] = append(antennasAntinodes[ant], antinode)
                antinodes[fmt.Sprintf("%v", antinode)]++
            }
            if a1x >= minXY && a1x <= maxX && a1y >= minXY && a1y <= maxY {
                antinode := []int{a1x, a1y}
                antennasAntinodes[ant] = append(antennasAntinodes[ant], antinode)
                antinodes[fmt.Sprintf("%v", antinode)]++
            }
        }
    }
    total += len(antinodes)

	return total
}

func d8p2(file *os.File) int {
	scanner := bufio.NewScanner(file)
	total := 0

	m := []string{}

	for scanner.Scan() {
		m = append(m, scanner.Text())
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

	fmt.Println("Solution Day 8 Part 1:", d8p1(file))

	file.Seek(0, 0)

	fmt.Println("Solution Day 8 Part 2:", d8p2(file))
}
