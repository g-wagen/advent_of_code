package main

import (
    "bufio"
	"fmt"
    "os"
	"slices"
    "strconv"
    "strings"
)

func checksafe(levels []int) bool {
	safe := 0
	optimal := len(levels) - 1

	for i, v := range levels {
		if i > 0 && v-levels[i-1] <= 3 && v-levels[i-1] >= 1 {
			safe++
		}
	}

	if optimal == safe {
		return true
	}

	return false
}

func permutate(levels []int) [][]int {
	output := [][]int{}
	for i, _ := range levels {
		temp := []int{}
		if i == 0 {
			temp = levels[1:]
		}
		if i > 0 && i < len(levels)-1 {
			before := []int{}
			after := []int{}
			before = levels[:i]
			after = levels[i+1 : len(levels)]
			temp = slices.Concat(before, after)
		}
		if i == len(levels)-1 {
			temp = levels[:len(levels)-1]
		}
		output = append(output, temp)
	}
	return output
}

func dampener(levels []int) bool {
    if checksafe(levels) {
        return true
    }

	permutations := permutate(levels)

	for _, v := range permutations {
        if checksafe(v) {
            return true
        }
	}

	slices.Reverse(levels)

    if checksafe(levels) {
        return true
    }

	permutations = permutate(levels)

	for _, v := range permutations {
        if checksafe(v) {
            return true
        }
	}

    return false
}

func main() {
	file, error := os.Open(os.Args[1])

	if error != nil {
		fmt.Println(error)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	total := 0

	for scanner.Scan() {
		flds := strings.Fields(scanner.Text())
		fields := []int{}

		for _, v := range flds {
			iv, _ := strconv.Atoi(v)
			fields = append(fields, iv)
		}

        if dampener(fields) {
            total++
        }
    }
    fmt.Println(total)
}
