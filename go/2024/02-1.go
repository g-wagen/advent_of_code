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

func reportsafe(levels []int) bool {
	if sort.IntsAreSorted(levels) {
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
	}
	return false
}

func main() {
	file, error := os.Open("02-input.txt")

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

		if reportsafe(fieldsi) || reportsafe(fieldsir) {
			total++
		}

	}
	fmt.Println(total)
}
