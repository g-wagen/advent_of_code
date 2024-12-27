package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strings"
)

func convertTo2DStringSlice(file *os.File) [][]string {
	output := [][]string{}
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		text := scanner.Text()
		output = append(output, strings.Split(text, ""))
	}

	return output
}

func contains(intSlice [][]int, target []int) bool {
	for _, slice := range intSlice {
		if len(slice) != len(target) {
			continue
		}

		match := true

		for i := range slice {
			if slice[i] != target[i] {
				match = false
				break
			}
		}

		if match {
			return true
		}
	}
	return false
}

func deleteCoord(slice [][]int, coord []int) [][]int {
	return slices.DeleteFunc(slice, func(c []int) bool {
		if len(c) != len(coord) {
			return false
		}

		for i := range c {
			if c[i] != coord[i] {
				return false
			}
		}

		return true
	})
}

func getPlotRegions(plot string, coordinates [][]int) [][][]int {
	out := [][][]int{}

	coordinatesCopy := make([][]int, len(coordinates))
	for i := range coordinates {
		coordinatesCopy[i] = coordinates[i]
	}

	for len(coordinatesCopy) > 0 {

		visited := [][]int{}
		queue := [][]int{coordinatesCopy[0]}

		for len(queue) > 0 {
			pop := queue[0]
			queue = queue[1:]

			coordinatesCopy = deleteCoord(coordinatesCopy, pop)

			if !contains(visited, pop) {
				visited = append(visited, pop)
			}

			u, d, l, r := []int{pop[0] - 1, pop[1]}, []int{pop[0] + 1, pop[1]}, []int{pop[0], pop[1] - 1}, []int{pop[0], pop[1] + 1}

			for _, coord := range [][]int{u, d, l, r} {
				if contains(coordinates, coord) && !contains(visited, coord) && !contains(queue, coord) {
					queue = append(queue, coord)
				}
			}
		}

		out = append(out, visited)
	}

	return out
}

func countPlotFence(plotCoordinates [][]int) int {
	total := 0
	for _, pc := range plotCoordinates {
		fences := 4
		u, d, l, r := []int{pc[0] - 1, pc[1]}, []int{pc[0] + 1, pc[1]}, []int{pc[0], pc[1] - 1}, []int{pc[0], pc[1] + 1}
		for _, coord := range [][]int{u, d, l, r} {
			if contains(plotCoordinates, coord) {
				fences--
			}
		}
		total += fences
	}
	return total
}

func getPlotLabels(m [][]string) []string {
	p := []string{}

	for _, r := range m {
		for _, c := range r {
			col := string(c)
			if slices.Index(p, col) == -1 {
				p = append(p, col)
			}
		}
	}
	slices.Sort(p)

	return p
}

func getPlotCoordinates(p string, m [][]string) [][]int {
	coords := [][]int{}

	for y, row := range m {
		for x, col := range row {
			plot := string(col)
			if plot == p {
				coords = append(coords, []int{y, x})
			}
		}
	}

	return coords
}

func d12p1(file *os.File) int {
	input := convertTo2DStringSlice(file)

	total := 0

	labels := getPlotLabels(input)

	for _, label := range labels {
		coords := getPlotCoordinates(label, input)
		regions := getPlotRegions(label, coords)

		for _, region := range regions {
			num := len(region)
			fence := countPlotFence(region)
			mult := num * fence
			total += mult
		}
	}

	return total
}

func main() {
	file, _ := os.Open(os.Args[1])
	defer file.Close()
	fmt.Println("Solution Day 12 Part 1:", d12p1(file))
	file.Seek(0, 0)
	//fmt.Println("Solution Day 12 Part 2:", d12p2(file))
}
