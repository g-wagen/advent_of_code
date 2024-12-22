package main

import (
	"bufio"
	"fmt"
	"os"
	_ "slices"
	"strconv"
)

func readInput(file *os.File) [][]int {
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

func startsEnds (data [][]int) ([][]int, [][]int) {

    starts := [][]int{}
    ends := [][]int{}

    start := 0
    end := 9

    for y, d := range data {
        for x, c := range d {
            coord := []int{y, x}
            if c == start {
                starts = append(starts, coord)
            }
            if c == end {
                ends = append(ends, coord)
            }
        }
    }
    return starts, ends
}

func hike (data [][]int, s []int, e [][]int) int {
    /*
    recursive?
    walk uphill (current value + 1).
    remember if path can split.
    stop current branch if path goes downhill (current value - 1).
    stop if end was reached.
    only count unique end positions.
    increment score if new 9 can be reached from start point.
    */
}

func d10p1(file *os.File) int {
	input := readInput(file)
    total := 0
    starts, ends := startsEnds(input)
    for _, s := range starts {
        total += hike(input, s, ends)

	return total
}

func d10p2(file *os.File) int {
	//input := readInput(file)

	return 2
}

func main() {
	file, error := os.Open(os.Args[1])

	if error != nil {
		fmt.Println(error)
		return
	}

	defer file.Close()

	fmt.Println("Solution Day 10 Part 1:", d10p1(file))

	file.Seek(0, 0)

	fmt.Println("Solution Day 10 Part 2:", d10p2(file))
}
