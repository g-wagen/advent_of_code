package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"sort"
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


func permute(levels []int) [][]int {
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


func reportsafe(levels []int) bool {
	if sort.IntsAreSorted(levels) {
		return checksafe(levels)
	} else {
        permutations := permute(levels)
        for i := 0; i < len(permutations); i++ {
            return checksafe(permutations[i])
            }
            
	}
	return false
}

func main() {
	file, error := os.Open("02-1-sample.txt")

	if error != nil {
		fmt.Println(error)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	total := 0

	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		fieldsi := []int{}

		for _, v := range fields {
			iv, _ := strconv.Atoi(v)
			fieldsi = append(fieldsi, iv)
		}

		fieldsir := []int{}

		for _, v := range fieldsi {
			fieldsir = append(fieldsir, v)
		}

		slices.Reverse(fieldsir)

	    fmt.Println(fields)	

        if reportsafe(fieldsi) {
			total++
		} else {
            if reportsafe(fieldsir) {
                total++
            }
        }

	}
	fmt.Println(total)
}
